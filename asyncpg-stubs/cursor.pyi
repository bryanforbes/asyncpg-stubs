import typing

from . import connection as _connection, connresource
from .protocol import protocol as _cprotocol

_Cursor = typing.TypeVar('_Cursor', bound='Cursor[typing.Any]')
_CursorIterator = typing.TypeVar('_CursorIterator', bound='CursorIterator[typing.Any]')
_Record = typing.TypeVar('_Record', bound='_cprotocol.Record')

class CursorFactory(connresource.ConnectionResource, typing.Generic[_Record]):
    __slots__: typing.Any
    _state: typing.Optional['_cprotocol.PreparedStatementState[_Record]']
    _args: typing.Sequence[typing.Any]
    _prefetch: typing.Optional[int]
    _query: str
    _timeout: typing.Optional[float]
    _record_class: typing.Optional[typing.Type[_Record]]
    @typing.overload
    def __init__(
        self,
        connection: _connection.Connection[_Record],
        query: str,
        state: typing.Optional['_cprotocol.PreparedStatementState[_Record]'],
        args: typing.Sequence[typing.Any],
        prefetch: typing.Optional[int],
        timeout: typing.Optional[float],
        record_class: None,
    ) -> None: ...
    @typing.overload
    def __init__(
        self,
        connection: _connection.Connection[typing.Any],
        query: str,
        state: typing.Optional['_cprotocol.PreparedStatementState[_Record]'],
        args: typing.Sequence[typing.Any],
        prefetch: typing.Optional[int],
        timeout: typing.Optional[float],
        record_class: typing.Type[_Record],
    ) -> None: ...
    def __aiter__(self) -> CursorIterator[_Record]: ...
    def __await__(self) -> typing.Generator[typing.Any, None, 'Cursor[_Record]']: ...
    def __del__(self) -> None: ...

class BaseCursor(connresource.ConnectionResource, typing.Generic[_Record]):
    __slots__: typing.Any
    _state: typing.Optional['_cprotocol.PreparedStatementState[_Record]']
    _args: typing.Sequence[typing.Any]
    _portal_name: typing.Optional[str]
    _exhausted: bool
    _query: str
    _record_class: typing.Optional[typing.Type[_Record]]
    @typing.overload
    def __init__(
        self,
        connection: _connection.Connection[_Record],
        query: str,
        state: typing.Optional['_cprotocol.PreparedStatementState[_Record]'],
        args: typing.Sequence[typing.Any],
        record_class: None,
    ) -> None: ...
    @typing.overload
    def __init__(
        self,
        connection: _connection.Connection[typing.Any],
        query: str,
        state: typing.Optional['_cprotocol.PreparedStatementState[_Record]'],
        args: typing.Sequence[typing.Any],
        record_class: typing.Type[_Record],
    ) -> None: ...
    def _check_ready(self) -> None: ...
    async def _bind_exec(
        self, n: int, timeout: typing.Optional[float]
    ) -> typing.Any: ...
    async def _bind(self, timeout: typing.Optional[float]) -> typing.Any: ...
    async def _exec(self, n: int, timeout: typing.Optional[float]) -> typing.Any: ...
    def __repr__(self) -> str: ...
    def __del__(self) -> None: ...

class CursorIterator(BaseCursor[_Record]):
    __slots__: typing.Any
    _buffer: typing.Deque[_Record]
    _prefetch: int
    _timeout: typing.Optional[float]
    @typing.overload
    def __init__(
        self,
        connection: _connection.Connection[_Record],
        query: str,
        state: typing.Optional['_cprotocol.PreparedStatementState[_Record]'],
        args: typing.Sequence[typing.Any],
        record_class: None,
        prefetch: int,
        timeout: typing.Optional[float],
    ) -> None: ...
    @typing.overload
    def __init__(
        self,
        connection: _connection.Connection[typing.Any],
        query: str,
        state: typing.Optional['_cprotocol.PreparedStatementState[_Record]'],
        args: typing.Sequence[typing.Any],
        record_class: typing.Type[_Record],
        prefetch: int,
        timeout: typing.Optional[float],
    ) -> None: ...
    def __aiter__(self: _CursorIterator) -> _CursorIterator: ...
    _state: typing.Any
    async def __anext__(self) -> _Record: ...

class Cursor(BaseCursor[_Record]):
    __slots__: typing.Any
    _state: typing.Any
    async def _init(self: _Cursor, timeout: typing.Optional[float]) -> _Cursor: ...
    _exhausted: bool
    async def fetch(
        self, n: int, *, timeout: typing.Optional[float] = ...
    ) -> typing.List[_Record]: ...
    async def fetchrow(
        self, *, timeout: typing.Optional[float] = ...
    ) -> typing.Optional[_Record]: ...
    async def forward(
        self, n: int, *, timeout: typing.Optional[float] = ...
    ) -> int: ...
