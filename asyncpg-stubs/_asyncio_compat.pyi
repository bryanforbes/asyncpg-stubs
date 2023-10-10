import sys
from asyncio import Future
from collections.abc import Awaitable, Generator
from typing import Any, TypeVar
from typing_extensions import TypeAlias

if sys.version_info < (3, 11):
    from async_timeout import timeout as timeout_ctx
else:
    from asyncio import timeout as timeout_ctx

_T = TypeVar('_T')
_FutureLike: TypeAlias = Future[_T] | Generator[Any, None, _T] | Awaitable[_T]

async def wait_for(
    fut: _FutureLike[_T],
    timeout: float | None,
) -> _T: ...
