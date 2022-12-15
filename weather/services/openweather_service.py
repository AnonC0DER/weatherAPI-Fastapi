import os
import httpx
from dotenv import load_dotenv
from typing import Optional
from caching import weather_cache

load_dotenv()

async def get_report(city: str, state: Optional[str], country: str, units: str) -> dict:
    if data := weather_cache.get_weather(city, state, country, units):
        return data

    if state:
        query = f'{city},{state},{country}'
    else:
        query = f'{city},{country}'

    url = f"https://api.openweathermap.org/data/2.5/weather?q={query}&appid={os.getenv('KEY')}"

    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
        resp.raise_for_status()
    
    data = resp.json()
    
    weather_cache.set_weather(city, state, country, units, data)

    return data