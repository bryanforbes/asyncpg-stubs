from __future__ import annotations

from typing_extensions import assert_type

import asyncpg
from asyncpg.cursor import Cursor
from asyncpg.pool import PoolConnectionProxy
from asyncpg.prepared_stmt import PreparedStatement


class MyRecord(asyncpg.Record):
    ...


class MyOtherRecord(asyncpg.Record):
    ...


async def main(record_class: type[MyRecord] | None) -> None:
    pool = await asyncpg.create_pool()
    assert_type(pool, 'asyncpg.Pool[asyncpg.Record] | None')
    assert pool is not None
    assert_type(await pool, 'asyncpg.Pool[asyncpg.Record] | None')

    assert_type(
        await asyncpg.create_pool(record_class=MyRecord),
        'asyncpg.Pool[MyRecord] | None',
    )

    async with asyncpg.create_pool() as record_pool:
        assert_type(record_pool, asyncpg.Pool[asyncpg.Record])

        assert_type(await record_pool.fetch(''), 'list[asyncpg.Record]')
        assert_type(
            await record_pool.fetch('', record_class=None), 'list[asyncpg.Record]'
        )
        assert_type(
            await record_pool.fetch('', record_class=MyRecord), 'list[MyRecord]'
        )
        assert_type(
            await record_pool.fetch('', record_class=record_class),
            'list[MyRecord] | list[asyncpg.Record]',
        )

        assert_type(await record_pool.fetchrow(''), 'asyncpg.Record| None')
        assert_type(
            await record_pool.fetchrow('', record_class=None), 'asyncpg.Record | None'
        )
        assert_type(
            await record_pool.fetchrow('', record_class=MyRecord), 'MyRecord | None'
        )
        assert_type(
            await record_pool.fetchrow('', record_class=record_class),
            'MyRecord | asyncpg.Record | None',
        )

        async with record_pool.acquire() as conn:
            assert_type(conn, PoolConnectionProxy[asyncpg.Record])

            assert_type(
                await conn.cursor('', prefetch=1, timeout=2.2), Cursor[asyncpg.Record]
            )
            assert_type(
                await conn.cursor('', prefetch=None, timeout=None),
                Cursor[asyncpg.Record],
            )
            assert_type(
                await conn.cursor('', record_class=None), Cursor[asyncpg.Record]
            )
            assert_type(await conn.cursor('', record_class=MyRecord), Cursor[MyRecord])
            assert_type(
                await conn.cursor('', record_class=record_class),
                'Cursor[asyncpg.Record] | Cursor[MyRecord]',
            )

            assert_type(
                await conn.prepare(''),
                PreparedStatement[asyncpg.Record],
            )
            assert_type(
                await conn.prepare('', record_class=None),
                PreparedStatement[asyncpg.Record],
            )
            assert_type(
                await conn.prepare('', record_class=MyRecord),
                PreparedStatement[MyRecord],
            )
            assert_type(
                await conn.prepare('', record_class=record_class),
                'PreparedStatement[asyncpg.Record] | PreparedStatement[MyRecord]',
            )

            assert_type(await conn.fetch(''), 'list[asyncpg.Record]')
            assert_type(await conn.fetch('', record_class=None), 'list[asyncpg.Record]')
            assert_type(await conn.fetch('', record_class=MyRecord), 'list[MyRecord]')
            assert_type(
                await conn.fetch('', record_class=record_class),
                'list[asyncpg.Record] | list[MyRecord]',
            )

            assert_type(await conn.fetchrow(''), 'asyncpg.Record | None')
            assert_type(
                await conn.fetchrow('', record_class=None), 'asyncpg.Record | None'
            )
            assert_type(
                await conn.fetchrow('', record_class=MyRecord), 'MyRecord | None'
            )
            assert_type(
                await conn.fetchrow('', record_class=record_class),
                'asyncpg.Record | MyRecord | None',
            )

    async with asyncpg.create_pool(record_class=MyRecord) as myrecord_pool:
        assert_type(myrecord_pool, asyncpg.Pool[MyRecord])

        assert_type(
            await myrecord_pool.fetch('', record_class=MyOtherRecord),
            'list[MyOtherRecord]',
        )

        async with myrecord_pool.acquire() as conn:
            assert_type(conn, PoolConnectionProxy[MyRecord])
            assert_type(
                await conn.cursor('', record_class=MyOtherRecord), Cursor[MyOtherRecord]
            )
