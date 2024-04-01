"""Don't import this module directly."""

from functools import lru_cache

import hjson
import requests

from . import data as datacls


@lru_cache(maxsize=128)
def get_request(address: str) -> dict:
    """Performs a GET request to the given address and returns the HJSON response."""
    response = requests.get(address, timeout=5)
    return hjson.loads(response.text)


def fetch_repository(address: str) -> datacls.resp.RRepository:
    """Fetches a repository from the given address."""
    data = get_request(address)
    return datacls.resp.RRepository.from_dict(data)
