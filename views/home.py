import fastapi
from starlette.templating import Jinja2Templates
from starlette.requests import Request
from services.report_service import get_reports

router = fastapi.APIRouter()
templates = Jinja2Templates('templates')

@router.get('/', include_in_schema=False)
async def home(request: Request):
    reports = get_reports()
    events = reports['reports']
    count = reports['count']

    return templates.TemplateResponse('home/home.html', {'request' : request, 'events' : events, 'count' : count})


@router.get('/favicon.ico', include_in_schema=False)
async def favicon():
    return fastapi.responses.RedirectResponse(url='/static/img/favicon.ico')