import typing

from . import connection

def _quote_ident(ident: str) -> str: ...
def _quote_literal(string: str) -> str: ...
async def _mogrify(
    conn: connection.Connection[typing.Any],
    query: str,
    args: typing.Tuple[typing.Any, ...],
) -> str: ...
