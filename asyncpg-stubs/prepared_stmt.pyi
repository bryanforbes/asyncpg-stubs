from collections.abc import Coroutine, Iterable
from typing import Any, Generic, Protocol, TypeVar

from . import connection as _connection, connresource, cursor, types
from .protocol import protocol as _cprotocol

_Record = TypeVar('_Record', bound=_cprotocol.Record)
_T_co = TypeVar('_T_co', covariant=True)

class _Executor(Protocol[_T_co]):
    def __call__(
        self,
        __protocol: _cprotocol.BaseProtocol[Any],
    ) -> Coroutine[Any, Any, _T_co]: ...

class PreparedStatement(connresource.ConnectionResource, Generic[_Record]):
    __slots__ = ('_state', '_query', '_last_status')
    def __init__(
        self,
        connection: _connection.Connection[Any],
        query: str,
        state: _cprotocol.PreparedStatementState[_Record],
    ) -> None: ...
    def get_name(self) -> str: ...
    def get_query(self) -> str: ...
    def get_statusmsg(self) -> str | None: ...
    def get_parameters(self) -> tuple[types.Type, ...]: ...
    def get_attributes(self) -> tuple[types.Attribute, ...]: ...
    def cursor(
        self,
        *args: object,
        prefetch: int | None = ...,
        timeout: float | None = ...,
    ) -> cursor.CursorFactory[_Record]: ...
    async def explain(self, *args: object, analyze: bool = ...) -> Any: ...
    async def fetch(
        self, *args: object, timeout: float | None = ...
    ) -> list[_Record]: ...
    async def fetchval(
        self,
        *args: object,
        column: int = ...,
        timeout: float | None = ...,
    ) -> Any: ...
    async def fetchrow(
        self, *args: object, timeout: float | None = ...
    ) -> _Record | None: ...
    async def executemany(
        self,
        args: Iterable[object],
        *,
        timeout: float | None = ...,
    ) -> None: ...
    def __del__(self) -> None: ...
