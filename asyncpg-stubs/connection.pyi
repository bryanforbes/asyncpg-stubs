from asyncio import AbstractEventLoop
from collections.abc import (
    AsyncIterable,
    Awaitable,
    Callable,
    Coroutine,
    Generator,
    Iterable,
    Sequence,
)
from os import PathLike
from typing import Any, BinaryIO, Generic, NamedTuple, Protocol, TypeVar, overload
from typing_extensions import Literal, TypeAlias

from . import (
    connect_utils,
    cursor,
    exceptions,
    pool,
    prepared_stmt,
    protocol,
    transaction,
    types,
)
from .protocol import protocol as _cprotocol

_Connection = TypeVar('_Connection', bound=Connection[Any])
_Writer: TypeAlias = Callable[[bytes], Coroutine[Any, Any, None]]
_Record = TypeVar('_Record', bound=protocol.Record)
_OtherRecord = TypeVar('_OtherRecord', bound=protocol.Record)
_RecordsType: TypeAlias = list[_Record]
_RecordsExtraType: TypeAlias = tuple[_RecordsType[_Record], bytes, bool]

_OutputType: TypeAlias = PathLike[Any] | BinaryIO | _Writer
_SourceType: TypeAlias = PathLike[Any] | BinaryIO | AsyncIterable[bytes]

_CopyFormat: TypeAlias = Literal['text', 'csv', 'binary']

class _Listener(Protocol):
    def __call__(
        self,
        con_ref: Connection[Any] | pool.PoolConnectionProxy[Any],
        pid: int,
        channel: str,
        payload: Any,
        /,
    ) -> Awaitable[None] | Generator[Any, None, None] | None: ...

class _LogListener(Protocol):
    def __call__(
        self,
        con_ref: Connection[Any] | pool.PoolConnectionProxy[Any],
        message: exceptions.PostgresLogMessage,
        /,
    ) -> Awaitable[None] | Generator[Any, None, None] | None: ...

class _TerminationListener(Protocol):
    def __call__(
        self,
        con_ref: Connection[Any] | pool.PoolConnectionProxy[Any],
        /,
    ) -> Awaitable[None] | Generator[Any, None, None] | None: ...

class _OnRemove(Protocol[_Record]):
    def __call__(
        self,
        statement: _cprotocol.PreparedStatementState[_Record],
        /,
    ) -> None: ...

class _Executor(Protocol[_Record]):
    def __call__(
        self,
        statement: _cprotocol.PreparedStatementState[_Record],
        timeout: float | None,
        /,
    ) -> Any: ...

class ConnectionMeta(type):
    def __instancecheck__(cls, instance: Any) -> bool: ...

