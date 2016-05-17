# -*- coding: utf-8 -*-
__author__ = 'florije'

import asyncio
from aiomysql import create_pool

loop = asyncio.get_event_loop()


async def go():
    async with create_pool(host='127.0.0.1', port=3306,
                           user='root', password='pass',
                           db='mysql', loop=loop, autocommit=True) as pool:
        async with pool.get() as conn:
            async with conn.cursor() as cur:
                await cur.execute("SELECT 42;")
                value = await cur.fetchone()
                print(value)


loop.run_until_complete(go())
