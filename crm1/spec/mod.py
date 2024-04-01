"""Don't import this module directly."""

from dataclasses import dataclass

from dataclasses_json import LetterCase, dataclass_json

from .dependency import RDependency
from .unsafe_modext import UnsafeModExt


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class RMod:
    """Raw mod data. This is used for deserialization."""

    id: str
    """Mod ID. This is in the format of group.id, like `com.example.mod`."""
    name: str
    """Mod name."""
    desc: str
    """A short description of the mod."""
    authors: list[str]
    """A list of the authors' names of the mod."""
    version: str
    """The version of the mod."""
    game_version: str
    """The version of the game that the mod is compatible with."""
    url: str
    """The download URL of the mod's jar."""
    deps: list[RDependency]
    """A list of dependencies of the mod."""
    ext: dict | UnsafeModExt
    """Some optional additional info of the mod."""
