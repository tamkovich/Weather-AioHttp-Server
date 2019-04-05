from backend.model.model import Weather
from exceptions.service.exceptions import WrongLocationError


class Service:
    def __init__(self, config):
        self.weather = Weather(config)

    async def validate_query(self, location):
        if not location:
            raise WrongLocationError

        location = location.lower()
        data = await self.weather.get_weather(location)
        if data["cod"] == "404":
            raise WrongLocationError
        data = data["list"]
        data = list(
            map(
                lambda x: dict(
                    dt=x["dt"],
                    temp=x["main"]["temp"],
                    dt_txt=x["dt_txt"],
                    weather=x["weather"],
                ),
                data,
            )
        )
        return data
