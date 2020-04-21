from typing import Any, Tuple
from typing_extensions import TypedDict

INTRO_LOOKUP_TYPES: str
TYPE_BY_NAME: str
SCALAR_TYPE_KINDS: Tuple[bytes, bytes, bytes]

class _TypeInfoBase(TypedDict):
    kind: bytes
    elemtype: Any

class _TypeInfo(_TypeInfoBase, total=False): ...

def is_scalar_type(typeinfo: _TypeInfo) -> bool: ...
