import typing

__all__ = [
    'PostgresError',
    'FatalPostgresError',
    'UnknownPostgresError',
    'InterfaceError',
    'InterfaceWarning',
    'PostgresLogMessage',
    'InternalClientError',
    'OutdatedSchemaCacheError',
    'ProtocolError',
    'UnsupportedClientFeatureError',
]

_PM = typing.TypeVar('_PM', bound=PostgresMessage)
_PE = typing.TypeVar('_PE', bound=PostgresError)
_IE = typing.TypeVar('_IE', bound=InterfaceError)

class PostgresMessageMeta(type): ...

class PostgresMessage(metaclass=PostgresMessageMeta):
    severity: str | None
    severity_en: str | None
    sqlstate: typing.ClassVar[str]
    message: str
    detail: str | None
    hint: str | None
    position: str | None
    internal_position: str | None
    internal_query: str | None
    context: str | None
    schema_name: str | None
    table_name: str | None
    column_name: str | None
    data_type_name: str | None
    constraint_name: str | None
    server_source_filename: str | None
    server_source_line: str | None
    server_source_function: str | None
    @classmethod
    def _make_constructor(
        cls: type[_PM], fields: dict[str, str], query: str | None = ...
    ) -> tuple[type[_PM], str, dict[str, str]]: ...
    def as_dict(self) -> dict[str, str]: ...

class PostgresError(PostgresMessage, Exception):
    def __str__(self) -> str: ...
    @classmethod
    def new(cls: type[_PE], fields: dict[str, str], query: str | None = ...) -> _PE: ...

class FatalPostgresError(PostgresError): ...
class UnknownPostgresError(FatalPostgresError): ...

class InterfaceMessage:
    args: tuple[typing.Any, ...]
    detail: str | None
    hint: str | None
    def __init__(self, *, detail: str | None = ..., hint: str | None = ...) -> None: ...
    def __str__(self) -> str: ...

class InterfaceError(InterfaceMessage, Exception):
    def __init__(
        self,
        msg: str,
        *,
        detail: str | None = ...,
        hint: str | None = ...,
    ) -> None: ...
    def with_msg(self: _IE, msg: str) -> _IE: ...

class DataError(InterfaceError, ValueError): ...
class UnsupportedClientFeatureError(InterfaceError): ...

class InterfaceWarning(InterfaceMessage, UserWarning):
    def __init__(
        self,
        msg: str,
        *,
        detail: str | None = ...,
        hint: str | None = ...,
    ) -> None: ...

class InternalClientError(Exception): ...
class ProtocolError(InternalClientError): ...

class OutdatedSchemaCacheError(InternalClientError):
    schema_name: str | None
    data_type_name: str | None
    position: str | None
    def __init__(
        self,
        msg: str,
        *,
        schema: str | None = ...,
        data_type: str | None = ...,
        position: str | None = ...,
    ) -> None: ...

class PostgresLogMessage(PostgresMessage):
    def __str__(self) -> str: ...
    def __setattr__(self, name: str, val: typing.Any) -> None: ...
    @classmethod
    def new(
        cls, fields: dict[str, str], query: str | None = ...
    ) -> PostgresMessage: ...