class Connection(Generic[_Record], metaclass=ConnectionMeta):
    def __init__(
        self,
        protocol: _cprotocol.BaseProtocol[_Record],
        transport: Any,
        loop: AbstractEventLoop,
        addr: tuple[str, int] | str,
        config: connect_utils._ClientConfiguration,
        params: connect_utils._ConnectionParameters,
    ) -> None: ...
    def __del__(self) -> None: ...
    async def add_listener(self, channel: str, callback: _Listener) -> None: ...
    async def remove_listener(self, channel: str, callback: _Listener) -> None: ...
    def add_log_listener(self, callback: _LogListener) -> None: ...
    def remove_log_listener(self, callback: _LogListener) -> None: ...
    def add_termination_listener(self, callback: _TerminationListener) -> None: ...
    def remove_termination_listener(self, callback: _TerminationListener) -> None: ...
    def get_server_pid(self) -> int: ...
    def get_server_version(self) -> types.ServerVersion: ...
    def get_settings(self) -> _cprotocol.ConnectionSettings: ...
    def transaction(
        self,
        *,
        isolation: transaction._IsolationLevels | None = ...,
        readonly: bool = ...,
        deferrable: bool = ...,
    ) -> transaction.Transaction: ...
    def is_in_transaction(self) -> bool: ...
    async def execute(
        self, query: str, *args: Any, timeout: float | None = ...
    ) -> str: ...
    async def executemany(
        self,
        command: str,
        args: Iterable[Sequence[Any]],
        *,
        timeout: float | None = ...,
    ) -> None: ...
    @overload
    def cursor(
        self,
        query: str,
        *args: Any,
        prefetch: int | None = ...,
        timeout: float | None = ...,
        record_class: None = ...,
    ) -> cursor.CursorFactory[_Record]: ...
    @overload
    def cursor(
        self,
        query: str,
        *args: Any,
        prefetch: int | None = ...,
        timeout: float | None = ...,
        record_class: type[_OtherRecord],
    ) -> cursor.CursorFactory[_OtherRecord]: ...
    @overload
    def cursor(
        self,
        query: str,
        *args: Any,
        prefetch: int | None = ...,
        timeout: float | None = ...,
        record_class: type[_OtherRecord] | None,
    ) -> cursor.CursorFactory[_Record] | cursor.CursorFactory[_OtherRecord]: ...
    @overload
    async def prepare(
        self,
        query: str,
        *,
        name: str | None = ...,
        timeout: float | None = ...,
        record_class: None = ...,
    ) -> prepared_stmt.PreparedStatement[_Record]: ...
    @overload
    async def prepare(
        self,
        query: str,
        *,
        name: str | None = ...,
        timeout: float | None = ...,
        record_class: type[_OtherRecord],
    ) -> prepared_stmt.PreparedStatement[_OtherRecord]: ...
    @overload
    async def prepare(
        self,
        query: str,
        *,
        name: str | None = ...,
        timeout: float | None = ...,
        record_class: type[_OtherRecord] | None,
    ) -> prepared_stmt.PreparedStatement[_Record] | prepared_stmt.PreparedStatement[
        _OtherRecord
    ]: ...
    @overload
    async def fetch(
        self,
        query: str,
        *args: Any,
        timeout: float | None = ...,
        record_class: None = ...,
    ) -> list[_Record]: ...
    @overload
    async def fetch(
        self,
        query: str,
        *args: Any,
        timeout: float | None = ...,
        record_class: type[_OtherRecord],
    ) -> list[_OtherRecord]: ...
    @overload
    async def fetch(
        self,
        query: str,
        *args: Any,
        timeout: float | None = ...,
        record_class: type[_OtherRecord] | None,
    ) -> list[_Record] | list[_OtherRecord]: ...
    async def fetchval(
        self,
        query: str,
        *args: Any,
        column: int = ...,
        timeout: float | None = ...,
    ) -> Any: ...
    @overload
    async def fetchrow(
        self,
        query: str,
        *args: Any,
        timeout: float | None = ...,
        record_class: None = ...,
    ) -> _Record | None: ...
    @overload
    async def fetchrow(
        self,
        query: str,
        *args: Any,
        timeout: float | None = ...,
        record_class: type[_OtherRecord],
    ) -> _OtherRecord | None: ...
    @overload
    async def fetchrow(
        self,
        query: str,
        *args: Any,
        timeout: float | None = ...,
        record_class: type[_OtherRecord] | None,
    ) -> _Record | _OtherRecord | None: ...
    async def copy_from_table(
        self,
        table_name: str,
        *,
        output: _OutputType,
        columns: Iterable[str] | None = ...,
        schema_name: str | None = ...,
        timeout: float | None = ...,
        format: _CopyFormat | None = ...,
        oids: int | None = ...,
        delimiter: str | None = ...,
        null: str | None = ...,
        header: bool | None = ...,
        quote: str | None = ...,
        escape: str | None = ...,
        force_quote: bool | Iterable[str] | None = ...,
        encoding: str | None = ...,
    ) -> str: ...
    async def copy_from_query(
        self,
        query: str,
        *args: Any,
        output: _OutputType,
        timeout: float | None = ...,
        format: _CopyFormat | None = ...,
        oids: int | None = ...,
        delimiter: str | None = ...,
        null: str | None = ...,
        header: bool | None = ...,
        quote: str | None = ...,
        escape: str | None = ...,
        force_quote: bool | Iterable[str] | None = ...,
        encoding: str | None = ...,
    ) -> str: ...
    async def copy_to_table(
        self,
        table_name: str,
        *,
        source: _SourceType,
        columns: Iterable[str] | None = ...,
        schema_name: str | None = ...,
        timeout: float | None = ...,
        format: _CopyFormat | None = ...,
        oids: int | None = ...,
        freeze: bool | None = ...,
        delimiter: str | None = ...,
        null: str | None = ...,
        header: bool | None = ...,
        quote: str | None = ...,
        escape: str | None = ...,
        force_quote: bool | Iterable[str] | None = ...,
        force_not_null: bool | Iterable[str] | None = ...,
        force_null: bool | Iterable[str] | None = ...,
        encoding: str | None = ...,
    ) -> str: ...
    async def copy_records_to_table(
        self,
        table_name: str,
        *,
        records: Iterable[Sequence[Any]] | AsyncIterable[Sequence[Any]],
        columns: Iterable[str] | None = ...,
        schema_name: str | None = ...,
        timeout: float | None = ...,
    ) -> str: ...
    async def set_type_codec(
        self,
        typename: str,
        *,
        schema: str = ...,
        encoder: Callable[[Any], Any],
        decoder: Callable[[Any], Any],
        format: str = ...,
    ) -> None: ...
    async def reset_type_codec(self, typename: str, *, schema: str = ...) -> None: ...
    async def set_builtin_type_codec(
        self,
        typename: str,
        *,
        schema: str = ...,
        codec_name: str,
        format: str | None = ...,
    ) -> None: ...
    def is_closed(self) -> bool: ...
    async def close(self, *, timeout: float | None = ...) -> None: ...
    def terminate(self) -> None: ...
    async def reset(self, *, timeout: float | None = ...) -> None: ...
    async def reload_schema_state(self) -> None: ...

