from typing import Pattern
from typing_extensions import Final

from .types import ServerVersion

version_regex: Final[Pattern[str]]

def split_server_version_string(version_string: str) -> ServerVersion: ...
