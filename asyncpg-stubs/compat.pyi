import sys
from asyncio import StreamWriter
from pathlib import Path
from typing import Final

SYSTEM: Final[str]

def get_pg_home_directory() -> Path | None: ...
async def wait_closed(stream: StreamWriter) -> None: ...

if sys.version_info < (3, 12):
    from ._asyncio_compat import wait_for as wait_for
else:
    from asyncio import wait_for as wait_for

if sys.version_info < (3, 11):
    from async_timeout import timeout as timeout_ctx
else:
    from asyncio import timeout as timeout_ctx
