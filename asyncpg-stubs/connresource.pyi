from collections.abc import Callable
from typing import Any, TypeVar

from . import connection

_Callable = TypeVar('_Callable', bound=Callable[..., Any])

def guarded(meth: _Callable) -> _Callable: ...

class ConnectionResource:
    __slots__ = ('_connection', '_con_release_ctr')
    def __init__(self, connection: connection.Connection[Any]) -> None: ...
