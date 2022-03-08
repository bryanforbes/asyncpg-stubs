from asyncio import AbstractEventLoop
from ssl import SSLContext
from typing import (
    IO,
    Any,
    AnyStr,
    AsyncIterable,
    BinaryIO,
    Callable,
    Coroutine,
    Dict,
    Generic,
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

from _typeshed import StrOrBytesPath

from . import connect_utils
from .cursor import CursorFactory
from .exceptions import PostgresLogMessage
from .pool import PoolConnectionProxy
from .prepared_stmt import PreparedStatement
from .protocol import Record
from .protocol.protocol import BaseProtocol, ConnectionSettings, PreparedStatementState
from .transaction import Transaction, _IsolationLevels
from .types import ServerVersion

_Connection = TypeVar('_Connection', bound='Connection[Any]')
_Writer = Callable[[bytes], Coroutine[Any, Any, None]]
_Record = TypeVar('_Record', bound=Record)
_OtherRecord = TypeVar('_OtherRecord', bound=Record)
_RecordsType = List[_Record]
_RecordsExtraType = Tuple[_RecordsType[_Record], bytes, bool]
_AnyCallable = Callable[..., Any]

_OutputType = Union[StrOrBytesPath, BinaryIO, _Writer]
_SourceType = Union[StrOrBytesPath, BinaryIO, AsyncIterable[bytes]]

_CopyFormat = Literal['text', 'csv', 'binary']
_PasswordType = Union[str, Callable[[], str], Callable[[], Coroutine[Any, Any, str]]]

class _Listener(Protocol):
    def __call__(
        self,
        __con_ref: Union[Connection[Any], PoolConnectionProxy[Any]],
        __pid: int,
        __channel: str,
        __payload: Any,
    ) -> None: ...

class _LogListener(Protocol):
    def __call__(
        self,
        __con_ref: Union[Connection[Any], PoolConnectionProxy[Any]],
        __message: PostgresLogMessage,
    ) -> None: ...

class _TerminationListener(Protocol):
    def __call__(
        self, __con_ref: Union[Connection[Any], PoolConnectionProxy[Any]]
    ) -> None: ...

class _OnRemove(Protocol[_Record]):
    def __call__(self, __statement: PreparedStatementState[_Record]) -> None: ...

class _Executor(Protocol[_Record]):
    def __call__(
        self,
        __statement: PreparedStatementState[_Record],
        __timeout: Optional[float],
    ) -> Any: ...

class ConnectionMeta(type):
    def __instancecheck__(cls, instance: Any) -> Any: ...

class Connection(Generic[_Record], metaclass=ConnectionMeta):
    def __init__(
        self,
        protocol: BaseProtocol[_Record],
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
    def add_termination_listener(self, callback: _TerminationListener) -> None: ...
    def remove_termination_listener(self, callback: _TerminationListener) -> None: ...
    def get_server_pid(self) -> int: ...
    def get_server_version(self) -> ServerVersion: ...
    def get_settings(self) -> ConnectionSettings: ...
    def transaction(
        self,
        *,
        isolation: Optional[_IsolationLevels] = ...,
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
    @overload
    def cursor(
        self,
        query: str,
        *args: Any,
        prefetch: Optional[int] = ...,
        timeout: Optional[float] = ...,
        record_class: None = ...,
    ) -> CursorFactory[_Record]: ...
    @overload
    def cursor(
        self,
        query: str,
        *args: Any,
        prefetch: Optional[int] = ...,
        timeout: Optional[float] = ...,
        record_class: Type[_OtherRecord],
    ) -> CursorFactory[_OtherRecord]: ...
    @overload
    def cursor(
        self,
        query: str,
        *args: Any,
        prefetch: Optional[int] = ...,
        timeout: Optional[float] = ...,
        record_class: Optional[Type[_OtherRecord]],
    ) -> Union[CursorFactory[_Record], CursorFactory[_OtherRecord]]: ...
    @overload
    def cursor(
        self,
        query: str,
        *args: Any,
        prefetch: Optional[int] = ...,
        timeout: Optional[float] = ...,
        record_class: Optional[Type[_OtherRecord]] = ...,
    ) -> Union[CursorFactory[_OtherRecord], CursorFactory[_Record]]: ...
    @overload
    async def prepare(
        self,
        query: str,
        *,
        timeout: Optional[float] = ...,
        record_class: None = ...,
    ) -> PreparedStatement[_Record]: ...
    @overload
    async def prepare(
        self,
        query: str,
        *,
        timeout: Optional[float] = ...,
        record_class: Type[_OtherRecord],
    ) -> PreparedStatement[_OtherRecord]: ...
    @overload
    async def prepare(
        self,
        query: str,
        *,
        timeout: Optional[float] = ...,
        record_class: Optional[Type[_OtherRecord]],
    ) -> Union[PreparedStatement[_Record], PreparedStatement[_OtherRecord]]: ...
    @overload
    async def prepare(
        self,
        query: str,
        *,
        timeout: Optional[float] = ...,
        record_class: Optional[Type[_OtherRecord]] = ...,
    ) -> Union[PreparedStatement[_Record], PreparedStatement[_OtherRecord]]: ...
    @overload
    async def fetch(
        self,
        query: str,
        *args: Any,
        timeout: Optional[float] = ...,
        record_class: None = ...,
    ) -> List[_Record]: ...
    @overload
    async def fetch(
        self,
        query: str,
        *args: Any,
        timeout: Optional[float] = ...,
        record_class: Type[_OtherRecord],
    ) -> List[_OtherRecord]: ...
    @overload
    async def fetch(
        self,
        query: str,
        *args: Any,
        timeout: Optional[float] = ...,
        record_class: Optional[Type[_OtherRecord]],
    ) -> Union[List[_Record], List[_OtherRecord]]: ...
    @overload
    async def fetch(
        self,
        query: str,
        *args: Any,
        timeout: Optional[float] = ...,
        record_class: Optional[Type[_OtherRecord]] = ...,
    ) -> Union[List[_Record], List[_OtherRecord]]: ...
    async def fetchval(
        self, query: str, *args: Any, column: int = ..., timeout: Optional[float] = ...
    ) -> Optional[Any]: ...
    @overload
    async def fetchrow(
        self,
        query: str,
        *args: Any,
        timeout: Optional[float] = ...,
        record_class: None = ...,
    ) -> Optional[_Record]: ...
    @overload
    async def fetchrow(
        self,
        query: str,
        *args: Any,
        timeout: Optional[float] = ...,
        record_class: Type[_OtherRecord],
    ) -> Optional[_OtherRecord]: ...
    @overload
    async def fetchrow(
        self,
        query: str,
        *args: Any,
        timeout: Optional[float] = ...,
        record_class: Optional[Type[_OtherRecord]],
    ) -> Union[Optional[_Record], Optional[_OtherRecord]]: ...
    @overload
    async def fetchrow(
        self,
        query: str,
        *args: Any,
        timeout: Optional[float] = ...,
        record_class: Optional[Type[_OtherRecord]] = ...,
    ) -> Union[None, _Record, _OtherRecord]: ...
    async def copy_from_table(
        self,
        table_name: str,
        output: _OutputType,
        *,
        columns: Optional[Iterable[str]] = ...,
        schema_name: Optional[str] = ...,
        timeout: Optional[float] = ...,
        format: Optional[_CopyFormat] = ...,
        oids: Optional[int] = ...,
        delimiter: Optional[str] = ...,
        null: Optional[str] = ...,
        header: Optional[bool] = ...,
        quote: Optional[str] = ...,
        escape: Optional[str] = ...,
        force_quote: Optional[bool] = ...,
        encoding: Optional[str] = ...,
    ) -> str: ...
    async def copy_from_query(
        self,
        query: str,
        *args: Any,
        output: _OutputType,
        timeout: Optional[float] = ...,
        format: Optional[_CopyFormat] = ...,
        oids: Optional[int] = ...,
        delimiter: Optional[str] = ...,
        null: Optional[str] = ...,
        header: Optional[bool] = ...,
        quote: Optional[str] = ...,
        escape: Optional[str] = ...,
        force_quote: Optional[bool] = ...,
        encoding: Optional[str] = ...,
    ) -> str: ...
    async def copy_to_table(
        self,
        table_name: str,
        source: _SourceType,
        *,
        columns: Optional[Iterable[str]] = ...,
        schema_name: Optional[str] = ...,
        timeout: Optional[float] = ...,
        format: Optional[_CopyFormat] = ...,
        oids: Optional[int] = ...,
        freeze: Optional[bool] = ...,
        delimiter: Optional[str] = ...,
        null: Optional[str] = ...,
        header: Optional[bool] = ...,
        quote: Optional[str] = ...,
        escape: Optional[str] = ...,
        force_quote: Optional[bool] = ...,
        force_not_null: Optional[bool] = ...,
        force_null: Optional[bool] = ...,
        encoding: Optional[str] = ...,
    ) -> str: ...
    async def copy_records_to_table(
        self,
        table_name: str,
        records: Iterable[Sequence[Any]],
        *,
        columns: Optional[Iterable[str]] = ...,
        schema_name: Optional[str] = ...,
        timeout: Optional[float] = ...,
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
async def connect(
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
    connection_class: Type[Connection[_Record]] = ...,
    record_class: Type[_Record],
    server_settings: Optional[Dict[str, str]] = ...,
) -> Connection[_Record]: ...
@overload
async def connect(
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
    connection_class: Type[Connection[Record]] = ...,
    record_class: Type[Record] = ...,
    server_settings: Optional[Dict[str, str]] = ...,
) -> Connection[Record]: ...
@overload
async def connect(
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
    record_class: Type[_Record] = ...,
    server_settings: Optional[Dict[str, str]] = ...,
) -> _Connection: ...

class _ConnectionProxy(Generic[_Record]): ...

class ServerCapabilities(NamedTuple):
    advisory_locks: bool
    notifications: bool
    plpgsql: bool
    sql_reset: bool
    sql_close_all: bool
