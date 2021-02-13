import asyncio
import typing
import typing_extensions

from . import connect_utils, connection, cursor, prepared_stmt, transaction, types
from .protocol import protocol as _cprotocol

_Connection = typing.TypeVar('_Connection', bound=connection.Connection[typing.Any])
_Pool = typing.TypeVar('_Pool', bound=Pool[typing.Any])
_Record = typing.TypeVar('_Record', bound=_cprotocol.Record)
_OtherRecord = typing.TypeVar('_OtherRecord', bound=_cprotocol.Record)

class _SetupCallback(typing_extensions.Protocol[_Record]):
    async def __call__(self, __proxy: PoolConnectionProxy[_Record]) -> None: ...

class _InitCallback(typing_extensions.Protocol[_Record]):
    async def __call__(self, __con: connection.Connection[_Record]) -> None: ...

class PoolConnectionProxyMeta(type): ...

class PoolConnectionProxy(
    connection._ConnectionProxy[_Record], metaclass=PoolConnectionProxyMeta, wrap=True
):
    _holder: PoolConnectionHolder[_Record]
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
        isolation: typing.Optional[transaction._IsolationLevels] = ...,
        readonly: bool = ...,
        deferrable: bool = ...,
    ) -> transaction.Transaction: ...
    def is_in_transaction(self) -> bool: ...
    async def execute(
        self, query: str, *args: typing.Any, timeout: typing.Optional[float] = ...
    ) -> str: ...
    async def executemany(
        self,
        command: str,
        args: typing.Iterable[typing.Sequence[typing.Any]],
        *,
        timeout: typing.Optional[float] = ...,
    ) -> None: ...
    @typing.overload
    def cursor(
        self,
        query: str,
        *args: typing.Any,
        prefetch: typing.Optional[int] = ...,
        timeout: typing.Optional[float] = ...,
        record_class: None = ...,
    ) -> cursor.CursorFactory[_Record]: ...
    @typing.overload
    def cursor(
        self,
        query: str,
        *args: typing.Any,
        prefetch: typing.Optional[int] = ...,
        timeout: typing.Optional[float] = ...,
        record_class: typing.Type[_OtherRecord],
    ) -> cursor.CursorFactory[_OtherRecord]: ...
    @typing.overload
    def cursor(
        self,
        query: str,
        *args: typing.Any,
        prefetch: typing.Optional[int] = ...,
        timeout: typing.Optional[float] = ...,
        record_class: typing.Optional[typing.Type[_OtherRecord]],
    ) -> typing.Union[
        cursor.CursorFactory[_Record],
        cursor.CursorFactory[_OtherRecord],
    ]: ...
    @typing.overload
    async def prepare(
        self,
        query: str,
        *,
        timeout: typing.Optional[float] = ...,
        record_class: None = ...,
    ) -> prepared_stmt.PreparedStatement[_Record]: ...
    @typing.overload
    async def prepare(
        self,
        query: str,
        *,
        timeout: typing.Optional[float] = ...,
        record_class: typing.Type[_OtherRecord],
    ) -> prepared_stmt.PreparedStatement[_OtherRecord]: ...
    @typing.overload
    async def prepare(
        self,
        query: str,
        *,
        timeout: typing.Optional[float] = ...,
        record_class: typing.Optional[typing.Type[_OtherRecord]],
    ) -> typing.Union[
        prepared_stmt.PreparedStatement[_Record],
        prepared_stmt.PreparedStatement[_OtherRecord],
    ]: ...
    @typing.overload
    async def fetch(
        self,
        query: str,
        *args: typing.Any,
        timeout: typing.Optional[float] = ...,
        record_class: None = ...,
    ) -> typing.List[_Record]: ...
    @typing.overload
    async def fetch(
        self,
        query: str,
        *args: typing.Any,
        timeout: typing.Optional[float] = ...,
        record_class: typing.Type[_OtherRecord],
    ) -> typing.List[_OtherRecord]: ...
    @typing.overload
    async def fetch(
        self,
        query: str,
        *args: typing.Any,
        timeout: typing.Optional[float] = ...,
        record_class: typing.Optional[typing.Type[_OtherRecord]],
    ) -> typing.Union[typing.List[_Record], typing.List[_OtherRecord]]: ...
    async def fetchval(
        self,
        query: str,
        *args: typing.Any,
        column: int = ...,
        timeout: typing.Optional[float] = ...,
    ) -> typing.Any: ...
    @typing.overload
    async def fetchrow(
        self,
        query: str,
        *args: typing.Any,
        timeout: typing.Optional[float] = ...,
        record_class: None = ...,
    ) -> typing.Optional[_Record]: ...
    @typing.overload
    async def fetchrow(
        self,
        query: str,
        *args: typing.Any,
        timeout: typing.Optional[float] = ...,
        record_class: typing.Type[_OtherRecord],
    ) -> typing.Optional[_OtherRecord]: ...
    @typing.overload
    async def fetchrow(
        self,
        query: str,
        *args: typing.Any,
        timeout: typing.Optional[float] = ...,
        record_class: typing.Optional[typing.Type[_OtherRecord]],
    ) -> typing.Union[typing.Optional[_Record], typing.Optional[_OtherRecord]]: ...
    async def copy_from_table(
        self,
        table_name: str,
        *,
        output: connection._OutputType,
        columns: typing.Optional[typing.Iterable[str]] = ...,
        schema_name: typing.Optional[str] = ...,
        timeout: typing.Optional[float] = ...,
        format: typing.Optional[connection._CopyFormat] = ...,
        oids: typing.Optional[int] = ...,
        delimiter: typing.Optional[str] = ...,
        null: typing.Optional[str] = ...,
        header: typing.Optional[bool] = ...,
        quote: typing.Optional[str] = ...,
        escape: typing.Optional[str] = ...,
        force_quote: typing.Optional[bool] = ...,
        encoding: typing.Optional[str] = ...,
    ) -> str: ...
    async def copy_from_query(
        self,
        query: str,
        *args: typing.Any,
        output: connection._OutputType,
        timeout: typing.Optional[float] = ...,
        format: typing.Optional[connection._CopyFormat] = ...,
        oids: typing.Optional[int] = ...,
        delimiter: typing.Optional[str] = ...,
        null: typing.Optional[str] = ...,
        header: typing.Optional[bool] = ...,
        quote: typing.Optional[str] = ...,
        escape: typing.Optional[str] = ...,
        force_quote: typing.Optional[bool] = ...,
        encoding: typing.Optional[str] = ...,
    ) -> str: ...
    async def copy_to_table(
        self,
        table_name: str,
        *,
        source: connection._SourceType,
        columns: typing.Optional[typing.Iterable[str]] = ...,
        schema_name: typing.Optional[str] = ...,
        timeout: typing.Optional[float] = ...,
        format: typing.Optional[connection._CopyFormat] = ...,
        oids: typing.Optional[int] = ...,
        freeze: typing.Optional[bool] = ...,
        delimiter: typing.Optional[str] = ...,
        null: typing.Optional[str] = ...,
        header: typing.Optional[bool] = ...,
        quote: typing.Optional[str] = ...,
        escape: typing.Optional[str] = ...,
        force_quote: typing.Optional[bool] = ...,
        force_not_null: typing.Optional[bool] = ...,
        force_null: typing.Optional[bool] = ...,
        encoding: typing.Optional[str] = ...,
    ) -> str: ...
    async def copy_records_to_table(
        self,
        table_name: str,
        *,
        records: typing.Iterable[typing.Sequence[typing.Any]],
        columns: typing.Optional[typing.Iterable[str]] = ...,
        schema_name: typing.Optional[str] = ...,
        timeout: typing.Optional[float] = ...,
    ) -> str: ...
    async def set_type_codec(
        self,
        typename: str,
        *,
        schema: str = ...,
        encoder: typing.Callable[[typing.Any], typing.Any],
        decoder: typing.Callable[[typing.Any], typing.Any],
        format: str = ...,
    ) -> None: ...
    async def reset_type_codec(self, typename: str, *, schema: str = ...) -> None: ...
    async def set_builtin_type_codec(
        self,
        typename: str,
        *,
        schema: str = ...,
        codec_name: str,
        format: typing.Optional[str] = ...,
    ) -> None: ...
    def is_closed(self) -> bool: ...
    async def close(self, *, timeout: typing.Optional[float] = ...) -> None: ...
    def terminate(self) -> None: ...
    async def reset(self, *, timeout: typing.Optional[float] = ...) -> None: ...
    async def reload_schema_state(self) -> None: ...

