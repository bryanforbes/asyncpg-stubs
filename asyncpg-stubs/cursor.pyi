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
    Type,
    TypeVar,
    overload,
)

from . import connresource
from .connection import Connection
from .protocol import Record
from .protocol.protocol import PreparedStatementState

_Cursor = TypeVar('_Cursor', bound=Cursor[Any])
_CursorIterator = TypeVar('_CursorIterator', bound=CursorIterator[Any])
_Record = TypeVar('_Record', bound=Record)

class CursorFactory(connresource.ConnectionResource, Generic[_Record]):
    @overload
    def __init__(
        self,
        connection: Connection[_Record],
        query: str,
        state: Optional[PreparedStatementState[_Record]],
        args: Sequence[Any],
        prefetch: Optional[int],
        timeout: Optional[float],
        record_class: None,
    ) -> None: ...
    @overload
    def __init__(
        self,
        connection: Connection[Any],
        query: str,
        state: Optional[PreparedStatementState[_Record]],
        args: Sequence[Any],
        prefetch: Optional[int],
        timeout: Optional[float],
        record_class: Type[_Record],
    ) -> None: ...
    @overload
    def __init__(
        self,
        connection: Connection[Any],
        query: str,
        state: Optional[PreparedStatementState[_Record]],
        args: Sequence[Any],
        prefetch: Optional[int],
        timeout: Optional[float],
        record_class: Optional[Type[_Record]],
    ) -> None: ...
    def __aiter__(self) -> CursorIterator[_Record]: ...
    def __await__(self) -> Generator[Any, None, Cursor[_Record]]: ...
    def __del__(self) -> None: ...

class BaseCursor(connresource.ConnectionResource, Generic[_Record]):
    @overload
    def __init__(
        self,
        connection: Connection[_Record],
        query: str,
        state: Optional[PreparedStatementState[_Record]],
        args: Sequence[Any],
        record_class: None,
    ) -> None: ...
    @overload
    def __init__(
        self,
        connection: Connection[Any],
        query: str,
        state: Optional[PreparedStatementState[_Record]],
        args: Sequence[Any],
        record_class: Type[_Record],
    ) -> None: ...
    @overload
    def __init__(
        self,
        connection: Connection[Any],
        query: str,
        state: Optional[PreparedStatementState[_Record]],
        args: Sequence[Any],
        record_class: Optional[Type[_Record]],
    ) -> None: ...
    def __del__(self) -> None: ...

class CursorIterator(BaseCursor[_Record]):
    @overload
    def __init__(
        self,
        connection: Connection[_Record],
        query: str,
        state: Optional[PreparedStatementState[_Record]],
        args: Sequence[Any],
        record_class: None,
        prefetch: int,
        timeout: Optional[float],
    ) -> None: ...
    @overload
    def __init__(
        self,
        connection: Connection[Any],
        query: str,
        state: Optional[PreparedStatementState[_Record]],
        args: Sequence[Any],
        record_class: Type[_Record],
        prefetch: int,
        timeout: Optional[float],
    ) -> None: ...
    @overload
    def __init__(
        self,
        connection: Connection[Any],
        query: str,
        state: Optional[PreparedStatementState[_Record]],
        args: Sequence[Any],
        record_class: Optional[Type[_Record]],
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
