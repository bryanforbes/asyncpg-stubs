from asyncio import AbstractEventLoop, Future, Protocol
from collections.abc import Awaitable, Callable
from enum import Enum, IntEnum
from ssl import SSLContext
from typing import Any, Final, Literal, NamedTuple
from typing_extensions import Self, TypeAlias

from asyncpg import compat

from . import connection

_ParsedSSLType: TypeAlias = SSLContext | Literal[False]
_PasswordType: TypeAlias = str | Callable[[], str] | Callable[[], Awaitable[str]]

PGPASSFILE: Final[str]

class SSLMode(IntEnum):
    disable = 0
    allow = 1
    prefer = 2
    require = 3
    verify_ca = 4
    verify_full = 5
    @classmethod
    def parse(cls, sslmode: str | Self) -> Self: ...

class SSLNegotiation(compat.StrEnum):
    postgres = 'postgres'  # noqa: PYI052
    direct = 'direct'  # noqa: PYI052

class _ConnectionParameters(NamedTuple):
    user: str
    password: _PasswordType | None
    database: str
    ssl: _ParsedSSLType | None
    sslmode: SSLMode | None
    ssl_negotiation: SSLNegotiation
    server_settings: dict[str, str] | None
    target_session_attrs: SessionAttribute
    krbsrvname: str | None
    gsslib: connection._GSSLibType | None

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
    any = 'any'
    primary = 'primary'
    standby = 'standby'
    prefer_standby = 'prefer-standby'
    read_write = 'read-write'
    read_only = 'read-only'

target_attrs_check: Final[
    dict[SessionAttribute, Callable[[connection.Connection[Any]], Any]]
]
