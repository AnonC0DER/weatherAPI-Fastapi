import fastapi
import uuid
from starlette.templating import Jinja2Templates
from starlette.requests import Request
from services.report_service import get_reports

router = fastapi.APIRouter()
templates = Jinja2Templates('templates')
instance_id = uuid.uuid4()

@router.get('/', include_in_schema=False)
async def home(request: Request):
    reports = get_reports(limit=10)
    events = reports['reports']
    count = reports['count']

    return templates.TemplateResponse('home/home.html', {'request' : request, 'events' : events, 'count' : count, 'instance_id' : instance_id})


@router.get('/favicon.ico', include_in_schema=False)
async def favicon():
    return fastapi.responses.RedirectResponse(url='/static/img/favicon.ico')


@router.get("/sentry-debug")
async def trigger_error():
    division_by_zero = 1 / 0