from typing import (
    Any,
    AsyncIterable,
    AsyncIterator,
    Awaitable,
    Generator,
    Generic,
    List,
    Optional,
    Sequence,
    TypeVar,
)

from . import connresource
from .connection import Connection
from .protocol import Record
from .protocol.protocol import PreparedStatementState

_Cursor = TypeVar('_Cursor', bound=Cursor[Any])
_CursorIterator = TypeVar('_CursorIterator', bound=CursorIterator[Any])
_Record = TypeVar('_Record', bound=Record)

class CursorFactory(connresource.ConnectionResource, Generic[_Record]):
    def __init__(
        self,
        connection: Connection,
        query: str,
        state: Optional[PreparedStatementState],
        args: Sequence[Any],
        prefetch: Optional[int],
        timeout: Optional[float],
    ) -> None: ...
    def __aiter__(self) -> CursorIterator[_Record]: ...
    def __await__(self) -> Generator[Any, None, Cursor[_Record]]: ...
    def __del__(self) -> None: ...

class BaseCursor(connresource.ConnectionResource, Generic[_Record]):
    def __init__(
        self,
        connection: Connection,
        query: str,
        state: Optional[PreparedStatementState],
        args: Sequence[Any],
    ) -> None: ...
    def __del__(self) -> None: ...

class CursorIterator(BaseCursor[_Record]):
    def __init__(
        self,
        connection: Connection,
        query: str,
        state: Optional[PreparedStatementState],
        args: Sequence[Any],
        prefetch: int,
        timeout: Optional[float],
    ) -> None: ...
    def __aiter__(self: _CursorIterator) -> _CursorIterator: ...
    async def __anext__(self) -> _Record: ...

class Cursor(BaseCursor[_Record]):
    async def fetch(
        self, n: int, *, timeout: Optional[float] = ...
    ) -> List[_Record]: ...
    async def fetchrow(
        self, *, timeout: Optional[float] = ...
    ) -> Optional[_Record]: ...
    async def forward(self, n: int, *, timeout: Optional[float] = ...) -> int: ...