class PoolConnectionHolder(typing.Generic[_Record]):
    _pool: Pool[_Record]
    async def connect(self) -> None: ...
    async def acquire(self) -> PoolConnectionProxy[_Record]: ...
    async def release(self, timeout: typing.Optional[float]) -> None: ...
    async def wait_until_released(self) -> None: ...
    async def close(self) -> None: ...
    def terminate(self) -> None: ...
    def _release_on_close(self) -> None: ...

class Pool(typing.Generic[_Record]):
    def set_connect_args(
        self,
        dsn: typing.Optional[str] = ...,
        *,
        host: typing.Optional[connect_utils._HostType] = ...,
        port: typing.Optional[connect_utils._PortType] = ...,
        user: typing.Optional[str] = ...,
        password: typing.Optional[connection._PasswordType] = ...,
        passfile: typing.Optional[str] = ...,
        database: typing.Optional[str] = ...,
        timeout: float = ...,
        statement_cache_size: int = ...,
        max_cached_statement_lifetime: int = ...,
        max_cacheable_statement_size: int = ...,
        command_timeout: typing.Optional[float] = ...,
        ssl: typing.Optional[connect_utils._SSLType] = ...,
        server_settings: typing.Optional[typing.Dict[str, str]] = ...,
    ) -> None: ...
    async def execute(
        self, query: str, *args: typing.Any, timeout: typing.Optional[float] = ...
    ) -> str: ...
    async def executemany(
        self,
        command: str,
        args: typing.Iterable[typing.Sequence[typing.Any]],
        *,
        timeout: typing.Optional[float] = ...,
    ) -> None: ...
    async def fetch(
        self, query: str, *args: typing.Any, timeout: typing.Optional[float] = ...
    ) -> typing.List[_cprotocol.Record]: ...
    async def fetchval(
        self,
        query: str,
        *args: typing.Any,
        column: int = ...,
        timeout: typing.Optional[float] = ...,
    ) -> typing.Any: ...
    async def fetchrow(
        self, query: str, *args: typing.Any, timeout: typing.Optional[float] = ...
    ) -> typing.Optional[_cprotocol.Record]: ...
    def acquire(
        self, *, timeout: typing.Optional[float] = ...
    ) -> PoolAcquireContext[_Record]: ...
    async def release(
        self,
        connection: PoolConnectionProxy[_Record],
        *,
        timeout: typing.Optional[float] = ...,
    ) -> None: ...
    async def close(self) -> None: ...
    def terminate(self) -> None: ...
    async def expire_connections(self) -> None: ...
    def _drop_statement_cache(self) -> None: ...
    def _drop_type_cache(self) -> None: ...
    def __await__(
        self: _Pool,
    ) -> typing.Generator[typing.Any, None, typing.Optional[_Pool]]: ...
    async def __aenter__(self: _Pool) -> _Pool: ...
    async def __aexit__(self, *exc: typing.Any) -> None: ...

