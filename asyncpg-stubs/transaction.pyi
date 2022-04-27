import enum
import typing
import typing_extensions

from . import connection as _connection, connresource

class TransactionState(enum.Enum):
    NEW: int
    STARTED: int
    COMMITTED: int
    ROLLEDBACK: int
    FAILED: int

IsolationLevels = typing_extensions.Literal[
    'read_committed', 'serializable', 'repeatable_read'
]
ISOLATION_LEVELS: typing_extensions.Final[typing.Set[IsolationLevels]]
ISOLATION_LEVELS_BY_VALUE: typing_extensions.Final[typing.Dict[str, IsolationLevels]]

class Transaction(connresource.ConnectionResource):
    __slots__: typing.Any
    _isolation: typing.Optional[IsolationLevels]
    _readonly: bool
    _deferrable: bool
    _state: TransactionState
    _nested: bool
    _id: typing.Optional[str]
    _managed: bool
    def __init__(
        self,
        connection: _connection.Connection[typing.Any],
        isolation: typing.Optional[IsolationLevels],
        readonly: bool,
        deferrable: bool,
    ) -> None: ...
    async def __aenter__(self) -> None: ...
    async def __aexit__(
        self, extype: typing.Any, ex: typing.Any, tb: typing.Any
    ) -> None: ...
    async def start(self) -> None: ...
    def __check_state_base(self, opname: str) -> None: ...
    def __check_state(self, opname: str) -> None: ...
    async def __commit(self) -> None: ...
    async def __rollback(self) -> None: ...
    async def commit(self) -> None: ...
    async def rollback(self) -> None: ...
    def __repr__(self) -> str: ...
