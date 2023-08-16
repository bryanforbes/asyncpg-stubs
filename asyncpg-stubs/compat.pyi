from asyncio import Future, StreamWriter
from collections.abc import Awaitable
from pathlib import Path
from typing import Final, TypeVar

_T = TypeVar('_T')

SYSTEM: Final[str]

def get_pg_home_directory() -> Path | None: ...
async def wait_closed(stream: StreamWriter) -> None: ...
async def wait_for(
    fut: Future[_T] | Awaitable[_T],
    timeout: float | None,
) -> _T: ...