class PoolAcquireContext(typing.Generic[_Record]):
    async def __aenter__(self) -> PoolConnectionProxy[_Record]: ...
    async def __aexit__(self, *exc: typing.Any) -> None: ...
    def __await__(
        self,
    ) -> typing.Generator[typing.Any, None, PoolConnectionProxy[_Record]]: ...

@typing.overload
def create_pool(
    dsn: typing.Optional[str] = ...,
    *,
    min_size: int = ...,
    max_size: int = ...,
    max_queries: int = ...,
    max_inactive_connection_lifetime: float = ...,
    setup: typing.Optional[_SetupCallback[_cprotocol.Record]] = ...,
    init: typing.Optional[_InitCallback[_cprotocol.Record]] = ...,
    loop: typing.Optional[asyncio.AbstractEventLoop] = ...,
    connection_class: typing.Type[_Connection] = ...,
    record_class: typing.Optional[typing.Type[_cprotocol.Record]] = ...,
    host: typing.Optional[connect_utils._HostType] = ...,
    port: typing.Optional[connect_utils._PortType] = ...,
    user: typing.Optional[str] = ...,
    password: typing.Optional[connection._PasswordType] = ...,
    passfile: typing.Optional[str] = ...,
    database: typing.Optional[str] = ...,
    timeout: float = ...,
    statement_cache_size: int = ...,
    max_cached_statement_lifetime: int = ...,
    max_cacheable_statement_size: int = ...,
    command_timeout: typing.Optional[float] = ...,
    ssl: typing.Optional[connect_utils._SSLType] = ...,
    server_settings: typing.Optional[typing.Dict[str, str]] = ...,
) -> Pool[_cprotocol.Record]: ...
@typing.overload
def create_pool(
    dsn: typing.Optional[str] = ...,
    *,
    min_size: int = ...,
    max_size: int = ...,
    max_queries: int = ...,
    max_inactive_connection_lifetime: float = ...,
    setup: typing.Optional[_SetupCallback[_Record]] = ...,
    init: typing.Optional[_InitCallback[_Record]] = ...,
    loop: typing.Optional[asyncio.AbstractEventLoop] = ...,
    connection_class: typing.Type[_Connection] = ...,
    record_class: typing.Type[_Record],
    host: typing.Optional[connect_utils._HostType] = ...,
    port: typing.Optional[connect_utils._PortType] = ...,
    user: typing.Optional[str] = ...,
    password: typing.Optional[connection._PasswordType] = ...,
    passfile: typing.Optional[str] = ...,
    database: typing.Optional[str] = ...,
    timeout: float = ...,
    statement_cache_size: int = ...,
    max_cached_statement_lifetime: int = ...,
    max_cacheable_statement_size: int = ...,
    command_timeout: typing.Optional[float] = ...,
    ssl: typing.Optional[connect_utils._SSLType] = ...,
    server_settings: typing.Optional[typing.Dict[str, str]] = ...,
) -> Pool[_Record]: ...
