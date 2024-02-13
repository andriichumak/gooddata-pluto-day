"""SBDB tap class."""

from __future__ import annotations

from singer_sdk import Tap
from singer_sdk import typing as th  # JSON schema typing helpers

from tap_sbdb.streams import SmallBodiesStream, SBDBStream


class TapSBDB(Tap):
    """SBDB tap class."""

    name = "tap-sbdb"

    config_jsonschema = th.PropertiesList(
        th.Property(
            "fields",
            th.ArrayType(th.StringType),
            required=True,
            description="A list of fields to retrieve from SBDB"
        ),
        th.Property(
            "filters",
            th.StringType,
            required=False,
            description='Filters for the query, e.g. {"AND":["diameter|GE|0.14"]}',
        ),
    ).to_dict()

    def discover_streams(self) -> list[SBDBStream]:
        """Return a list of discovered streams.

        Returns:
            A list of discovered streams.
        """
        return [
            SmallBodiesStream(self),
        ]


if __name__ == "__main__":
    TapSBDB.cli()
