from typing import Any, Callable, TypeVar

from .connection import Connection

_Callable = TypeVar('_Callable', bound=Callable[..., Any])

def guarded(meth: _Callable) -> _Callable: ...

class ConnectionResource:
    def __init__(self, connection: Connection[Any]) -> None: ...
