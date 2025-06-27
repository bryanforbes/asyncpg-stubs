from collections.abc import Generator, Sequence
from typing import Any, Generic, overload
from typing_extensions import Self, TypeVar

from . import connection as _connection, connresource
from .protocol import protocol as _cprotocol

_Record = TypeVar('_Record', bound=_cprotocol.Record, default=_cprotocol.Record)

class CursorFactory(connresource.ConnectionResource, Generic[_Record]):
    __slots__ = (
        '_state',
        '_args',
        '_prefetch',
        '_query',
        '_timeout',
        '_record_class',
    )
    @overload
    def __init__(
        self,
        connection: _connection.Connection[_Record],
        query: str,
        state: _cprotocol.PreparedStatementState[_Record] | None,
        args: Sequence[object],
        prefetch: int | None,
        timeout: float | None,
        record_class: None,
    ) -> None: ...
    @overload
    def __init__(
        self,
        connection: _connection.Connection[Any],
        query: str,
        state: _cprotocol.PreparedStatementState[_Record] | None,
        args: Sequence[object],
        prefetch: int | None,
        timeout: float | None,
        record_class: type[_Record],
    ) -> None: ...
    def __aiter__(self) -> CursorIterator[_Record]: ...
    def __await__(self) -> Generator[Any, None, Cursor[_Record]]: ...
    def __del__(self) -> None: ...

class BaseCursor(connresource.ConnectionResource, Generic[_Record]):
    __slots__ = (
        '_state',
        '_args',
        '_portal_name',
        '_exhausted',
        '_query',
        '_record_class',
    )
    @overload
    def __init__(
        self,
        connection: _connection.Connection[_Record],
        query: str,
        state: _cprotocol.PreparedStatementState[_Record] | None,
        args: Sequence[object],
        record_class: None,
    ) -> None: ...
    @overload
    def __init__(
        self,
        connection: _connection.Connection[Any],
        query: str,
        state: _cprotocol.PreparedStatementState[_Record] | None,
        args: Sequence[object],
        record_class: type[_Record],
    ) -> None: ...
    def __del__(self) -> None: ...

class CursorIterator(BaseCursor[_Record]):
    __slots__ = ('_buffer', '_prefetch', '_timeout')
    @overload
    def __init__(
        self,
        connection: _connection.Connection[_Record],
        query: str,
        state: _cprotocol.PreparedStatementState[_Record] | None,
        args: Sequence[object],
        record_class: None,
        prefetch: int,
        timeout: float | None,
    ) -> None: ...
    @overload
    def __init__(
        self,
        connection: _connection.Connection[Any],
        query: str,
        state: _cprotocol.PreparedStatementState[_Record] | None,
        args: Sequence[object],
        record_class: type[_Record],
        prefetch: int,
        timeout: float | None,
    ) -> None: ...
    def __aiter__(self) -> Self: ...
    async def __anext__(self) -> _Record: ...

class Cursor(BaseCursor[_Record]):
    __slots__ = ()
    async def fetch(self, n: int, *, timeout: float | None = ...) -> list[_Record]: ...
    async def fetchrow(self, *, timeout: float | None = ...) -> _Record | None: ...
    async def forward(self, n: int, *, timeout: float | None = ...) -> int: ...
