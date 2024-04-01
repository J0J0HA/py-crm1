"""Don't import this module directly."""

from dataclasses import dataclass
from typing import Optional

from dataclasses_json import CatchAll, LetterCase, dataclass_json

from .. import data as datacls


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class KnownModExt:
    """Some known mod.ext data."""

    icon: Optional[str] = None
    """A URL to the mod's icon."""
    modid: Optional[str] = None
    """The mod's ID. This is similar to mod.id, but does not include the group. Eg. `examplemod`."""
    loader: Optional[str] = None
    """Which mod loader the mod uses. Eg. `fabric`."""
    loader_version: Optional[str] = None
    """Which version of the mod loader the mod uses. Eg. `0.11.3`."""
    source: Optional[str] = None
    """A URL to the mod's source code."""
    issues: Optional[str] = None
    """A URL to the mod's issue tracker."""
    owner: Optional[str] = None
    """The name of the mod's owner."""
    changelog: Optional[str] = None
    """A URL to the releases's changelog."""
    published_at: Optional[int] = None
    """The time the release was published at, in milliseconds since the Unix epoch."""
    alt_download: Optional[list[list[str, str]]] = None
    """A list of alternative download URLs.
    Each element is a list of two strings: the name and the URL."""
    suggests: Optional[list[datacls.resp.RDependency]] = None
    """A list of suggested mods, that are not required
    but are recommended to be installed with this mod."""
    prerelease: Optional[bool] = None
    """Pre-release status of the mod release. If true, the mod's release is a pre-release."""
    ext: Optional[dict] = CatchAll
    """All mod.ext data that is not covered by the above fields."""
