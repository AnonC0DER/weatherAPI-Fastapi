import fastapi
from starlette.templating import Jinja2Templates
from starlette.requests import Request

router = fastapi.APIRouter()
templates = Jinja2Templates('weather/templates')

@router.get('/')
def home(request: Request):
    return templates.TemplateResponse('home.html', {'request' : request})


@router.get('/favicon.ico')
def favicon():
    return fastapi.responses.RedirectResponse(url='/static/img/favicon.ico')