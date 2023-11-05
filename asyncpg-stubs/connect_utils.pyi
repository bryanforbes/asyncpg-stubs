from asyncio import AbstractEventLoop, Future, Protocol
from collections.abc import Awaitable, Callable
from enum import Enum, IntEnum
from ssl import SSLContext
from typing import Any, Final, Literal, NamedTuple
from typing_extensions import Self, TypeAlias

from . import connection

_ParsedSSLType: TypeAlias = SSLContext | Literal[False]
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
    def parse(cls, sslmode: str | Self) -> Self: ...

class _ConnectionParameters(NamedTuple):
    user: str
    password: _PasswordType | None
    database: str
    ssl: _ParsedSSLType | None
    sslmode: SSLMode | None
    direct_tls: bool
    server_settings: dict[str, str] | None
    target_session_attrs: SessionAttribute

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

class SessionAttribute(str, Enum):
    any: str
    primary: str
    standby: str
    prefer_standby: str
    read_write: str
    read_only: str

target_attrs_check: Final[
    dict[SessionAttribute, Callable[[connection.Connection[Any]], Any]]
]
