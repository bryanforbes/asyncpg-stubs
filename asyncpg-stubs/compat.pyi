from asyncio import AbstractEventLoop, Future, StreamWriter, Task
from collections.abc import Awaitable
from pathlib import Path
from typing import Any, TypeVar
from typing_extensions import Final

_T = TypeVar('_T')

PY_37: Final[bool]
SYSTEM: Final[str]

def get_pg_home_directory() -> Path | None: ...
def current_asyncio_task(
    loop: AbstractEventLoop | None,
) -> Task[Any] | None: ...
async def wait_closed(stream: StreamWriter) -> None: ...
async def wait_for(
    fut: Future[_T] | Awaitable[_T],
    timeout: float | None,
) -> _T: ...
