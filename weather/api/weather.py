import fastapi
from fastapi import Depends
from typing import Optional
from models.location import Location
from services.openweather_service import get_report

router = fastapi.APIRouter()

@router.get('/api/weather/')
async def weather(loc: Location = Depends(), units: Optional[str] = 'metric'):
    report = await get_report(loc.city, loc.state, loc.country, units)

    return report['main']