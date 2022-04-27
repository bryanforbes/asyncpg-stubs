import typing

from . import connection

_Callable = typing.TypeVar('_Callable', bound=typing.Callable[..., typing.Any])

def guarded(meth: _Callable) -> _Callable: ...

class ConnectionResource:
    __slots__: typing.Any
    _connection: connection.Connection[typing.Any]
    _con_release_ctr: int
    def __init__(self, connection: connection.Connection[typing.Any]) -> None: ...
    def _check_conn_validity(self, meth_name: str) -> None: ...
