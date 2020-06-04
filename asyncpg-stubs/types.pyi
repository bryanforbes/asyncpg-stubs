from typing import (
    Any,
    Generic,
    Hashable,
    Iterable,
    Iterator,
    NamedTuple,
    Optional,
    Sequence,
    Sized,
    Tuple,
    TypeVar,
)

from asyncpg.pgproto.types import BitString as BitString
from asyncpg.pgproto.types import Box as Box
from asyncpg.pgproto.types import Circle as Circle
from asyncpg.pgproto.types import Line as Line
from asyncpg.pgproto.types import LineSegment as LineSegment
from asyncpg.pgproto.types import Path as Path
from asyncpg.pgproto.types import Point as Point
from asyncpg.pgproto.types import Polygon as Polygon

_T = TypeVar('_T')

class Type(NamedTuple):
    oid: int
    name: str
    kind: str
    schema: str

class Attribute(NamedTuple):
    name: str
    type: Type

class ServerVersion(NamedTuple):
    major: int
    minor: int
    micro: int
    releaselevel: str
    serial: int

class Range(Generic[_T]):
    def __init__(
        self,
        lower: Optional[_T] = ...,
        upper: Optional[_T] = ...,
        *,
        lower_inc: bool = ...,
        upper_inc: bool = ...,
        empty: bool = ...,
    ) -> None: ...
    @property
    def lower(self) -> Optional[_T]: ...
    @property
    def lower_inc(self) -> bool: ...
    @property
    def lower_inf(self) -> bool: ...
    @property
    def upper(self) -> Optional[_T]: ...
    @property
    def upper_inc(self) -> bool: ...
    @property
    def upper_inf(self) -> bool: ...
    @property
    def isempty(self) -> bool: ...
    def __bool__(self) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
