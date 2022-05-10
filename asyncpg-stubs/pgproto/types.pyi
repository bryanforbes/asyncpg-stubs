import builtins
from _typeshed import Self
from collections.abc import Iterator, Sequence
from typing import Any, SupportsFloat, overload
from typing_extensions import Literal, SupportsIndex, TypeAlias

__all__ = (
    'BitString',
    'Point',
    'Path',
    'Polygon',
    'Box',
    'Line',
    'LineSegment',
    'Circle',
)

_BitOrderType: TypeAlias = Literal['big', 'little']

class BitString:
    __slots__: Any
    def __init__(self, bitstring: builtins.bytes | None = ...) -> None: ...
    @classmethod
    def frombytes(
        cls: type[Self],
        bytes_: builtins.bytes | None = ...,
        bitlength: int | None = ...,
    ) -> Self: ...
    @property
    def bytes(self) -> builtins.bytes: ...
    def as_string(self) -> str: ...
    def to_int(self, bitorder: _BitOrderType = ..., *, signed: bool = ...) -> int: ...
    @classmethod
    def from_int(
        cls: type[Self],
        x: int,
        length: int,
        bitorder: _BitOrderType = ...,
        *,
        signed: bool = ...,
    ) -> Self: ...
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __getitem__(self, i: int) -> int: ...
    def __len__(self) -> int: ...

class Point(tuple[float, float]):
    def __new__(
        cls: type[Self],
        x: SupportsFloat | SupportsIndex | str | builtins.bytes | builtins.bytearray,
        y: SupportsFloat | SupportsIndex | str | builtins.bytes | builtins.bytearray,
    ) -> Self: ...
    @property
    def x(self) -> float: ...
    @property
    def y(self) -> float: ...

class Box(tuple[Point, Point]):
    __slots__: Any
    def __new__(
        cls: type[Self], high: Sequence[float], low: Sequence[float]
    ) -> Self: ...
    @property
    def high(self) -> Point: ...
    @property
    def low(self) -> Point: ...

class Line(tuple[float, float, float]):
    __slots__: Any
    def __new__(cls: type[Self], A: float, B: float, C: float) -> Self: ...
    @property
    def A(self) -> float: ...
    @property
    def B(self) -> float: ...
    @property
    def C(self) -> float: ...

class LineSegment(tuple[Point, Point]):
    def __new__(cls: type[Self], p1: Sequence[float], p2: Sequence[float]) -> Self: ...
    @property
    def p1(self) -> Point: ...
    @property
    def p2(self) -> Point: ...

class Path:
    __slots__: Any
    points: tuple[Point, ...]
    def __init__(self, *points: Sequence[float], is_closed: bool = ...) -> None: ...
    @property
    def is_closed(self) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __iter__(self) -> Iterator[Point]: ...
    def __len__(self) -> int: ...
    @overload
    def __getitem__(self, i: int) -> Point: ...
    @overload
    def __getitem__(self, i: slice) -> tuple[Point, ...]: ...
    def __contains__(self, point: object) -> bool: ...

class Polygon(Path):
    __slots__: Any
    def __init__(self, *points: Sequence[float]) -> None: ...

class Circle(tuple[Point, float]):
    __slots__: Any
    def __new__(cls: type[Self], center: Point, radius: float) -> Self: ...
    @property
    def center(self) -> Point: ...
    @property
    def radius(self) -> float: ...
