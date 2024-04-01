"""Don't import this module directly."""

from dataclasses import dataclass
from typing import Optional

from dataclasses_json import LetterCase, dataclass_json


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class RDependency:
    """Raw dependency data. This is used for deserialization."""

    id: str
    """The ID of the mod."""
    version: str
    """The version of the mod."""
    source: Optional[str]
    """The repository rootId of the mod."""
