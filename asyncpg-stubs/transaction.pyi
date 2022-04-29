from enum import Enum
from typing import Any
from typing_extensions import Final, Literal, TypeAlias

from . import connection as _connection, connresource

class TransactionState(Enum):
    NEW: int
    STARTED: int
    COMMITTED: int
    ROLLEDBACK: int
    FAILED: int

_IsolationLevels: TypeAlias = Literal[
    'read_committed', 'serializable', 'repeatable_read'
]
ISOLATION_LEVELS: Final[set[_IsolationLevels]]
ISOLATION_LEVELS_BY_VALUE: Final[dict[str, _IsolationLevels]]

class Transaction(connresource.ConnectionResource):
    __slots__: Any
    def __init__(
        self,
        connection: _connection.Connection[Any],
        isolation: _IsolationLevels | None,
        readonly: bool,
        deferrable: bool,
    ) -> None: ...
    async def __aenter__(self) -> None: ...
    async def __aexit__(self, extype: object, ex: object, tb: object) -> None: ...
    async def start(self) -> None: ...
    async def commit(self) -> None: ...
    async def rollback(self) -> None: ...
