from enum import Enum
from typing import Any, Final, Literal
from typing_extensions import TypeAlias

from . import connection as _connection, connresource

class TransactionState(Enum):
    NEW = 0
    STARTED = 1
    COMMITTED = 2
    ROLLEDBACK = 3
    FAILED = 4

_IsolationLevels: TypeAlias = Literal[
    'read_committed', 'read_uncommitted', 'serializable', 'repeatable_read'
]
ISOLATION_LEVELS: Final[set[_IsolationLevels]]
ISOLATION_LEVELS_BY_VALUE: Final[dict[str, _IsolationLevels]]

class Transaction(connresource.ConnectionResource):
    __slots__ = (
        '_connection',
        '_isolation',
        '_readonly',
        '_deferrable',
        '_state',
        '_nested',
        '_id',
        '_managed',
    )
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
