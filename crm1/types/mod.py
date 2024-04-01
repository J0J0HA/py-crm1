"""Don't import this module directly."""

from .dependency import Dependency
from .. import spec


class Mod:
    """This class represents a mod.

    Raises:
        ValueError: If the data is not of type spec.RMod
    """

    meta: spec.RMod
    """The raw data of the mod."""

    def __init__(self, data: spec.RMod):
        self.meta = data
        if not isinstance(self.meta, spec.RMod):
            raise ValueError("Invalid data type")

    @property
    def known_ext(self) -> spec.UnsafeModExt:
        """Converts the ext field to a KnownModExt object.
        This allows for easier access to the fields in the ext field."""
        return spec.UnsafeModExt.from_dict(self.meta.ext)

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
