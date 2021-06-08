from asyncio import AbstractEventLoop, Protocol, WriteTransport
from enum import IntEnum
from ssl import SSLContext
from typing import Any, Dict, List, NamedTuple, Optional, Tuple, Type, TypeVar, Union
from typing_extensions import Final, Literal

_Connection = TypeVar('_Connection')
_Protocol = TypeVar('_Protocol', bound=Protocol)
_SSLMode = TypeVar('_SSLMode', bound=SSLMode)

_TPTupleType = Tuple[WriteTransport, _Protocol]
_AddrType = Union[Tuple[str, int], str]
_HostType = Union[List[str], str]
_PortType = Union[List[int], int]
_ParsedSSLType = Union[SSLContext, Literal[False]]
_SSLStringValues = Literal[
    'disable', 'prefer', 'allow', 'require', 'verify-ca', 'verify-full'
]
_SSLType = Union[_ParsedSSLType, _SSLStringValues, bool]

PGPASSFILE: Final[str]

class SSLMode(IntEnum):
    disable: int
    allow: int
    prefer: int
    require: int
    verify_ca: int
    verify_full: int
    @classmethod
    def parse(cls: Type[_SSLMode], sslmode: Union[str, _SSLMode]) -> _SSLMode: ...

class _ConnectionParameters(NamedTuple):
    user: str
    password: Optional[str]
    database: str
    ssl: Optional[_ParsedSSLType]
    sslmode: Optional[SSLMode]
    connect_timeout: Optional[float]
    server_settings: Optional[Dict[str, str]]

class _ClientConfiguration(NamedTuple):
    command_timeout: Optional[float]
    statement_cache_size: int
    max_cached_statement_lifetime: int
    max_cacheable_statement_size: int

class TLSUpgradeProto(Protocol):
    on_data: Any = ...
    host: Any = ...
    port: Any = ...
    ssl_context: Any = ...
    ssl_is_advisory: Any = ...
    def __init__(
        self,
        loop: Optional[AbstractEventLoop],
        host: str,
        port: int,
        ssl_context: SSLContext,
        ssl_is_advisory: Optional[bool],
    ) -> None: ...
    def data_received(self, data: bytes) -> None: ...
    def connection_lost(self, exc: Optional[Exception]) -> None: ...
