# Copyright (C) 2016-present the asyncpg authors and contributors
# <see AUTHORS file>
#
# This module is part of asyncpg and is released under
# the Apache 2.0 License: http://www.apache.org/licenses/LICENSE-2.0

from typing import Final

from . import protocol

_TYPEINFO_13: Final[str] = ...

INTRO_LOOKUP_TYPES_13: Final[str] = ...

_TYPEINFO: Final[str] = ...

INTRO_LOOKUP_TYPES: Final[str] = ...

TYPE_BY_NAME: Final = ...

TYPE_BY_OID: Final[str] = ...

# 'b' for a base type, 'd' for a domain, 'e' for enum.
SCALAR_TYPE_KINDS: Final[tuple[bytes, bytes, bytes]] = ...

def is_scalar_type(typeinfo: protocol.Record) -> bool: ...
def is_domain_type(
    typeinfo: protocol.Record,
) -> bool: ...  # type: ignore[no-any-return]
def is_composite_type(
    typeinfo: protocol.Record,
) -> bool: ...  # type: ignore[no-any-return]
