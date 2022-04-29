from typing import Any

from . import connection

def _quote_ident(ident: str) -> str: ...
def _quote_literal(string: str) -> str: ...
async def _mogrify(
    conn: connection.Connection[Any],
    query: str,
    args: tuple[Any, ...],
) -> str: ...
