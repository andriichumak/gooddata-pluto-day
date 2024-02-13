"""Stream type classes for tap-sbdb."""

from __future__ import annotations

import copy
import typing as t

from singer_sdk import typing as th, Tap
from tap_sbdb.client import SBDBStream


class SmallBodiesStream(SBDBStream):
    """Define custom stream."""

    name = "sbdb"
    path = "/sbdb_query.api"
    primary_keys: t.ClassVar[list[str]] = ["id"]
    replication_key = None

    def __init__(
            self,
            tap: Tap,
            name: str | None = None,
            path: str | None = None
    ):
        props = [
            th.Property(
                "id",
                th.StringType,
                description="Small Body ID",
                required=True
            )
        ]
        conf = copy.copy(dict(tap.config))
        for prop in conf["fields"]:
            props.append(th.Property(
                prop,
                th.OneOf(th.StringType, th.IntegerType),
                required=False
            ))
        super().__init__(name=name, schema=th.PropertiesList(*props).to_dict(), tap=tap, path=path)
