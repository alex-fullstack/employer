from aiohttp import web
from settings import config

from db import init_pg, close_pg

from controllers import employee


async def index(request):
    return web.Response(text="Welcome home!")


async def get_web_app():
    app = web.Application()
    app['config'] = config
    app.router.add_get('/', employee)
    app.on_startup.append(init_pg)
    app.on_cleanup.append(close_pg)
    return app

