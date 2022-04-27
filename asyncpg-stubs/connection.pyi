import asyncio
import collections
import os
import typing
import typing_extensions
import weakref

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

_Connection = typing.TypeVar('_Connection', bound='Connection[typing.Any]')
_Writer = typing.Callable[[bytes], typing.Coroutine[typing.Any, typing.Any, None]]
_Record = typing.TypeVar('_Record', bound=protocol.Record)
_OtherRecord = typing.TypeVar('_OtherRecord', bound=protocol.Record)
_RecordsType = typing.List[_Record]
_RecordsExtraType = typing.Tuple[_RecordsType[_Record], bytes, bool]

OutputType = typing.Union['os.PathLike[typing.Any]', typing.BinaryIO, _Writer]
SourceType = typing.Union[
    'os.PathLike[typing.Any]', typing.BinaryIO, typing.AsyncIterable[bytes]
]

CopyFormat = typing_extensions.Literal['text', 'csv', 'binary']
PasswordType = typing.Union[
    str,
    typing.Callable[[], str],
    typing.Callable[[], typing.Coroutine[typing.Any, typing.Any, str]],
]

class Listener(typing_extensions.Protocol):
    def __call__(
        self,
        __con_ref: typing.Union[
            'Connection[typing.Any]', 'pool.PoolConnectionProxy[typing.Any]'
        ],
        __pid: int,
        __channel: str,
        __payload: typing.Any,
    ) -> typing.Union[
        None, typing.Awaitable[None], typing.Generator[typing.Any, None, None]
    ]: ...

class LogListener(typing_extensions.Protocol):
    def __call__(
        self,
        __con_ref: typing.Union[
            'Connection[typing.Any]', 'pool.PoolConnectionProxy[typing.Any]'
        ],
        __message: exceptions.PostgresLogMessage,
    ) -> typing.Union[
        None, typing.Awaitable[None], typing.Generator[typing.Any, None, None]
    ]: ...

class TerminationListener(typing_extensions.Protocol):
    def __call__(
        self,
        __con_ref: typing.Union[
            'Connection[typing.Any]', 'pool.PoolConnectionProxy[typing.Any]'
        ],
    ) -> typing.Union[
        None, typing.Awaitable[None], typing.Generator[typing.Any, None, None]
    ]: ...

class OnRemove(typing_extensions.Protocol[_Record]):
    def __call__(
        self, __statement: _cprotocol.PreparedStatementState[_Record]
    ) -> None: ...

class Executor(typing_extensions.Protocol[_Record]):
    def __call__(
        self,
        __statement: _cprotocol.PreparedStatementState[_Record],
        __timeout: typing.Optional[float],
    ) -> typing.Any: ...

class ConnectionMeta(type):
    def __instancecheck__(cls, instance: typing.Any) -> bool: ...

