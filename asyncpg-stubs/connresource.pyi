from typing import Any, Callable, Generic, TypeVar

from .connection import Connection

_F = TypeVar('_F', bound=Callable[..., Any])

def guarded(meth: _F) -> _F: ...

_C = TypeVar('_C', bound=Connection)

class ConnectionResource(Generic[_C]):
    def __init__(self, connection: _C) -> None: ...
