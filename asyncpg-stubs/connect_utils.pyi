from _typeshed import Self
from asyncio import AbstractEventLoop, Future, Protocol, WriteTransport
from collections.abc import Awaitable, Callable
from enum import IntEnum
from ssl import SSLContext
from typing import NamedTuple, TypeVar
from typing_extensions import Final, Literal, TypeAlias

_AsyncProtocol = TypeVar('_AsyncProtocol', bound=Protocol)

_TPTupleType: TypeAlias = tuple[WriteTransport, _AsyncProtocol]
_AddrTupleType: TypeAlias = tuple[str, int]
_AddrType: TypeAlias = _AddrTupleType | str
_SSLStringValues: TypeAlias = Literal[
    'disable', 'prefer', 'allow', 'require', 'verify-ca', 'verify-full'
]
_ParsedSSLType: TypeAlias = SSLContext | Literal[False]
_SSLType: TypeAlias = _ParsedSSLType | _SSLStringValues | bool
_HostType: TypeAlias = list[str] | str
_PortListType: TypeAlias = list[int | str] | list[int] | list[str]
_PortType: TypeAlias = _PortListType | int | str
_PasswordType: TypeAlias = str | Callable[[], str] | Callable[[], Awaitable[str]]

PGPASSFILE: Final[str]

class SSLMode(IntEnum):
    disable: int
    allow: int
    prefer: int
    require: int
    verify_ca: int
    verify_full: int
    @classmethod
    def parse(cls: Self, sslmode: str | Self) -> Self: ...

class _ConnectionParameters(NamedTuple):
    user: str
    password: _PasswordType | None
    database: str
    ssl: _ParsedSSLType | None
    sslmode: SSLMode | None
    direct_tls: bool
    connect_timeout: float
    server_settings: dict[str, str] | None

class _ClientConfiguration(NamedTuple):
    command_timeout: float | None
    statement_cache_size: int
    max_cached_statement_lifetime: int
    max_cacheable_statement_size: int

class TLSUpgradeProto(Protocol):
    on_data: Future[bool]
    host: str
    port: int
    ssl_context: SSLContext
    ssl_is_advisory: bool | None
    def __init__(
        self,
        loop: AbstractEventLoop | None,
        host: str,
        port: int,
        ssl_context: SSLContext,
        ssl_is_advisory: bool | None,
    ) -> None: ...
    def data_received(self, data: bytes) -> None: ...
    def connection_lost(self, exc: Exception | None) -> None: ...
