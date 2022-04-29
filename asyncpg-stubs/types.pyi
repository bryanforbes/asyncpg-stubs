from typing import Any, Generic, NamedTuple, TypeVar

from asyncpg.pgproto.types import (
    BitString as BitString,
    Box as Box,
    Circle as Circle,
    Line as Line,
    LineSegment as LineSegment,
    Path as Path,
    Point as Point,
    Polygon as Polygon,
)

_V = TypeVar('_V', bound=_RangeValue)

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

class _RangeValue:
    def __eq__(self, other: object) -> bool: ...
    def __lt__(self, other: _RangeValue) -> bool: ...
    def __gt__(self, other: _RangeValue) -> bool: ...

class Range(Generic[_V]):
    __slots__: Any
    def __init__(
        self,
        lower: _V | None = ...,
        upper: _V | None = ...,
        *,
        lower_inc: bool = ...,
        upper_inc: bool = ...,
        empty: bool = ...,
    ) -> None: ...
    @property
    def lower(self) -> _V | None: ...
    @property
    def lower_inc(self) -> bool: ...
    @property
    def lower_inf(self) -> bool: ...
    @property
    def upper(self) -> _V | None: ...
    @property
    def upper_inc(self) -> bool: ...
    @property
    def upper_inf(self) -> bool: ...
    @property
    def isempty(self) -> bool: ...
    def issubset(self, other: Range[_V]) -> bool: ...
    def issuperset(self, other: Range[_V]) -> bool: ...
    def __bool__(self) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
