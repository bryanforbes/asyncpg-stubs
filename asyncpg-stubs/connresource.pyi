from typing import Any, Callable, TypeVar

from .connection import Connection

_F = TypeVar('_F', bound=Callable[..., Any])

def guarded(meth: _F) -> _F: ...

class ConnectionResource:
    def __init__(self, connection: Connection) -> None: ...
