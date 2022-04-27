import typing

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

_V = typing.TypeVar('_V', bound=_RangeValue)

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

class Type(typing.NamedTuple):
    oid: int
    name: str
    kind: str
    schema: str

class Attribute(typing.NamedTuple):
    name: str
    type: Type

class ServerVersion(typing.NamedTuple):
    major: int
    minor: int
    micro: int
    releaselevel: str
    serial: int

class _RangeValue:
    def __eq__(self, other: object) -> bool: ...
    def __lt__(self, other: _RangeValue) -> bool: ...
    def __gt__(self, other: _RangeValue) -> bool: ...

class Range(typing.Generic[_V]):
    __slots__: typing.Any
    _lower: typing.Optional[_V]
    _upper: typing.Optional[_V]
    _lower_inc: bool
    _upper_inc: bool
    _empty: bool
    def __init__(
        self,
        lower: typing.Optional[_V] = ...,
        upper: typing.Optional[_V] = ...,
        *,
        lower_inc: bool = ...,
        upper_inc: bool = ...,
        empty: bool = ...,
    ) -> None: ...
    @property
    def lower(self) -> typing.Optional[_V]: ...
    @property
    def lower_inc(self) -> bool: ...
    @property
    def lower_inf(self) -> bool: ...
    @property
    def upper(self) -> typing.Optional[_V]: ...
    @property
    def upper_inc(self) -> bool: ...
    @property
    def upper_inf(self) -> bool: ...
    @property
    def isempty(self) -> bool: ...
    def _issubset_lower(self, other: Range[_V]) -> bool: ...
    def _issubset_upper(self, other: Range[_V]) -> bool: ...
    def issubset(self, other: Range[_V]) -> bool: ...
    def issuperset(self, other: Range[_V]) -> bool: ...
    def __bool__(self) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __repr__(self) -> str: ...
    __str__: typing.Callable[[Range[typing.Any]], str]
