import sys
from collections.abc import Awaitable
from typing import TypeVar

if sys.version_info >= (3, 11):
    from asyncio import timeout as timeout_ctx
else:
    from async_timeout import timeout as timeout_ctx

_T = TypeVar('_T')

async def wait_for(fut: Awaitable[_T], timeout: float | None) -> _T: ...
