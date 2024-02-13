"""REST client handling, including SBDBStream base class."""

from __future__ import annotations

import copy
from typing import Any, Callable, Iterable

import requests
from singer_sdk.streams import RESTStream

_Auth = Callable[[requests.PreparedRequest], requests.PreparedRequest]


class SBDBStream(RESTStream):
    """SBDB stream class."""

    @property
    def url_base(self) -> str:
        """Return the API URL root, configurable via tap settings."""
        return "https://ssd-api.jpl.nasa.gov"

    def get_url_params(
        self,
        context: dict | None,  # noqa: ARG002
        next_page_token: Any | None,  # noqa: ANN401
    ) -> dict[str, Any]:
        """Return a dictionary of values to be used in URL parameterization.

        Args:
            context: The stream context.
            next_page_token: The next page index or value.

        Returns:
            A dictionary of URL query parameters.
        """
        conf = copy.copy(dict(self.config))
        params: dict = {
            "full-prec": False,
            "sb-xfrag": 1,
            "www": 1,
            "fields": ",".join(conf["fields"])
        }
        if "filters" in conf:
            # e.g. {"AND":["diameter|GE|0.14"]}
            params["sb-cdata"] = conf["filters"]
        return params

    def parse_response(self, response: requests.Response) -> Iterable[dict]:
        """Parse the response and return an iterator of result records.

        Args:
            response: The HTTP ``requests.Response`` object.

        Yields:
            Each record from the source.
        """
        json = response.json()

        header = json["fields"]
        for entry in json["data"]:
            yield dict([(header[ind], x) for ind, x in enumerate(entry)])
