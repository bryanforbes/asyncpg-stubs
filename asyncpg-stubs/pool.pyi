from _typeshed import Self
from asyncio import AbstractEventLoop
from collections.abc import AsyncIterable, Callable, Generator, Iterable, Sequence
from typing import Any, Generic, Protocol, TypeVar, overload

from . import (
    connect_utils,
    connection,
    cursor,
    prepared_stmt,
    protocol,
    transaction,
    types,
)
from .protocol import protocol as _cprotocol

_Connection = TypeVar('_Connection', bound=connection.Connection[Any])
_Record = TypeVar('_Record', bound=protocol.Record)
_OtherRecord = TypeVar("_OtherRecord", bound=protocol.Record)

class _SetupCallback(Protocol[_Record]):
    async def __call__(self, proxy: PoolConnectionProxy[_Record], /) -> None: ...

class _InitCallback(Protocol[_Record]):
    async def __call__(self, con: connection.Connection[_Record], /) -> None: ...

class PoolConnectionProxyMeta(type): ...

class PoolConnectionProxy(
    connection._ConnectionProxy[_Record], metaclass=PoolConnectionProxyMeta
):
    _holder: PoolConnectionHolder[_Record]
    def __init__(
        self,
        holder: PoolConnectionHolder[_Record],
        con: connection.Connection[_Record],
    ) -> None: ...
    async def add_listener(
        self, channel: str, callback: connection._Listener
    ) -> None: ...
    async def remove_listener(
        self, channel: str, callback: connection._Listener
    ) -> None: ...
    def add_log_listener(self, callback: connection._LogListener) -> None: ...
    def remove_log_listener(self, callback: connection._LogListener) -> None: ...
    def add_termination_listener(
        self, callback: connection._TerminationListener
    ) -> None: ...
    def remove_termination_listener(
        self, callback: connection._TerminationListener
    ) -> None: ...
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
        output: connection._OutputType,
        columns: Iterable[str] | None = ...,
        schema_name: str | None = ...,
        timeout: float | None = ...,
        format: connection._CopyFormat | None = ...,
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
        output: connection._OutputType,
        timeout: float | None = ...,
        format: connection._CopyFormat | None = ...,
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
        source: connection._SourceType,
        columns: Iterable[str] | None = ...,
        schema_name: str | None = ...,
        timeout: float | None = ...,
        format: connection._CopyFormat | None = ...,
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

class PoolConnectionHolder(Generic[_Record]):
    __slots__: Any
    _pool: Pool[_Record]
    def __init__(
        self,
        pool: Pool[_Record],
        *,
        max_queries: int,
        setup: _SetupCallback[_Record] | None,
        max_inactive_time: float,
    ) -> None: ...
    def is_connected(self) -> bool: ...
    def is_idle(self) -> bool: ...
    async def connect(self) -> None: ...
    async def acquire(self) -> PoolConnectionProxy[_Record]: ...
    async def release(self, timeout: float | None) -> None: ...
    async def wait_until_released(self) -> None: ...
    async def close(self) -> None: ...
    def terminate(self) -> None: ...

