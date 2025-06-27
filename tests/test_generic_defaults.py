from __future__ import annotations

from typing import TYPE_CHECKING
from typing_extensions import assert_type

if TYPE_CHECKING:
    import asyncpg
    from asyncpg.cursor import Cursor
    from asyncpg.pool import Pool, PoolConnectionProxy
    from asyncpg.prepared_stmt import PreparedStatement


def main(
    connection: asyncpg.Connection,
    cursor: Cursor,
    pool_proxy: PoolConnectionProxy,
    pool: Pool,
    prepared_statement: PreparedStatement,
) -> None:
    assert_type(connection, 'asyncpg.Connection[asyncpg.Record]')
    assert_type(cursor, 'Cursor[asyncpg.Record]')
    assert_type(pool_proxy, 'PoolConnectionProxy[asyncpg.Record]')
    assert_type(pool, 'asyncpg.Pool[asyncpg.Record]')
    assert_type(prepared_statement, 'PreparedStatement[asyncpg.Record]')
