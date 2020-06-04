from typing import Any, Tuple
from typing_extensions import TypedDict

from .protocol import Record

INTRO_LOOKUP_TYPES: str
TYPE_BY_NAME: str
SCALAR_TYPE_KINDS: Tuple[bytes, bytes, bytes]

def is_scalar_type(typeinfo: Record) -> bool: ...
