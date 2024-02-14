from pathlib import Path
from argparse import ArgumentParser
from GDConfig import GDConfig
from gooddata_sdk import GoodDataSdk


def main():
    # Parse args
    parser = ArgumentParser()
    parser.add_argument('-p', '--profile', help='Profile name', default='dev')
    args = parser.parse_args()

    # Load GD config and instantiate SDK
    config = GDConfig.load(Path('gooddata.yaml'), args.profile)
    sdk = GoodDataSdk.create(config.host, config.token)

    # Clear the cache
    sdk.catalog_data_source.register_upload_notification(config.data_source_id)


main()
