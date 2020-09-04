from asyncio import AbstractEventLoop
from ssl import SSLContext
from typing import (
    IO,
    Any,
    AnyStr,
    AsyncIterable,
    Callable,
    Coroutine,
    Dict,
    Iterable,
    List,
    NamedTuple,
    Optional,
    Sequence,
    Tuple,
    Type,
    TypeVar,
    Union,
    overload,
)
from typing_extensions import Literal, Protocol

from . import connect_utils
from .compat import PathLike
from .cursor import CursorFactory
from .exceptions import PostgresLogMessage
from .pool import PoolConnectionProxy
from .prepared_stmt import PreparedStatement
from .protocol import Record
from .protocol.protocol import BaseProtocol, ConnectionSettings, PreparedStatementState
from .transaction import Transaction, _IsolationLevels
from .types import ServerVersion

_Connection = TypeVar('_Connection', bound='Connection')
_Writer = Callable[[bytes], Coroutine[Any, Any, None]]
_Record = TypeVar('_Record', bound=Record)
_RecordsType = List[Record]
_RecordsExtraType = Tuple[_RecordsType, bytes, bool]
_AnyCallable = Callable[..., Any]

_OutputType = Union[AnyStr, PathLike[AnyStr], IO[AnyStr], _Writer]
_SourceType = Union[AnyStr, PathLike[AnyStr], IO[AnyStr], AsyncIterable[bytes]]

_CopyFormat = Literal['text', 'csv', 'binary']
_PasswordType = Union[str, Callable[[], str]]

class _Listener(Protocol):
    def __call__(
        self,
        __con_ref: Union[Connection, PoolConnectionProxy],
        __pid: int,
        __channel: str,
        __payload: Any,
    ) -> None: ...

class _LogListener(Protocol):
    def __call__(
        self,
        __con_ref: Union[Connection, PoolConnectionProxy],
        __message: PostgresLogMessage,
    ) -> None: ...

class _OnRemove(Protocol):
    def __call__(self, __statement: PreparedStatementState) -> None: ...

class _Executor(Protocol):
    def __call__(
        self,
        __statement: PreparedStatementState,
        __timeout: Optional[float],
    ) -> Any: ...

class ConnectionMeta(type):
    def __instancecheck__(cls, instance: Any) -> Any: ...

