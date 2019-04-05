import aiohttp_jinja2
import jinja2

from aiohttp import web


def create_app():
    app = web.Application()

    aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader("templates"))
    app["static_root_url"] = "/static"
    app.router.add_static("/static", "static", name="static")

    return app
