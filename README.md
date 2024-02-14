# Pluto Day

This is a demo dashboard created to showcase a complete data pipeline with GoodData for VS Code.

* Data ingestion is done with Meltano's REST API extractor.
* Data is stored in Snowflake.
* Data is transformed with dbt.
* The analytical project is created with GoodData for VS Code.

You can find a source code for the dashboard on [GitHub](https://github.com/andriichumak/gooddata-pluto-day).

# Installation

Most of the tooling require Python, for GoodData for VS Code we recommend to install our
[VS Code extension](https://marketplace.visualstudio.com/items?itemName=GoodData.gooddata-vscode)
and run deployment from there. Or you can use
[the CLI Utility](https://www.npmjs.com/package/@gooddata/code-cli), but make sure you have NodeJS on your machine.

Install Python dependencies and Meltano plugins:

```bash
pip install -r requirements.txt
meltano install
```

In case you choose to run GoodData for VS Code from CLI, install NPM dependencies:

```bash
npm i
```

# Setting up the environment

Create a new file `.env`, make sure to not commit it to Git (it's already in `.gitignore`).

Add the following env variables to the `.env`:

```
TARGET_SNOWFLAKE_PASSWORD='your-snowflake-password'
DBT_SNOWFLAKE_PASSWORD='your-snowflake-password'
GOODDATA_API_TOKEN='your-gd-token-for-dev-env'
GOODDATA_API_TOKEN_DEMO='your-gd-token-for-demo-env'
```

You will also need to update Snowflake connection properties in [`meltano.yml`](./meltano.yml) file in your fork of the repo,
feel free to commit those.

# Running the pipelines

## Data ingestion

Data ingestion is done with Meltano, run:

```bash
meltano run tap-rest-api-msdk tap-sbdb target-snowflake
```

## Data transformation

Data transformation is done with dbt, run:

```bash
meltano --environment dev run dbt-snowflake:run
```

## Provision data source to GoodData

Python script can help you with data source provisioning to GoodData server:

```bash
python scripts/deploy.py --profile dev
```

## Provision analytics

If you're using VS Code extension, open the project in VS Code, press Cmd+P (or Ctrl+P on Windows/Linux),
then search for "GoodData deploy" command and press Enter. Select the profile you'd like to deploy to in the popup.

If you're using CLI, run:

```bash
npx gd deploy --profile dev
```

## Clearing the database cache

Whenever you have a new data in the database, or you've updated the database schema,
you need to let GoodData server know about that. There is a Python script prepared for this:

```bash
python scripts/clear_cache.py --profile dev
```

# Credits

This project is loading data from two sources:
* [The Solar System OpenData](https://api.le-systeme-solaire.net/en/)
* [NASA JPL Small Bodies Database](https://ssd-api.jpl.nasa.gov/doc/sbdb_query.html)