class Connection:
    def __init__(
        self,
        protocol: BaseProtocol,
        transport: Any,
        loop: AbstractEventLoop,
        addr: Union[Tuple[str, int], str],
        config: connect_utils._ClientConfiguration,
        params: connect_utils._ConnectionParameters,
    ) -> None: ...
    def __del__(self) -> None: ...
    async def add_listener(self, channel: str, callback: _Listener) -> None: ...
    async def remove_listener(self, channel: str, callback: _Listener) -> None: ...
    def add_log_listener(self, callback: _LogListener) -> None: ...
    def remove_log_listener(self, callback: _LogListener) -> None: ...
    def get_server_pid(self) -> int: ...
    def get_server_version(self) -> ServerVersion: ...
    def get_settings(self) -> ConnectionSettings: ...
    def transaction(
        self,
        *,
        isolation: _IsolationLevels = ...,
        readonly: bool = ...,
        deferrable: bool = ...,
    ) -> Transaction: ...
    def is_in_transaction(self) -> bool: ...
    async def execute(
        self, query: str, *args: Any, timeout: Optional[float] = ...
    ) -> str: ...
    async def executemany(
        self,
        command: str,
        args: Iterable[Sequence[Any]],
        *,
        timeout: Optional[float] = ...,
    ) -> None: ...
    def cursor(
        self,
        query: str,
        *args: Any,
        prefetch: Optional[int] = ...,
        timeout: Optional[float] = ...,
    ) -> CursorFactory[Record]: ...
    async def prepare(
        self, query: str, *, timeout: Optional[float] = ...
    ) -> PreparedStatement[Record]: ...
    async def fetch(
        self, query: str, *args: Any, timeout: Optional[float] = ...
    ) -> List[Record]: ...
    async def fetchval(
        self, query: str, *args: Any, column: int = ..., timeout: Optional[float] = ...
    ) -> Optional[Any]: ...
    async def fetchrow(
        self, query: str, *args: Any, timeout: Optional[float] = ...
    ) -> Optional[Record]: ...
    async def copy_from_table(
        self,
        table_name: str,
        *,
        output: _OutputType[AnyStr],
        columns: Optional[Iterable[str]] = None,
        schema_name: Optional[str] = None,
        timeout: Optional[float] = None,
        format: Optional[_CopyFormat] = None,
        oids: Optional[int] = None,
        delimiter: Optional[str] = None,
        null: Optional[str] = None,
        header: Optional[bool] = None,
        quote: Optional[str] = None,
        escape: Optional[str] = None,
        force_quote: Optional[bool] = None,
        encoding: Optional[str] = None,
    ) -> str: ...
    async def copy_from_query(
        self,
        query: str,
        *args: Any,
        output: _OutputType[AnyStr],
        timeout: Optional[float] = None,
        format: Optional[_CopyFormat] = None,
        oids: Optional[int] = None,
        delimiter: Optional[str] = None,
        null: Optional[str] = None,
        header: Optional[bool] = None,
        quote: Optional[str] = None,
        escape: Optional[str] = None,
        force_quote: Optional[bool] = None,
        encoding: Optional[str] = None,
    ) -> str: ...
    async def copy_to_table(
        self,
        table_name: str,
        *,
        source: _SourceType[AnyStr],
        columns: Optional[Iterable[str]] = None,
        schema_name: Optional[str] = None,
        timeout: Optional[float] = None,
        format: Optional[_CopyFormat] = None,
        oids: Optional[int] = None,
        freeze: Optional[bool] = None,
        delimiter: Optional[str] = None,
        null: Optional[str] = None,
        header: Optional[bool] = None,
        quote: Optional[str] = None,
        escape: Optional[str] = None,
        force_quote: Optional[bool] = None,
        force_not_null: Optional[bool] = None,
        force_null: Optional[bool] = None,
        encoding: Optional[str] = None,
    ) -> str: ...
    async def copy_records_to_table(
        self,
        table_name: str,
        *,
        records: Iterable[Sequence[Any]],
        columns: Optional[Iterable[str]] = None,
        schema_name: Optional[str] = None,
        timeout: Optional[float] = None,
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
        format: Optional[str] = ...,
    ) -> None: ...
    def is_closed(self) -> bool: ...
    async def close(self, *, timeout: Optional[float] = ...) -> None: ...
    def terminate(self) -> None: ...
    async def reset(self, *, timeout: Optional[float] = ...) -> None: ...
    async def reload_schema_state(self) -> None: ...

@overload
def connect(
    dsn: Optional[str] = ...,
    *,
    host: Optional[connect_utils._HostType] = ...,
    port: Optional[connect_utils._PortType] = ...,
    user: Optional[str] = ...,
    password: Optional[_PasswordType] = ...,
    passfile: Optional[str] = ...,
    database: Optional[str] = ...,
    loop: Optional[AbstractEventLoop] = ...,
    timeout: float = ...,
    statement_cache_size: int = ...,
    max_cached_statement_lifetime: int = ...,
    max_cacheable_statement_size: int = ...,
    command_timeout: Optional[float] = ...,
    ssl: Optional[connect_utils._SSLType] = ...,
    server_settings: Optional[Dict[str, str]] = ...,
) -> Connection: ...
@overload
def connect(
    dsn: Optional[str] = ...,
    *,
    host: Optional[connect_utils._HostType] = ...,
    port: Optional[connect_utils._PortType] = ...,
    user: Optional[str] = ...,
    password: Optional[_PasswordType] = ...,
    passfile: Optional[str] = ...,
    database: Optional[str] = ...,
    loop: Optional[AbstractEventLoop] = ...,
    timeout: float = ...,
    statement_cache_size: int = ...,
    max_cached_statement_lifetime: int = ...,
    max_cacheable_statement_size: int = ...,
    command_timeout: Optional[float] = ...,
    ssl: Optional[connect_utils._SSLType] = ...,
    connection_class: Type[_Connection],
    server_settings: Optional[Dict[str, str]] = ...,
) -> _Connection: ...

class _ConnectionProxy: ...

class ServerCapabilities(NamedTuple):
    advisory_locks: bool
    notifications: bool
    plpgsql: bool
    sql_reset: bool
    sql_close_all: bool
