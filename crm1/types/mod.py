"""Don't import this module directly."""

from .. import data as datacls
from .dependency import Dependency


class Mod:
    """This class represents a mod.

    Raises:
        ValueError: If the data is not of type datacls.resp.RMod
    """

    meta: datacls.resp.RMod
    """The raw data of the mod."""

    def __init__(self, data: datacls.resp.RMod):
        self.meta = data
        if not isinstance(self.meta, datacls.resp.RMod):
            raise ValueError("Invalid data type")

    @property
    def known_ext(self) -> datacls.KnownModExt:
        """Converts the ext field to a KnownModExt object.
        This allows for easier access to the fields in the ext field."""
        return datacls.KnownModExt.from_dict(self.meta.ext)

    @property
    def id(self) -> str:
        """The ID of the mod."""
        return self.meta.id

    @property
    def depends(self) -> list[Dependency]:
        """The dependencies of the mod."""
        return [Dependency(dep) for dep in self.meta.deps]

    @property
    def suggests(self) -> list[Dependency]:
        """The suggestions of the mod."""
        if self.known_ext.suggests is not None:
            return [Dependency(dep) for dep in self.known_ext.suggests]
