from asyncio import Protocol, WriteTransport
from ssl import SSLContext
from typing import Any, Dict, List, NamedTuple, Optional, Tuple, TypeVar, Union
from typing_extensions import Final, Literal

_Connection = TypeVar('_Connection')
_Protocol = TypeVar('_Protocol', bound=Protocol)

_TPTupleType = Tuple[WriteTransport, _Protocol]
_AddrType = Union[Tuple[str, int], str]
_SSLType = Union[SSLContext, Literal[True]]
_HostType = Union[List[str], str]
_PortType = Union[List[int], int]

PGPASSFILE: str

class _ConnectionParameters(NamedTuple):
    user: str
    password: Optional[str]
    database: str
    ssl: Optional[_SSLType]
    ssl_is_advisory: Optional[bool]
    connect_timeout: Optional[float]
    server_settings: Optional[Dict[str, str]]

class _ClientConfiguration(NamedTuple):
    command_timeout: Optional[float]
    statement_cache_size: int
    max_cached_statement_lifetime: int
    max_cacheable_statement_size: int
