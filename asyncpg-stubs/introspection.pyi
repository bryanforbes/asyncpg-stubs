from typing import Final

from . import protocol

_TYPEINFO_13: Final[str]
INTRO_LOOKUP_TYPES_13: Final[str]
_TYPEINFO: Final[str]
INTRO_LOOKUP_TYPES: Final[str]
TYPE_BY_NAME: Final[str]
TYPE_BY_OID: Final[str]
SCALAR_TYPE_KINDS: Final[tuple[bytes, bytes, bytes]]

def is_scalar_type(typeinfo: protocol.Record) -> bool: ...
def is_domain_type(typeinfo: protocol.Record) -> bool: ...
def is_composite_type(typeinfo: protocol.Record) -> bool: ...
