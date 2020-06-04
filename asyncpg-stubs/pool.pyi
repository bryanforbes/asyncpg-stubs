import asyncio
import typing

from . import connect_utils, connection, cursor, prepared_stmt, transaction, types
from .protocol import protocol as _cprotocol

_SetupCallback = typing.Callable[
    [PoolConnectionProxy], typing.Coroutine[typing.Any, typing.Any, None]
]
_InitCallback = typing.Callable[
    [connection.Connection], typing.Coroutine[typing.Any, typing.Any, None]
]

_Pool = typing.TypeVar('_Pool', bound=Pool)
_Record = typing.TypeVar('_Record', bound=_cprotocol.Record)

class PoolConnectionProxyMeta(type): ...

class PoolConnectionProxy(
    connection._ConnectionProxy, metaclass=PoolConnectionProxyMeta, wrap=True
):
    async def add_listener(
        self, channel: str, callback: connection._Listener
    ) -> None: ...
    async def remove_listener(
        self, channel: str, callback: connection._Listener
    ) -> None: ...
    def add_log_listener(self, callback: connection._LogListener) -> None: ...
    def remove_log_listener(self, callback: connection._LogListener) -> None: ...
    def get_server_pid(self) -> int: ...
    def get_server_version(self) -> types.ServerVersion: ...
    def get_settings(self) -> _cprotocol.ConnectionSettings: ...
    def transaction(
        self,
        *,
        isolation: transaction._IsolationLevels = ...,
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
    ) -> cursor.CursorFactory[_cprotocol.Record]: ...
    @typing.overload
    def cursor(
        self,
        query: str,
        *args: typing.Any,
        prefetch: typing.Optional[int] = ...,
        timeout: typing.Optional[float] = ...,
        return_type: typing.Type[_Record],
    ) -> cursor.CursorFactory[_Record]: ...
    @typing.overload
    async def prepare(
        self, query: str, *, timeout: typing.Optional[float] = ...
    ) -> prepared_stmt.PreparedStatement[_cprotocol.Record]: ...
    @typing.overload
    async def prepare(
        self,
        query: str,
        *,
        timeout: typing.Optional[float] = ...,
        return_type: typing.Type[_Record],
    ) -> prepared_stmt.PreparedStatement[_Record]: ...
    @typing.overload
    async def fetch(
        self, query: str, *args: typing.Any, timeout: typing.Optional[float] = ...
    ) -> typing.List[_cprotocol.Record]: ...
    @typing.overload
    async def fetch(
        self,
        query: str,
        *args: typing.Any,
        timeout: typing.Optional[float] = ...,
        return_type: typing.Type[_Record],
    ) -> typing.List[_Record]: ...
    async def fetchval(
        self,
        query: str,
        *args: typing.Any,
        column: int = ...,
        timeout: typing.Optional[float] = ...,
    ) -> typing.Any: ...
    @typing.overload
    async def fetchrow(
        self, query: str, *args: typing.Any, timeout: typing.Optional[float] = ...
    ) -> typing.Optional[_cprotocol.Record]: ...
    @typing.overload
    async def fetchrow(
        self,
        query: str,
        *args: typing.Any,
        timeout: typing.Optional[float] = ...,
        return_type: typing.Type[_Record],
    ) -> typing.Optional[_Record]: ...
    async def copy_from_table(
        self,
        table_name: str,
        *,
        output: connection._OutputType[typing.AnyStr],
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
        output: connection._OutputType[typing.AnyStr],
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
        source: connection._SourceType[typing.AnyStr],
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

class PoolConnectionHolder:
    async def connect(self) -> None: ...
    async def acquire(self) -> PoolConnectionProxy: ...
    async def release(self, timeout: typing.Optional[float]) -> None: ...
    async def wait_until_released(self) -> None: ...
    async def close(self) -> None: ...
    def terminate(self) -> None: ...

class Pool:
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
    @typing.overload
    async def fetch(
        self, query: str, *args: typing.Any, timeout: typing.Optional[float] = ...
    ) -> typing.List[_cprotocol.Record]: ...
    @typing.overload
    async def fetch(
        self,
        query: str,
        *args: typing.Any,
        timeout: typing.Optional[float] = ...,
        return_type: typing.Type[_Record],
    ) -> typing.List[_Record]: ...
    async def fetchval(
        self,
        query: str,
        *args: typing.Any,
        column: int = ...,
        timeout: typing.Optional[float] = ...,
    ) -> typing.Any: ...
    @typing.overload
    async def fetchrow(
        self, query: str, *args: typing.Any, timeout: typing.Optional[float] = ...
    ) -> typing.Optional[_cprotocol.Record]: ...
    @typing.overload
    async def fetchrow(
        self,
        query: str,
        *args: typing.Any,
        timeout: typing.Optional[float] = ...,
        return_type: typing.Type[_Record],
    ) -> typing.Optional[_Record]: ...
    def acquire(
        self, *, timeout: typing.Optional[float] = ...
    ) -> PoolAcquireContext: ...
    async def release(
        self, connection: PoolConnectionProxy, *, timeout: typing.Optional[float] = ...
    ) -> None: ...
    async def close(self) -> None: ...
    def terminate(self) -> None: ...
    async def expire_connections(self) -> None: ...
    def __await__(
        self: _Pool,
    ) -> typing.Generator[typing.Any, None, typing.Optional[_Pool]]: ...
    async def __aenter__(self: _Pool) -> _Pool: ...
    async def __aexit__(self, *exc: typing.Any) -> None: ...

class PoolAcquireContext:
    async def __aenter__(self) -> PoolConnectionProxy: ...
    async def __aexit__(self, *exc: typing.Any) -> None: ...
    def __await__(self) -> typing.Generator[typing.Any, None, PoolConnectionProxy]: ...

def create_pool(
    dsn: typing.Optional[str] = ...,
    *,
    min_size: int = ...,
    max_size: int = ...,
    max_queries: int = ...,
    max_inactive_connection_lifetime: float = ...,
    setup: typing.Optional[_SetupCallback] = ...,
    init: typing.Optional[_InitCallback] = ...,
    loop: typing.Optional[asyncio.AbstractEventLoop] = ...,
    connection_class: typing.Type[connection.Connection] = ...,
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
) -> Pool: ...
