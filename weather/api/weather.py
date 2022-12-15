import fastapi
from fastapi import Depends
from typing import Optional
from models.location import Location
from models.validation import ValidationError
from services.openweather_service import get_report

router = fastapi.APIRouter()

@router.get('/api/weather/')
async def weather(loc: Location = Depends(), units: Optional[str] = 'metric') -> dict:
    try:
        return await get_report(loc.city, loc.state, loc.country, units)
    except ValidationError as e:
        return fastapi.Response(content=e.error_msg, status_code=e.status_code)