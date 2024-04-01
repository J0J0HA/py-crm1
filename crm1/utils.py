"""Don't import this module directly."""

from functools import lru_cache
from typing import overload

import hjson
import requests

from . import datacls
from .types import Repository, RepositoryPool


@lru_cache(maxsize=128)
def get_request(address: str) -> dict:
    """Performs a GET request to the given address and returns the HJSON response."""
    response = requests.get(address, timeout=5)
    return hjson.loads(response.text)


def fetch_repository(address: str) -> datacls.resp.RRepository:
    """Fetches a repository from the given address."""
    data = get_request(address)
    return datacls.resp.RRepository.from_dict(data)


@overload
def make_pool(repos: list[Repository]) -> RepositoryPool:
    """Creates a repository pool from a list of repositories."""


@overload
def make_pool(*repos: Repository) -> RepositoryPool:
    """Creates a repository pool from multiple repositories."""


def make_pool(*repos):
    """Above"""
    if len(repos) == 1 and isinstance(repos[0], list):
        repos = repos[0]
    pool = RepositoryPool()
    for repo in repos:
        if not isinstance(repo, Repository):
            raise TypeError("Invalid repository", repo)
        pool.add_repository(repo)
    return pool
