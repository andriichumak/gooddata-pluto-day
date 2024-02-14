from pathlib import Path
from urllib.parse import quote_plus
import yaml
from dotenv import get_variable
from argparse import ArgumentParser
from GDConfig import GDConfig
from gooddata_sdk import GoodDataSdk, CatalogDataSourceSnowflake, SnowflakeAttributes, BasicCredentials


def main():
    # Parse args
    parser = ArgumentParser()
    parser.add_argument('-p', '--profile', help='Profile name', default='dev')
    args = parser.parse_args()

    # Load GD config and instantiate SDK
    config = GDConfig.load(Path('gooddata.yaml'), args.profile)
    sdk = GoodDataSdk.create(config.host, config.token)

    # Load datasource details
    snowflake_password = get_variable('.env', 'TARGET_SNOWFLAKE_PASSWORD')
    with open('meltano.yml') as f:
        meltano_config = yaml.safe_load(f.read())
    snowflake_config = next(x for x in meltano_config['plugins']['loaders'] if x['name'] == 'target-snowflake')['config']

    # Deploy the datasource
    data_source = CatalogDataSourceSnowflake(
        id=config.data_source_id,
        name=snowflake_config['schema'],
        db_specific_attributes=SnowflakeAttributes(
            db_name=quote_plus(snowflake_config['database']),
            account=snowflake_config['account'],
            warehouse=snowflake_config['warehouse'],
        ),
        schema=snowflake_config['schema'],
        credentials=BasicCredentials(
            username=snowflake_config['user'],
            password=snowflake_password,
        ),
    )
    sdk.catalog_data_source.create_or_update_data_source(data_source)


main()
