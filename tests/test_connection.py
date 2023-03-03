from __future__ import annotations

from typing_extensions import assert_type

import asyncpg
from asyncpg.cursor import Cursor
from asyncpg.prepared_stmt import PreparedStatement


class MyRecord(asyncpg.Record):
    ...


class MyOtherRecord(asyncpg.Record):
    ...


class MyConnection(asyncpg.Connection[MyOtherRecord]):
    ...


async def main(record_class: type[MyRecord] | None) -> None:
    assert_type(await asyncpg.connect(), asyncpg.Connection[asyncpg.Record])
    assert_type(
        await asyncpg.connect(record_class=MyRecord), asyncpg.Connection[MyRecord]
    )
    assert_type(await asyncpg.connect(connection_class=MyConnection), MyConnection)

    conn = await asyncpg.connect()

    assert_type(await conn.cursor(''), Cursor[asyncpg.Record])
    assert_type(
        await conn.cursor('', record_class=None, prefetch=None, timeout=None),
        Cursor[asyncpg.Record],
    )
    assert_type(
        await conn.cursor('', record_class=MyRecord, prefetch=1, timeout=2.2),
        Cursor[MyRecord],
    )
    assert_type(
        await conn.cursor('', record_class=record_class),
        'Cursor[asyncpg.Record] | Cursor[MyRecord]',
    )

    assert_type(await conn.prepare(''), PreparedStatement[asyncpg.Record])
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
    assert_type(await conn.fetchrow('', record_class=None), 'asyncpg.Record | None')
    assert_type(await conn.fetchrow('', record_class=MyRecord), 'MyRecord | None')
    assert_type(
        await conn.fetchrow('', record_class=record_class),
        'asyncpg.Record | MyRecord | None',
    )

    myrecord_connection = await asyncpg.connect(record_class=MyRecord)
    assert_type(
        await myrecord_connection.cursor('', record_class=MyOtherRecord),
        Cursor[MyOtherRecord],
    )