class Connection(typing.Generic[_Record], metaclass=ConnectionMeta):
    __slots__: typing.Any
    _protocol: _cprotocol.BaseProtocol[_Record]
    _transport: typing.Any
    _loop: asyncio.AbstractEventLoop
    _top_xact: typing.Optional[transaction.Transaction]
    _aborted: bool
    _pool_release_ctr: int
    _stmt_cache: _StatementCache
    _stmts_to_close: typing.Set['_cprotocol.PreparedStatementState[typing.Any]']
    _listeners: typing.Dict[str, typing.Set['_Callback']]
    _server_version: types.ServerVersion
    _server_caps: ServerCapabilities
    _intro_query: str
    _reset_query: typing.Optional[str]
    _proxy: typing.Optional['pool.PoolConnectionProxy[typing.Any]']
    _stmt_exclusive_section: _Atomic
    _config: connect_utils._ClientConfiguration
    _params: connect_utils._ConnectionParameters
    _addr: typing.Union[typing.Tuple[str, int], str]
    _log_listeners: typing.Set['_Callback']
    _termination_listeners: typing.Set['_Callback']
    _cancellations: typing.Set['asyncio.Task[typing.Any]']
    _source_traceback: typing.Optional[str]
    def __init__(
        self,
        protocol: _cprotocol.BaseProtocol[_Record],
        transport: typing.Any,
        loop: asyncio.AbstractEventLoop,
        addr: typing.Union[typing.Tuple[str, int], str],
        config: connect_utils._ClientConfiguration,
        params: connect_utils._ConnectionParameters,
    ) -> None: ...
    def __del__(self) -> None: ...
    async def add_listener(self, channel: str, callback: Listener) -> None: ...
    async def remove_listener(self, channel: str, callback: Listener) -> None: ...
    def add_log_listener(self, callback: LogListener) -> None: ...
    def remove_log_listener(self, callback: LogListener) -> None: ...
    def add_termination_listener(self, callback: TerminationListener) -> None: ...
    def remove_termination_listener(self, callback: TerminationListener) -> None: ...
    def get_server_pid(self) -> int: ...
    def get_server_version(self) -> types.ServerVersion: ...
    def get_settings(self) -> _cprotocol.ConnectionSettings: ...
    def transaction(
        self,
        *,
        isolation: typing.Optional[transaction.IsolationLevels] = ...,
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
    async def _get_statement(
        self,
        query: str,
        timeout: typing.Optional[float],
        *,
        named: typing.Union[bool, str] = ...,
        use_cache: bool = ...,
        ignore_custom_codec: bool = ...,
        record_class: None = ...,
    ) -> _cprotocol.PreparedStatementState[_Record]: ...
    @typing.overload
    async def _get_statement(
        self,
        query: str,
        timeout: typing.Optional[float],
        *,
        named: typing.Union[bool, str] = ...,
        use_cache: bool = ...,
        ignore_custom_codec: bool = ...,
        record_class: typing.Type[_OtherRecord],
    ) -> _cprotocol.PreparedStatementState[_OtherRecord]: ...
    @typing.overload
    async def _get_statement(
        self,
        query: str,
        timeout: typing.Optional[float],
        *,
        named: typing.Union[bool, str] = ...,
        use_cache: bool = ...,
        ignore_custom_codec: bool = ...,
        record_class: typing.Optional[typing.Type[_OtherRecord]],
    ) -> typing.Union[
        '_cprotocol.PreparedStatementState[_Record]',
        '_cprotocol.PreparedStatementState[_OtherRecord]',
    ]: ...
    async def _introspect_types(
        self, typeoids: typing.Set[int], timeout: typing.Optional[float]
    ) -> typing.Tuple[typing.Any, '_cprotocol.PreparedStatementState[_Record]']: ...
    async def _introspect_type(self, typename: str, schema: str) -> typing.Any: ...
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
        'cursor.CursorFactory[_Record]', 'cursor.CursorFactory[_OtherRecord]'
    ]: ...
    @typing.overload
    async def prepare(
        self,
        query: str,
        *,
        name: typing.Optional[str] = ...,
        timeout: typing.Optional[float] = ...,
        record_class: None = ...,
    ) -> prepared_stmt.PreparedStatement[_Record]: ...
    @typing.overload
    async def prepare(
        self,
        query: str,
        *,
        name: typing.Optional[str] = ...,
        timeout: typing.Optional[float] = ...,
        record_class: typing.Type[_OtherRecord],
    ) -> prepared_stmt.PreparedStatement[_OtherRecord]: ...
    @typing.overload
    async def prepare(
        self,
        query: str,
        *,
        name: typing.Optional[str] = ...,
        timeout: typing.Optional[float] = ...,
        record_class: typing.Optional[typing.Type[_OtherRecord]],
    ) -> typing.Union[
        prepared_stmt.PreparedStatement[_Record],
        prepared_stmt.PreparedStatement[_OtherRecord],
    ]: ...
    @typing.overload
    async def _prepare(
        self,
        query: str,
        *,
        name: typing.Optional[str] = ...,
        timeout: typing.Optional[float] = ...,
        use_cache: bool = ...,
        record_class: None = ...,
    ) -> prepared_stmt.PreparedStatement[_Record]: ...
    @typing.overload
    async def _prepare(
        self,
        query: str,
        *,
        name: typing.Optional[str] = ...,
        timeout: typing.Optional[float] = ...,
        use_cache: bool = ...,
        record_class: typing.Type[_OtherRecord],
    ) -> prepared_stmt.PreparedStatement[_OtherRecord]: ...
    @typing.overload
    async def _prepare(
        self,
        query: str,
        *,
        name: typing.Optional[str] = ...,
        timeout: typing.Optional[float] = ...,
        use_cache: bool = ...,
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
        output: OutputType,
        *,
        columns: typing.Optional[typing.Iterable[str]] = ...,
        schema_name: typing.Optional[str] = ...,
        timeout: typing.Optional[float] = ...,
        format: typing.Optional[CopyFormat] = ...,
        oids: typing.Optional[int] = ...,
        delimiter: typing.Optional[str] = ...,
        null: typing.Optional[str] = ...,
        header: typing.Optional[bool] = ...,
        quote: typing.Optional[str] = ...,
        escape: typing.Optional[str] = ...,
        force_quote: typing.Union[bool, typing.Iterable[str], None] = ...,
        encoding: typing.Optional[str] = ...,
    ) -> str: ...
    async def copy_from_query(
        self,
        query: str,
        *args: typing.Any,
        output: OutputType,
        timeout: typing.Optional[float] = ...,
        format: typing.Optional[CopyFormat] = ...,
        oids: typing.Optional[int] = ...,
        delimiter: typing.Optional[str] = ...,
        null: typing.Optional[str] = ...,
        header: typing.Optional[bool] = ...,
        quote: typing.Optional[str] = ...,
        escape: typing.Optional[str] = ...,
        force_quote: typing.Union[bool, typing.Iterable[str], None] = ...,
        encoding: typing.Optional[str] = ...,
    ) -> str: ...
    async def copy_to_table(
        self,
        table_name: str,
        source: SourceType,
        *,
        columns: typing.Optional[typing.Iterable[str]] = ...,
        schema_name: typing.Optional[str] = ...,
        timeout: typing.Optional[float] = ...,
        format: typing.Optional[CopyFormat] = ...,
        oids: typing.Optional[int] = ...,
        freeze: typing.Optional[bool] = ...,
        delimiter: typing.Optional[str] = ...,
        null: typing.Optional[str] = ...,
        header: typing.Optional[bool] = ...,
        quote: typing.Optional[str] = ...,
        escape: typing.Optional[str] = ...,
        force_quote: typing.Union[bool, typing.Iterable[str], None] = ...,
        force_not_null: typing.Union[bool, typing.Iterable[str], None] = ...,
        force_null: typing.Union[bool, typing.Iterable[str], None] = ...,
        encoding: typing.Optional[str] = ...,
    ) -> str: ...
    async def copy_records_to_table(
        self,
        table_name: str,
        records: typing.Union[
            typing.Iterable[typing.Sequence[typing.Any]],
            typing.AsyncIterable[typing.Sequence[typing.Any]],
        ],
        *,
        columns: typing.Optional[typing.Iterable[str]] = ...,
        schema_name: typing.Optional[str] = ...,
        timeout: typing.Optional[float] = ...,
    ) -> str: ...
    def _format_copy_opts(
        self,
        *,
        format: typing.Optional[CopyFormat] = ...,
        oids: typing.Optional[int] = ...,
        freeze: typing.Optional[bool] = ...,
        delimiter: typing.Optional[str] = ...,
        null: typing.Optional[str] = ...,
        header: typing.Optional[bool] = ...,
        quote: typing.Optional[str] = ...,
        escape: typing.Optional[str] = ...,
        force_quote: typing.Union[bool, typing.Iterable[str], None] = ...,
        force_not_null: typing.Union[bool, typing.Iterable[str], None] = ...,
        force_null: typing.Union[bool, typing.Iterable[str], None] = ...,
        encoding: typing.Optional[str] = ...,
    ) -> str: ...
    async def _copy_out(
        self, copy_stmt: str, output: OutputType, timeout: typing.Optional[float]
    ) -> str: ...
    async def _copy_in(
        self, copy_stmt: str, source: SourceType, timeout: typing.Optional[float]
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
    def _abort(self) -> None: ...
    def _cleanup(self) -> None: ...
    def _clean_tasks(self) -> None: ...
    def _check_open(self) -> None: ...
    def _get_unique_id(self, prefix: str) -> str: ...
    def _mark_stmts_as_closed(self) -> None: ...
    def _maybe_gc_stmt(
        self, stmt: _cprotocol.PreparedStatementState[typing.Any]
    ) -> None: ...
    async def _cleanup_stmts(self) -> None: ...
    async def _cancel(self, waiter: asyncio.Future[None]) -> None: ...
    def _cancel_current_command(self, waiter: asyncio.Future[None]) -> None: ...
    def _process_log_message(
        self, fields: typing.Dict[str, str], last_query: str
    ) -> None: ...
    def _call_termination_listeners(self) -> None: ...
    def _process_notification(
        self, pid: int, channel: str, payload: typing.Any
    ) -> None: ...
    def _unwrap(
        self,
    ) -> typing.Union[
        'Connection[_Record]', 'pool.PoolConnectionProxy[typing.Any]'
    ]: ...
    def _get_reset_query(self) -> str: ...
    def _set_proxy(
        self, proxy: typing.Optional['pool.PoolConnectionProxy[typing.Any]']
    ) -> None: ...
    def _check_listeners(self, listeners: typing.Sized, listener_type: str) -> None: ...
    def _on_release(self, stacklevel: int = ...) -> None: ...
    def _drop_local_statement_cache(self) -> None: ...
    def _drop_global_statement_cache(self) -> None: ...
    def _drop_local_type_cache(self) -> None: ...
    def _drop_global_type_cache(self) -> None: ...
    async def reload_schema_state(self) -> None: ...
    @typing.overload
    async def _execute(
        self,
        query: str,
        args: typing.Sequence[typing.Any],
        limit: int,
        timeout: typing.Optional[float],
        *,
        return_status: typing_extensions.Literal[False] = ...,
        ignore_custom_codec: bool = ...,
        record_class: None = ...,
    ) -> _RecordsType[_Record]: ...
    @typing.overload
    async def _execute(
        self,
        query: str,
        args: typing.Sequence[typing.Any],
        limit: int,
        timeout: typing.Optional[float],
        *,
        return_status: typing_extensions.Literal[False] = ...,
        ignore_custom_codec: bool = ...,
        record_class: typing.Type[_OtherRecord],
    ) -> _RecordsType[_OtherRecord]: ...
    @typing.overload
    async def _execute(
        self,
        query: str,
        args: typing.Sequence[typing.Any],
        limit: int,
        timeout: typing.Optional[float],
        *,
        return_status: typing_extensions.Literal[False] = ...,
        ignore_custom_codec: bool = ...,
        record_class: typing.Optional[typing.Type[_OtherRecord]],
    ) -> typing.Union[_RecordsType[_Record], _RecordsType[_OtherRecord]]: ...
    @typing.overload
    async def _execute(
        self,
        query: str,
        args: typing.Sequence[typing.Any],
        limit: int,
        timeout: typing.Optional[float],
        return_status: typing_extensions.Literal[True],
        *,
        ignore_custom_codec: bool = ...,
        record_class: None = ...,
    ) -> _RecordsExtraType[_Record]: ...
    @typing.overload
    async def _execute(
        self,
        query: str,
        args: typing.Sequence[typing.Any],
        limit: int,
        timeout: typing.Optional[float],
        return_status: typing_extensions.Literal[True],
        *,
        ignore_custom_codec: bool = ...,
        record_class: typing.Type[_OtherRecord],
    ) -> _RecordsExtraType[_OtherRecord]: ...
    @typing.overload
    async def _execute(
        self,
        query: str,
        args: typing.Sequence[typing.Any],
        limit: int,
        timeout: typing.Optional[float],
        return_status: typing_extensions.Literal[True],
        *,
        ignore_custom_codec: bool = ...,
        record_class: typing.Optional[typing.Type[_OtherRecord]],
    ) -> typing.Union[_RecordsExtraType[_Record], _RecordsExtraType[_OtherRecord]]: ...
    @typing.overload
    async def _execute(
        self,
        query: str,
        args: typing.Sequence[typing.Any],
        limit: int,
        timeout: typing.Optional[float],
        return_status: bool,
        *,
        ignore_custom_codec: bool = ...,
        record_class: typing.Optional[typing.Type[_OtherRecord]],
    ) -> typing.Union[
        _RecordsExtraType[_Record],
        _RecordsExtraType[_OtherRecord],
        _RecordsType[_Record],
        _RecordsType[_OtherRecord],
    ]: ...
    @typing.overload
    async def __execute(
        self,
        query: str,
        args: typing.Sequence[typing.Any],
        limit: int,
        timeout: typing.Optional[float],
        *,
        return_status: typing_extensions.Literal[False] = ...,
        ignore_custom_codec: bool = ...,
        record_class: None = ...,
    ) -> typing.Tuple[
        _RecordsType[_Record], '_cprotocol.PreparedStatementState[_Record]'
    ]: ...
    @typing.overload
    async def __execute(
        self,
        query: str,
        args: typing.Sequence[typing.Any],
        limit: int,
        timeout: typing.Optional[float],
        *,
        return_status: typing_extensions.Literal[False] = ...,
        ignore_custom_codec: bool = ...,
        record_class: typing.Type[_OtherRecord],
    ) -> typing.Tuple[
        _RecordsType[_OtherRecord], '_cprotocol.PreparedStatementState[_OtherRecord]'
    ]: ...
    @typing.overload
    async def __execute(
        self,
        query: str,
        args: typing.Sequence[typing.Any],
        limit: int,
        timeout: typing.Optional[float],
        return_status: typing_extensions.Literal[True],
        *,
        ignore_custom_codec: bool = ...,
        record_class: None = ...,
    ) -> typing.Tuple[
        _RecordsExtraType[_Record], '_cprotocol.PreparedStatementState[_Record]'
    ]: ...
    @typing.overload
    async def __execute(
        self,
        query: str,
        args: typing.Sequence[typing.Any],
        limit: int,
        timeout: typing.Optional[float],
        return_status: typing_extensions.Literal[True],
        *,
        ignore_custom_codec: bool = ...,
        record_class: typing.Type[_OtherRecord],
    ) -> typing.Tuple[
        _RecordsExtraType[_OtherRecord],
        '_cprotocol.PreparedStatementState[_OtherRecord]',
    ]: ...
    @typing.overload
    async def __execute(
        self,
        query: str,
        args: typing.Sequence[typing.Any],
        limit: int,
        timeout: typing.Optional[float],
        return_status: bool,
        *,
        ignore_custom_codec: bool = ...,
        record_class: typing.Optional[typing.Type[_OtherRecord]],
    ) -> typing.Union[
        typing.Tuple[
            _RecordsExtraType[_Record], '_cprotocol.PreparedStatementState[_Record]'
        ],
        typing.Tuple[
            _RecordsType[_Record], '_cprotocol.PreparedStatementState[_Record]'
        ],
        typing.Tuple[
            _RecordsExtraType[_OtherRecord],
            '_cprotocol.PreparedStatementState[_OtherRecord]',
        ],
        typing.Tuple[
            _RecordsType[_OtherRecord],
            '_cprotocol.PreparedStatementState[_OtherRecord]',
        ],
    ]: ...
    async def _executemany(
        self,
        query: str,
        args: typing.Iterable[typing.Sequence[typing.Any]],
        timeout: typing.Optional[float],
    ) -> None: ...
    @typing.overload
    async def _do_execute(
        self,
        query: str,
        executor: Executor[_Record],
        timeout: typing.Optional[float],
        retry: bool = ...,
        *,
        ignore_custom_codec: bool = ...,
        record_class: None = ...,
    ) -> typing.Tuple[typing.Any, '_cprotocol.PreparedStatementState[_Record]']: ...
    @typing.overload
    async def _do_execute(
        self,
        query: str,
        executor: Executor[_OtherRecord],
        timeout: typing.Optional[float],
        retry: bool = ...,
        *,
        ignore_custom_codec: bool = ...,
        record_class: typing.Type[_OtherRecord],
    ) -> typing.Tuple[
        typing.Any, '_cprotocol.PreparedStatementState[_OtherRecord]'
    ]: ...
    @typing.overload
    async def _do_execute(
        self,
        query: str,
        executor: Executor[_OtherRecord],
        timeout: typing.Optional[float],
        retry: bool = ...,
        *,
        ignore_custom_codec: bool = ...,
        record_class: typing.Optional[typing.Type[_OtherRecord]],
    ) -> typing.Union[
        typing.Tuple[typing.Any, '_cprotocol.PreparedStatementState[_Record]'],
        typing.Tuple[typing.Any, '_cprotocol.PreparedStatementState[_OtherRecord]'],
    ]: ...

@typing.overload
async def connect(
    dsn: typing.Optional[str] = ...,
    *,
    host: typing.Optional[connect_utils.HostType] = ...,
    port: typing.Optional[connect_utils.PortType] = ...,
    user: typing.Optional[str] = ...,
    password: typing.Optional[PasswordType] = ...,
    passfile: typing.Optional[str] = ...,
    database: typing.Optional[str] = ...,
    loop: typing.Optional[asyncio.AbstractEventLoop] = ...,
    timeout: float = ...,
    statement_cache_size: int = ...,
    max_cached_statement_lifetime: int = ...,
    max_cacheable_statement_size: int = ...,
    command_timeout: typing.Optional[float] = ...,
    ssl: typing.Optional[connect_utils.SSLType] = ...,
    connection_class: typing.Type[Connection[_Record]] = ...,
    record_class: typing.Type[_Record],
    server_settings: typing.Optional[typing.Dict[str, str]] = ...,
) -> Connection[_Record]: ...
@typing.overload
async def connect(
    dsn: typing.Optional[str] = ...,
    *,
    host: typing.Optional[connect_utils.HostType] = ...,
    port: typing.Optional[connect_utils.PortType] = ...,
    user: typing.Optional[str] = ...,
    password: typing.Optional[PasswordType] = ...,
    passfile: typing.Optional[str] = ...,
    database: typing.Optional[str] = ...,
    loop: typing.Optional[asyncio.AbstractEventLoop] = ...,
    timeout: float = ...,
    statement_cache_size: int = ...,
    max_cached_statement_lifetime: int = ...,
    max_cacheable_statement_size: int = ...,
    command_timeout: typing.Optional[float] = ...,
    ssl: typing.Optional[connect_utils.SSLType] = ...,
    connection_class: typing.Type[Connection[protocol.Record]] = ...,
    record_class: typing.Type[protocol.Record] = ...,
    server_settings: typing.Optional[typing.Dict[str, str]] = ...,
) -> Connection[protocol.Record]: ...
@typing.overload
async def connect(
    dsn: typing.Optional[str] = ...,
    *,
    host: typing.Optional[connect_utils.HostType] = ...,
    port: typing.Optional[connect_utils.PortType] = ...,
    user: typing.Optional[str] = ...,
    password: typing.Optional[PasswordType] = ...,
    passfile: typing.Optional[str] = ...,
    database: typing.Optional[str] = ...,
    loop: typing.Optional[asyncio.AbstractEventLoop] = ...,
    timeout: float = ...,
    statement_cache_size: int = ...,
    max_cached_statement_lifetime: int = ...,
    max_cacheable_statement_size: int = ...,
    command_timeout: typing.Optional[float] = ...,
    ssl: typing.Optional[connect_utils.SSLType] = ...,
    connection_class: typing.Type[_Connection],
    record_class: typing.Type[_Record] = ...,
    server_settings: typing.Optional[typing.Dict[str, str]] = ...,
) -> _Connection: ...

_StatementCacheKey = typing.Tuple[str, typing.Type[_Record], bool]

class _StatementCacheEntry(typing.Generic[_Record]):
    __slots__: typing.Any
    _query: _StatementCacheKey[_Record]
    _statement: _cprotocol.PreparedStatementState[_Record]
    _cache: _StatementCache
    _cleanup_cb: typing.Optional[asyncio.TimerHandle]
    def __init__(
        self,
        cache: _StatementCache,
        query: _StatementCacheKey[_Record],
        statement: _cprotocol.PreparedStatementState[_Record],
    ) -> None: ...

class _StatementCache:
    __slots__: typing.Any
    _loop: asyncio.AbstractEventLoop
    _entries: collections.OrderedDict[
        _StatementCacheKey[typing.Any], _StatementCacheEntry[typing.Any]
    ]
    _max_size: int
    _on_remove: OnRemove[typing.Any]
    _max_lifetime: float
    def __init__(
        self,
        loop: asyncio.AbstractEventLoop,
        max_size: int,
        on_remove: OnRemove[typing.Any],
        max_lifetime: float,
    ) -> None: ...
    def __len__(self) -> int: ...
    def get_max_size(self) -> int: ...
    def set_max_size(self, new_size: int) -> None: ...
    def get_max_lifetime(self) -> float: ...
    def set_max_lifetime(self, new_lifetime: float) -> None: ...
    def get(
        self, query: _StatementCacheKey[_Record], *, promote: bool = ...
    ) -> typing.Optional['_cprotocol.PreparedStatementState[_Record]']: ...
    def has(self, query: _StatementCacheKey[_Record]) -> bool: ...
    def put(
        self,
        query: _StatementCacheKey[_Record],
        statement: _cprotocol.PreparedStatementState[_Record],
    ) -> None: ...
    def iter_statements(
        self,
    ) -> typing.Iterator['_cprotocol.PreparedStatementState[typing.Any]']: ...
    def clear(self) -> None: ...
    def _set_entry_timeout(self, entry: _StatementCacheEntry[typing.Any]) -> None: ...
    def _new_entry(
        self,
        query: _StatementCacheKey[_Record],
        statement: _cprotocol.PreparedStatementState[_Record],
    ) -> _StatementCacheEntry[_Record]: ...
    def _on_entry_expired(self, entry: _StatementCacheEntry[typing.Any]) -> None: ...
    def _clear_entry_callback(
        self, entry: _StatementCacheEntry[typing.Any]
    ) -> None: ...
    def _maybe_cleanup(self) -> None: ...

class _Callback(typing.NamedTuple):
    cb: typing.Callable[
        ...,
        typing.Union[
            None, typing.Awaitable[None], typing.Generator[typing.Any, None, None]
        ],
    ]
    is_async: bool
    @classmethod
    def from_callable(
        cls,
        cb: typing.Callable[
            ...,
            typing.Union[
                None, typing.Awaitable[None], typing.Generator[typing.Any, None, None]
            ],
        ],
    ) -> _Callback: ...

class _Atomic:
    __slots__: typing.Any
    _acquired: int
    def __init__(self) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(self, t: typing.Any, e: typing.Any, tb: typing.Any) -> None: ...

class _ConnectionProxy(typing.Generic[_Record]):
    __slots__: typing.Any

class ServerCapabilities(typing.NamedTuple):
    advisory_locks: bool
    notifications: bool
    plpgsql: bool
    sql_reset: bool
    sql_close_all: bool

def _detect_server_capabilities(
    server_version: types.ServerVersion,
    connection_settings: _cprotocol.ConnectionSettings,
) -> ServerCapabilities: ...
def _extract_stack(limit: int = ...) -> str: ...
def _check_record_class(record_class: typing.Type[typing.Any]) -> None: ...
def _weak_maybe_gc_stmt(
    weak_ref: weakref.ref[Connection[typing.Any]],
    stmt: _cprotocol.PreparedStatementState[typing.Any],
) -> None: ...

_uid: int
