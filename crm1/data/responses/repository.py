"""Don't import this module directly."""

from dataclasses import dataclass

from dataclasses_json import LetterCase, dataclass_json

from .mod import RMod


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class RRepository:
    """Raw repository data. This is used for deserialization."""

    spec_version: int
    """The version of the repository specification."""
    last_updated: int
    """The timestamp of the last update of the repository."""
    root_id: str
    """The root ID of the repository."""
    mods: list[RMod]
    """A list of mods in the repository."""
