# -*- coding: utf-8 -*-
__author__ = 'florije'

import asyncio
import sqlalchemy as sa

from aiomysql.sa import create_engine

metadata = sa.MetaData()

tbl = sa.Table('tbl', metadata,
               sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
               sa.Column('val', sa.String(255)))


@asyncio.coroutine
def go():
    engine = yield from create_engine(user='root',
                                      db='test_pymysql',
                                      host='127.0.0.1',
                                      password='pass',
                                      autocommit=True)

    with (yield from engine) as conn:
        yield from conn.execute(tbl.insert().values(val='abc'))
        # yield from conn.execute(
        #     tbl.insert(),
        #     {"val": "v1", "id": 1}
        # )
        # yield from conn.execute('commit')
        res = yield from conn.execute(tbl.select())
        for row in res:
            print(row.id, row.val)


asyncio.get_event_loop().run_until_complete(go())
