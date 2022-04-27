import typing
import typing_extensions

from . import protocol

_TYPEINFO_13: typing_extensions.Final[str]
INTRO_LOOKUP_TYPES_13: typing_extensions.Final[str]
_TYPEINFO: typing_extensions.Final[str]
INTRO_LOOKUP_TYPES: typing_extensions.Final[str]
TYPE_BY_NAME: typing_extensions.Final[str]
TYPE_BY_OID: typing_extensions.Final[str]
SCALAR_TYPE_KINDS: typing_extensions.Final[typing.Tuple[bytes, bytes, bytes]]

def is_scalar_type(typeinfo: protocol.Record) -> bool: ...
def is_domain_type(typeinfo: protocol.Record) -> bool: ...
