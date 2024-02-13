# Pluto Day

This is a demo dashboard created to showcase a complete data pipeline with GoodData for VS Code.

* Data ingestion is done with Meltano's REST API extractor.
* Data is stored in Snowflake.
* Data is transformed with dbt.
* The analytical project is created with GoodData for VS Code.

You can find a source code for the dashboard on [GitHub](https://github.com/andriichumak/gooddata-pluto-day).

# Credits

This project is loading data from two sources:
* [The Solar System OpenData](https://api.le-systeme-solaire.net/en/)
* [NASA JPL Small Bodies Database](https://ssd-api.jpl.nasa.gov/doc/sbdb_query.html)
