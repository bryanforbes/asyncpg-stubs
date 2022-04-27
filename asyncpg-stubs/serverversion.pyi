import typing
import typing_extensions

from .types import ServerVersion

version_regex: typing.Any

class _VersionDict(typing_extensions.TypedDict):
    major: int
    minor: typing.Optional[int]
    micro: typing.Optional[int]
    releaselevel: typing.Optional[str]
    serial: typing.Optional[int]

def split_server_version_string(version_string: str) -> ServerVersion: ...
