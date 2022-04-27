import asyncio
import enum
import pathlib
import ssl as ssl_module
import typing
import typing_extensions

from . import connection, protocol

_Connection = typing.TypeVar('_Connection', bound='connection.Connection[typing.Any]')
_Protocol = typing.TypeVar('_Protocol', bound='protocol.Protocol[typing.Any]')
_AsyncProtocol = typing.TypeVar('_AsyncProtocol', bound='asyncio.protocols.Protocol')
_Record = typing.TypeVar('_Record', bound=protocol.Record)
_SSLMode = typing.TypeVar('_SSLMode', bound='SSLMode')

_TPTupleType = typing.Tuple[asyncio.WriteTransport, _AsyncProtocol]
AddrType = typing.Union[typing.Tuple[str, int], str]
SSLStringValues = typing_extensions.Literal[
    'disable', 'prefer', 'allow', 'require', 'verify-ca', 'verify-full'
]
_ParsedSSLType = typing.Union[ssl_module.SSLContext, typing_extensions.Literal[False]]
SSLType = typing.Union[_ParsedSSLType, SSLStringValues, bool]
HostType = typing.Union[typing.List[str], str]
PortType = typing.Union[typing.List[int], int]

class SSLMode(enum.IntEnum):
    disable: int
    allow: int
    prefer: int
    require: int
    verify_ca: int
    verify_full: int
    @classmethod
    def parse(cls, sslmode: typing.Union[str, _SSLMode]) -> _SSLMode: ...

class _ConnectionParameters(typing.NamedTuple):
    user: str
    password: typing.Union[
        str, typing.Callable[[], str], typing.Callable[[], typing.Awaitable[str]], None
    ]
    database: str
    ssl: typing.Optional[_ParsedSSLType]
    sslmode: typing.Optional[SSLMode]
    connect_timeout: float
    server_settings: typing.Optional[typing.Dict[str, str]]

class _ClientConfiguration(typing.NamedTuple):
    command_timeout: typing.Optional[float]
    statement_cache_size: int
    max_cached_statement_lifetime: int
    max_cacheable_statement_size: int

PGPASSFILE: typing_extensions.Final[str]

def _read_password_file(
    passfile: pathlib.Path,
) -> typing.List[typing.Tuple[str, ...]]: ...
def _read_password_from_pgpass(
    passfile: pathlib.Path,
    hosts: typing.List[str],
    ports: typing.List[int],
    database: str,
    user: str,
) -> typing.Optional[str]: ...
def _validate_port_spec(
    hosts: typing.List[str], port: PortType
) -> typing.List[int]: ...
def _parse_hostlist(
    hostlist: str, port: typing.Optional[PortType], *, unquote: bool = ...
) -> typing.Tuple[typing.List[str], typing.List[int]]: ...
def _parse_tls_version(tls_version: str) -> ssl_module.TLSVersion: ...
def _dot_postgresql_path(filename: str) -> pathlib.Path: ...
def _parse_connect_dsn_and_args(
    dsn: typing.Optional[str],
    host: typing.Optional[HostType],
    port: typing.Optional[PortType],
    user: typing.Optional[str],
    password: typing.Optional[str],
    passfile: typing.Optional[str],
    database: typing.Optional[str],
    ssl: typing.Optional[SSLType],
    connect_timeout: float,
    server_settings: typing.Optional[typing.Dict[str, str]],
) -> typing.Tuple[
    typing.List[typing.Union[typing.Tuple[str, int], str]], _ConnectionParameters
]: ...
def _parse_connect_arguments(
    dsn: typing.Optional[str],
    host: typing.Optional[HostType],
    port: typing.Optional[PortType],
    user: typing.Optional[str],
    password: typing.Optional[str],
    passfile: typing.Optional[str],
    database: typing.Optional[str],
    timeout: float,
    command_timeout: typing.Optional[typing.Union[float, typing.SupportsFloat]],
    statement_cache_size: int,
    max_cached_statement_lifetime: int,
    max_cacheable_statement_size: int,
    ssl: typing.Optional[SSLType],
    server_settings: typing.Optional[typing.Dict[str, str]],
) -> typing.Tuple[
    typing.List[AddrType], _ConnectionParameters, _ClientConfiguration
]: ...

class TLSUpgradeProto(asyncio.Protocol):
    on_data: asyncio.Future[bool]
    host: str
    port: int
    ssl_context: ssl_module.SSLContext
    ssl_is_advisory: typing.Optional[bool]
    def __init__(
        self,
        loop: typing.Optional[asyncio.AbstractEventLoop],
        host: str,
        port: int,
        ssl_context: ssl_module.SSLContext,
        ssl_is_advisory: typing.Optional[bool],
    ) -> None: ...
    def data_received(self, data: bytes) -> None: ...
    def connection_lost(self, exc: typing.Optional[Exception]) -> None: ...

@typing.overload
async def _create_ssl_connection(
    protocol_factory: typing.Callable[[], _Protocol],
    host: str,
    port: int,
    loop: asyncio.AbstractEventLoop,
    ssl_context: ssl_module.SSLContext,
    *,
    ssl_is_advisory: typing.Optional[bool] = ...,
) -> _TPTupleType[_Protocol]: ...
@typing.overload
async def _create_ssl_connection(
    protocol_factory: typing.Callable[[], '_CancelProto'],
    host: str,
    port: int,
    loop: asyncio.AbstractEventLoop,
    ssl_context: ssl_module.SSLContext,
    *,
    ssl_is_advisory: typing.Optional[bool] = ...,
) -> _TPTupleType['_CancelProto']: ...
async def _connect_addr(
    addr: AddrType,
    loop: asyncio.AbstractEventLoop,
    timeout: float,
    params: _ConnectionParameters,
    config: _ClientConfiguration,
    connection_class: typing.Type[_Connection],
    record_class: typing.Type[_Record],
) -> _Connection: ...

class _RetryConnectSignal(Exception): ...

async def __connect_addr(
    params: _ConnectionParameters,
    timeout: float,
    retry: bool,
    addr: AddrType,
    loop: asyncio.AbstractEventLoop,
    config: _ClientConfiguration,
    connection_class: typing.Type[_Connection],
    record_class: typing.Type[_Record],
    params_input: _ConnectionParameters,
) -> _Connection: ...
async def _connect(
    loop: typing.Optional[asyncio.AbstractEventLoop],
    timeout: float,
    connection_class: typing.Type[_Connection],
    record_class: typing.Type[_Record],
    **kwargs: typing.Any,
) -> _Connection: ...

class _CancelProto(asyncio.Protocol):
    on_disconnect: typing.Any
    is_ssl: bool
    def __init__(self, loop: asyncio.AbstractEventLoop) -> None: ...
    def connection_lost(self, exc: typing.Optional[Exception]) -> None: ...

async def _cancel(
    loop: asyncio.AbstractEventLoop,
    addr: typing.Union[typing.Tuple[str, int], str],
    params: _ConnectionParameters,
    backend_pid: int,
    backend_secret: str,
) -> None: ...
def _get_socket(transport: asyncio.BaseTransport) -> typing.Any: ...
def _set_nodelay(sock: typing.Any) -> None: ...
def _create_future(
    loop: typing.Optional[asyncio.AbstractEventLoop],
) -> asyncio.Future[typing.Any]: ...
