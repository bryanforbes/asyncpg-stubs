from collections.abc import Coroutine, Iterable
from typing import Any, Generic, Protocol, TypeVar

from . import connection as _connection, connresource, cursor, types
from .protocol import protocol as _cprotocol

_Record = TypeVar('_Record', bound=_cprotocol.Record)
_T_co = TypeVar('_T_co', covariant=True)

class _Executor(Protocol[_T_co]):
    def __call__(
        self,
        protocol: _cprotocol.BaseProtocol[Any],
        /,
    ) -> Coroutine[Any, Any, _T_co]: ...

class PreparedStatement(connresource.ConnectionResource, Generic[_Record]):
    __slots__: Any
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
        *args: Any,
        prefetch: int | None = ...,
        timeout: float | None = ...,
    ) -> cursor.CursorFactory[_Record]: ...
    async def explain(self, *args: Any, analyze: bool = ...) -> Any: ...
    async def fetch(self, *args: Any, timeout: float | None = ...) -> list[_Record]: ...
    async def fetchval(
        self,
        *args: Any,
        column: int = ...,
        timeout: float | None = ...,
    ) -> Any: ...
    async def fetchrow(
        self, *args: Any, timeout: float | None = ...
    ) -> _Record | None: ...
    async def executemany(
        self,
        args: Iterable[Any],
        *,
        timeout: float | None = ...,
    ) -> None: ...
    def __del__(self) -> None: ...
