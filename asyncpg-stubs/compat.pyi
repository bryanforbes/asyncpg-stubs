import asyncio
import pathlib
import typing

_T = typing.TypeVar('_T')

def get_pg_home_directory() -> typing.Optional[pathlib.Path]: ...
def current_asyncio_task(
    loop: typing.Optional[asyncio.AbstractEventLoop],
) -> typing.Optional['asyncio.Task[typing.Any]']: ...
async def wait_closed(stream: asyncio.StreamWriter) -> None: ...
async def wait_for(
    fut: typing.Union['asyncio.Future[_T]', typing.Awaitable[_T]],
    timeout: typing.Optional[float],
) -> _T: ...
