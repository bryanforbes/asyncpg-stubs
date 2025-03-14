import enum
import sys
from asyncio import StreamWriter
from pathlib import Path
from typing import Any, Final

SYSTEM: Final[str]

def get_pg_home_directory() -> Path | None: ...
async def wait_closed(stream: StreamWriter) -> None: ...

if sys.version_info >= (3, 12):
    from asyncio import wait_for as wait_for
    from inspect import markcoroutinefunction as markcoroutinefunction
else:
    from ._asyncio_compat import wait_for as wait_for
    def markcoroutinefunction(c: Any) -> None: ...

if sys.version_info >= (3, 11):
    from asyncio import timeout as timeout_ctx
else:
    from async_timeout import timeout as timeout_ctx

if sys.version_info >= (3, 11):
    from enum import StrEnum as StrEnum
else:
    class StrEnum(str, enum.Enum): ...  # type: ignore[misc]
