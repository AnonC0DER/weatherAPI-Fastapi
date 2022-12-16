import fastapi
from starlette.templating import Jinja2Templates
from starlette.requests import Request
from services import report_service

router = fastapi.APIRouter()
templates = Jinja2Templates('templates')

@router.get('/', include_in_schema=False)
async def home(request: Request):
    events = await report_service.get_reports()
    return templates.TemplateResponse('home/home.html', {'request' : request, 'events' : events})


@router.get('/favicon.ico', include_in_schema=False)
async def favicon():
    return fastapi.responses.RedirectResponse(url='/static/img/favicon.ico')