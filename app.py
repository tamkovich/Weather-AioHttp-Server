from aiohttp import web

from backend.create_app import create_app
from routers.routers import routes

if __name__ == "__main__":
    app = create_app()
    app.add_routes(routes)
    web.run_app(app)
