import aiohttp_jinja2

from aiohttp import web
from aiohttp.web import json_response

from config import config
from exceptions.service.exceptions import WrongLocationError
from logger.create_logger import create_logger
from service.service import Service

service = Service(config)
routes = web.RouteTableDef()
logger = create_logger(config)


@routes.view("/")
class View(web.View):
    @aiohttp_jinja2.template("home/index.html")
    async def get(self):
        return

    @aiohttp_jinja2.template("home/index.html")
    async def post(self):
        location = (await self.request.post()).get("location")
        try:
            response = await service.validate_query(location)
        except WrongLocationError:
            return json_response({"error": "Wrong Location"})
        return json_response({"answer": response})
