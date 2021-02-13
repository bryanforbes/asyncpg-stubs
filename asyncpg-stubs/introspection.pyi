from typing import Any, Tuple
from typing_extensions import Final, TypedDict

from .protocol import Record

INTRO_LOOKUP_TYPES: Final[str]
TYPE_BY_NAME: Final[str]
TYPE_BY_OID: Final[str]
SCALAR_TYPE_KINDS: Final[Tuple[bytes, bytes, bytes]]

def is_scalar_type(typeinfo: Record) -> bool: ...
def is_domain_type(typeinfo: Record) -> bool: ...
