import os
import httpx
from dotenv import load_dotenv
from typing import Optional
from httpx import Response
from caching.weather_cache import get_weather, set_weather
from models.validation import ValidationError

load_dotenv()

async def get_report(city: str, state: Optional[str], country: str, units: str) -> dict:
    if data := get_weather(city, state, country, units):
        return data

    if state:
        query = f'{city},{state},{country}'
    else:
        query = f'{city},{country}'

    url = f"https://api.openweathermap.org/data/2.5/weather?q={query}&appid={os.getenv('KEY')}"

    async with httpx.AsyncClient() as client:
        resp: Response = await client.get(url)
        if resp.status_code != 200:
            raise ValidationError(resp.text, status_code=resp.status_code)
    
    data = resp.json()
    
    set_weather(city, state, country, units, data)

    return data