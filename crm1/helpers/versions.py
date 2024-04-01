from dataclasses import dataclass
from typing import Optional
from enum import Enum


class VersionEndMode(Enum):
    INCLUSIVE = "inclusive"
    EXCLUSIVE = "exclusive"


DONTCARE = VersionEndMode.EXCLUSIVE


@dataclass
class Version:
    major: int
    minor: int
    patch: int

    @staticmethod
    def from_string(version: str) -> "Version":
        parts = version.split(".")
        if len(parts) < 2:
            raise ValueError("Invalid version string")
        if len(parts) > 3:
            raise ValueError("Invalid version string")
        major = int(parts[0])
        minor = int(parts[1])
        patch = int(parts[2]) if len(parts) == 3 else 0
        return Version(major, minor, patch)

    def to_string(self) -> str:
        return f"{self.major}.{self.minor}" + (
            f".{self.patch}" if self.patch is not None else ""
        )

    def __eq__(self, other: "Version") -> bool:
        return (
            self.major == other.major
            and self.minor == other.minor
            and self.patch == other.patch
        )

    def __lt__(self, other: "Version") -> bool:
        if self.major < other.major:
            return True
        if self.major > other.major:
            return False
        if self.minor < other.minor:
            return True
        if self.minor > other.minor:
            return False
        if self.patch < other.patch:
            return True
        return False

    def __le__(self, other: "Version") -> bool:
        return self == other or self < other

    def __gt__(self, other: "Version") -> bool:
        return not self <= other

    def __ge__(self, other: "Version") -> bool:
        return not self < other

    def __ne__(self, other: "Version") -> bool:
        return not self == other

    def __hash__(self) -> int:
        return hash((self.major, self.minor, self.patch))

    def __repr__(self) -> str:
        return f"Version({self.major}, {self.minor}, {self.patch})"

    def __str__(self) -> str:
        return self.to_string()


@dataclass
class VersionRange:
    lower: Optional[Version]
    lower_mode: VersionEndMode
    upper: Optional[Version]
    upper_mode: VersionEndMode
    
    def __post_init__(self):
        if self.lower is not None and self.upper is not None and self.lower > self.upper:
            raise ValueError("Invalid range")

    @staticmethod
    def from_string(range_: str) -> "VersionRange":
        if range_.startswith("["):
            lower_mode = VersionEndMode.INCLUSIVE
        elif range_.startswith("("):
            lower_mode = VersionEndMode.EXCLUSIVE
        else:
            raise ValueError("Invalid range string")
        if range_.endswith("]"):
            upper_mode = VersionEndMode.INCLUSIVE
        elif range_.endswith(")"):
            upper_mode = VersionEndMode.EXCLUSIVE
        else:
            raise ValueError("Invalid range string")
        range_ = range_[1:-1]
        parts = range_.split(",")
        if len(parts) != 2:
            raise ValueError("Invalid range string")
        lower = Version.from_string(parts[0]) if parts[0] else None
        upper = Version.from_string(parts[1]) if parts[1] else None
        return VersionRange(lower, lower_mode, upper, upper_mode)

    def to_string(self) -> str:
        if self.lower is not None and self.upper is not None and self.lower == self.upper:
            return self.lower.to_string()
        return (
            ("[" if self.lower_mode == VersionEndMode.INCLUSIVE else "(")
            + (self.lower.to_string() if self.lower else "")
            + ","
            + (self.upper.to_string() if self.upper else "")
            + ("]" if self.upper_mode == VersionEndMode.INCLUSIVE else ")")
        )

    def contains(self, version: Version) -> bool:
        if self.lower is not None:
            if self.lower_mode == VersionEndMode.INCLUSIVE:
                if version < self.lower:
                    return False
            else:
                if version <= self.lower:
                    return False
        if self.upper is not None:
            if self.upper_mode == VersionEndMode.INCLUSIVE:
                if version > self.upper:
                    return False
            else:
                if version >= self.upper:
                    return False
        return True

    def __contains__(self, version: Version) -> bool:
        return self.contains(version)

    def __str__(self) -> str:
        return self.to_string()


def range_from_maven_string(version: str):
    if version.startswith(">="):
        lower_mode = VersionEndMode.INCLUSIVE
        lower = Version.from_string(version[2:])
        upper = None
        upper_mode = DONTCARE
    elif version.startswith(">"):
        lower_mode = VersionEndMode.EXCLUSIVE
        lower = Version.from_string(version[1:])
        upper = None
        upper_mode = DONTCARE
    elif version.startswith("<="):
        lower_mode = DONTCARE
        lower = None
        upper = Version.from_string(version[2:])
        upper_mode = VersionEndMode.INCLUSIVE
    elif version.startswith("<"):
        lower_mode = DONTCARE
        lower = None
        upper = Version.from_string(version[1:])
        upper_mode = VersionEndMode.EXCLUSIVE
    else:
        lower_mode = VersionEndMode.INCLUSIVE
        lower = Version.from_string(version)
        upper = Version.from_string(version)
        upper_mode = VersionEndMode.INCLUSIVE
    return VersionRange(lower, lower_mode, upper, upper_mode)
