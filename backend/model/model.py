import aiohttp


class Weather:
    def __init__(self, config):
        self.url = config["backend"]["weather"]["url"]
        self.key = config["backend"]["weather"]["key"]

    async def get_weather(self, location):
        async with aiohttp.ClientSession() as session:
            async with session.get(
                self.url, params={"q": location, "units": "metric", "appid": self.key}
            ) as resp:
                return await resp.json()
