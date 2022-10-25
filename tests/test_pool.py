from __future__ import annotations

from typing_extensions import assert_type

import asyncpg


async def main() -> None:
    pool = await asyncpg.create_pool()
    assert_type(pool, 'asyncpg.Pool[asyncpg.Record] | None')
    assert pool is not None
    assert_type(await pool, 'asyncpg.Pool[asyncpg.Record] | None')

    async with asyncpg.create_pool() as pool:
        assert_type(pool, asyncpg.Pool[asyncpg.Record])
