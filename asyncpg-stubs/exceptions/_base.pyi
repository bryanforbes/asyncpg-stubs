import typing

__all__ = (
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
)

class PostgresMessageMeta(type): ...

class PostgresMessage(metaclass=PostgresMessageMeta):
    severity: typing.Optional[str]
    severity_en: typing.Optional[str]
    sqlstate: typing.ClassVar[str]
    message: str
    detail: typing.Optional[str]
    hint: typing.Optional[str]
    position: typing.Optional[str]
    internal_position: typing.Optional[str]
    internal_query: typing.Optional[str]
    context: typing.Optional[str]
    schema_name: typing.Optional[str]
    table_name: typing.Optional[str]
    column_name: typing.Optional[str]
    data_type_name: typing.Optional[str]
    constraint_name: typing.Optional[str]
    server_source_filename: typing.Optional[str]
    server_source_line: typing.Optional[str]
    server_source_function: typing.Optional[str]
    def as_dict(self) -> typing.Dict[str, str]: ...

class PostgresError(PostgresMessage, Exception):
    def __str__(self) -> str: ...
    @classmethod
    def new(
        cls, fields: typing.Dict[str, str], query: typing.Optional[str] = ...
    ) -> PostgresMessage: ...

class FatalPostgresError(PostgresError): ...
class UnknownPostgresError(FatalPostgresError): ...

class InterfaceMessage:
    def __init__(
        self, *, detail: typing.Optional[str] = ..., hint: typing.Optional[str] = ...
    ) -> None: ...
    def with_msg(self, msg: str) -> str: ...
    def __str__(self) -> str: ...

class InterfaceError(InterfaceMessage, Exception):
    def __init__(
        self,
        msg: str,
        *,
        detail: typing.Optional[str] = ...,
        hint: typing.Optional[str] = ...,
    ) -> None: ...

class DataError(InterfaceError, ValueError): ...
class UnsupportedClientFeatureError(InterfaceError): ...

class InterfaceWarning(InterfaceMessage, UserWarning):
    def __init__(
        self,
        msg: str,
        *,
        detail: typing.Optional[str] = ...,
        hint: typing.Optional[str] = ...,
    ) -> None: ...

class InternalClientError(Exception): ...
class ProtocolError(InternalClientError): ...

class OutdatedSchemaCacheError(InternalClientError):
    def __init__(
        self,
        msg: str,
        *,
        schema: typing.Optional[str] = ...,
        data_type: typing.Optional[str] = ...,
        position: typing.Optional[str] = ...,
    ) -> None: ...

class PostgresLogMessage(PostgresMessage):
    def __str__(self) -> str: ...
    @classmethod
    def new(
        cls, fields: typing.Dict[str, str], query: typing.Optional[str] = ...
    ) -> PostgresMessage: ...