@overload
async def connect(
    dsn: str | None = ...,
    *,
    host: connect_utils._HostType | None = ...,
    port: connect_utils._PortType | None = ...,
    user: str | None = ...,
    password: connect_utils._PasswordType | None = ...,
    passfile: str | None = ...,
    database: str | None = ...,
    loop: AbstractEventLoop | None = ...,
    timeout: float = ...,
    statement_cache_size: int = ...,
    max_cached_statement_lifetime: int = ...,
    max_cacheable_statement_size: int = ...,
    command_timeout: float | None = ...,
    ssl: connect_utils._SSLType | None = ...,
    direct_tls: bool = ...,
    record_class: type[_Record],
    server_settings: dict[str, str] | None = ...,
) -> Connection[_Record]: ...
@overload
async def connect(
    dsn: str | None = ...,
    *,
    host: connect_utils._HostType | None = ...,
    port: connect_utils._PortType | None = ...,
    user: str | None = ...,
    password: connect_utils._PasswordType | None = ...,
    passfile: str | None = ...,
    database: str | None = ...,
    loop: AbstractEventLoop | None = ...,
    timeout: float = ...,
    statement_cache_size: int = ...,
    max_cached_statement_lifetime: int = ...,
    max_cacheable_statement_size: int = ...,
    command_timeout: float | None = ...,
    ssl: connect_utils._SSLType | None = ...,
    direct_tls: bool = ...,
    connection_class: type[_Connection],
    record_class: type[_Record] = ...,
    server_settings: dict[str, str] | None = ...,
) -> _Connection: ...
@overload
async def connect(
    dsn: str | None = ...,
    *,
    host: connect_utils._HostType | None = ...,
    port: connect_utils._PortType | None = ...,
    user: str | None = ...,
    password: connect_utils._PasswordType | None = ...,
    passfile: str | None = ...,
    database: str | None = ...,
    loop: AbstractEventLoop | None = ...,
    timeout: float = ...,
    statement_cache_size: int = ...,
    max_cached_statement_lifetime: int = ...,
    max_cacheable_statement_size: int = ...,
    command_timeout: float | None = ...,
    ssl: connect_utils._SSLType | None = ...,
    direct_tls: bool = ...,
    server_settings: dict[str, str] | None = ...,
) -> Connection[protocol.Record]: ...

class _ConnectionProxy(Generic[_Record]):
    __slots__: Any

class ServerCapabilities(NamedTuple):
    advisory_locks: bool
    notifications: bool
    plpgsql: bool
    sql_reset: bool
    sql_close_all: bool
