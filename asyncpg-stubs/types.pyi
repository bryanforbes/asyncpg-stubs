from typing import Generic, NamedTuple, Protocol, TypeVar
from typing_extensions import Self

from asyncpg.pgproto.types import (
    BitString,
    Box,
    Circle,
    Line,
    LineSegment,
    Path,
    Point,
    Polygon,
)

__all__ = (
    'Type',
    'Attribute',
    'Range',
    'BitString',
    'Point',
    'Path',
    'Polygon',
    'Box',
    'Line',
    'LineSegment',
    'Circle',
    'ServerVersion',
)

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

class _RangeValue(Protocol):
    def __eq__(self, value: object, /) -> bool: ...
    def __lt__(self, __other: Self, /) -> bool: ...
    def __gt__(self, __other: Self, /) -> bool: ...

_RV = TypeVar('_RV', bound=_RangeValue)

class Range(Generic[_RV]):
    __slots__ = '_lower', '_upper', '_lower_inc', '_upper_inc', '_empty'

    _lower: _RV | None
    _upper: _RV | None
    _lower_inc: bool
    _upper_inc: bool
    _empty: bool

    def __init__(
        self,
        lower: _RV | None = None,
        upper: _RV | None = None,
        *,
        lower_inc: bool = True,
        upper_inc: bool = False,
        empty: bool = False,
    ) -> None: ...
    @property
    def lower(self) -> _RV | None: ...
    @property
    def lower_inc(self) -> bool: ...
    @property
    def lower_inf(self) -> bool: ...
    @property
    def upper(self) -> _RV | None: ...
    @property
    def upper_inc(self) -> bool: ...
    @property
    def upper_inf(self) -> bool: ...
    @property
    def isempty(self) -> bool: ...
    def issubset(self, other: Self) -> bool: ...
    def issuperset(self, other: Self) -> bool: ...
    def __bool__(self) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
