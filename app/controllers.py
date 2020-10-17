from aiohttp import web

import db


async def employee(request):
    async with request.app['db'].acquire() as conn:
        cursor = await conn.execute(db.employee.select())
        records = await cursor.fetchall()
        employees = [dict(q) for q in records]
        return web.Response(text=str(employees))