class Pool(Generic[_Record]):
    __slots__: Any
    def __init__(
        self,
        *connect_args: Any,
        min_size: int,
        max_size: int,
        max_queries: int,
        max_inactive_connection_lifetime: float,
        setup: _SetupCallback[_Record] | None,
        init: _InitCallback[_Record] | None,
        loop: AbstractEventLoop | None,
        connection_class: type[_Connection],
        record_class: type[_Record],
        **connect_kwargs: Any,
    ) -> None: ...
    def get_size(self) -> int: ...
    def get_min_size(self) -> int: ...
    def get_max_size(self) -> int: ...
    def get_idle_size(self) -> int: ...
    def set_connect_args(
        self,
        dsn: str | None = ...,
        *,
        host: connect_utils._HostType | None = ...,
        port: connect_utils._PortType | None = ...,
        user: str | None = ...,
        password: connect_utils._PasswordType | None = ...,
        passfile: str | None = ...,
        database: str | None = ...,
        timeout: float = ...,
        statement_cache_size: int = ...,
        max_cached_statement_lifetime: int = ...,
        max_cacheable_statement_size: int = ...,
        command_timeout: float | None = ...,
        ssl: connect_utils._SSLType | None = ...,
        server_settings: dict[str, str] | None = ...,
    ) -> None: ...
    async def execute(
        self, query: str, *args: Any, timeout: float | None = ...
    ) -> str: ...
    async def executemany(
        self, command: str, args: Any, *, timeout: float | None = ...
    ) -> None: ...
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
        output: connection._OutputType,
        columns: Iterable[str] | None = ...,
        schema_name: str | None = ...,
        timeout: float | None = ...,
        format: connection._CopyFormat | None = ...,
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
        output: connection._OutputType,
        timeout: float | None = ...,
        format: connection._CopyFormat | None = ...,
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
        source: connection._SourceType,
        columns: Iterable[str] | None = ...,
        schema_name: str | None = ...,
        timeout: float | None = ...,
        format: connection._CopyFormat | None = ...,
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
    def acquire(
        self, *, timeout: float | None = ...
    ) -> PoolAcquireContext[_Record]: ...
    async def release(
        self,
        connection: PoolConnectionProxy[_Record],
        *,
        timeout: float | None = ...,
    ) -> None: ...
    async def close(self) -> None: ...
    def terminate(self) -> None: ...
    async def expire_connections(self) -> None: ...
    def __await__(self: Self) -> Generator[Any, None, Self | None]: ...
    async def __aenter__(self: Self) -> Self: ...
    async def __aexit__(self, *exc: object) -> None: ...

class PoolAcquireContext(Generic[_Record]):
    __slots__: Any
    timeout: float | None
    connection: PoolConnectionProxy[_Record] | None
    done: bool
    pool: Pool[_Record]
    def __init__(self, pool: Pool[_Record], timeout: float | None) -> None: ...
    async def __aenter__(
        self,
    ) -> PoolConnectionProxy[_Record]: ...
    async def __aexit__(self, *exc: object) -> None: ...
    def __await__(
        self,
    ) -> Generator[Any, None, PoolConnectionProxy[_Record]]: ...

@overload
def create_pool(
    dsn: str | None = ...,
    *,
    min_size: int = ...,
    max_size: int = ...,
    max_queries: int = ...,
    max_inactive_connection_lifetime: float = ...,
    setup: _SetupCallback[protocol.Record] | None = ...,
    init: _InitCallback[protocol.Record] | None = ...,
    loop: AbstractEventLoop | None = ...,
    connection_class: type[connection.Connection[protocol.Record]] = ...,
    record_class: type[protocol.Record] = ...,
    host: connect_utils._HostType | None = ...,
    port: connect_utils._PortType | None = ...,
    user: str | None = ...,
    password: connect_utils._PasswordType | None = ...,
    passfile: str | None = ...,
    database: str | None = ...,
    timeout: float = ...,
    statement_cache_size: int = ...,
    max_cached_statement_lifetime: int = ...,
    max_cacheable_statement_size: int = ...,
    command_timeout: float | None = ...,
    ssl: connect_utils._SSLType | None = ...,
    server_settings: dict[str, str] | None = ...,
) -> Pool[protocol.Record]: ...
@overload
def create_pool(
    dsn: str | None = ...,
    *,
    min_size: int = ...,
    max_size: int = ...,
    max_queries: int = ...,
    max_inactive_connection_lifetime: float = ...,
    setup: _SetupCallback[_Record] | None = ...,
    init: _InitCallback[_Record] | None = ...,
    loop: AbstractEventLoop | None = ...,
    connection_class: type[_Connection] = ...,
    record_class: type[_Record],
    host: connect_utils._HostType | None = ...,
    port: connect_utils._PortType | None = ...,
    user: str | None = ...,
    password: connect_utils._PasswordType | None = ...,
    passfile: str | None = ...,
    database: str | None = ...,
    timeout: float = ...,
    statement_cache_size: int = ...,
    max_cached_statement_lifetime: int = ...,
    max_cacheable_statement_size: int = ...,
    command_timeout: float | None = ...,
    ssl: connect_utils._SSLType | None = ...,
    server_settings: dict[str, str] | None = ...,
) -> Pool[_Record]: ...
