from __future__ import annotations

from typing_extensions import assert_type

from asyncpg import Connection, Pool, Record


async def test_connection(conn: Connection[Record]) -> None:
    prepared_stmt = await conn.prepare('SELECT $1, $2, $3')

    assert_type(
        await prepared_stmt.fetchmany(
            [
                (1, 2, 3),
                (4, 5, 6),
            ]
        ),
        list[Record],
    )
    assert_type(
        await prepared_stmt.executemany(
            [
                (1, 2, 3),
                (4, 5, 6),
            ]
        ),
        None,
    )


async def test_pool(pool: Pool[Record]) -> None:
    async with pool.acquire() as conn:
        prepared_stmt = await conn.prepare('SELECT $1, $2, $3')

        assert_type(
            await prepared_stmt.fetchmany(
                [
                    (1, 2, 3),
                    (4, 5, 6),
                ]
            ),
            list[Record],
        )
        assert_type(
            await prepared_stmt.executemany(
                [
                    (1, 2, 3),
                    (4, 5, 6),
                ]
            ),
            None,
        )
