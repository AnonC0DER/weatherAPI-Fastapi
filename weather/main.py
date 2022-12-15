import fastapi
import uvicorn
from starlette.staticfiles import StaticFiles
from api import weather
from views import home

app = fastapi.FastAPI()

def configure():
    configure_routing()


def configure_routing():
    app.mount('/static', StaticFiles(directory='weather/static'), name='static')
    app.include_router(home.router)
    app.include_router(weather.router)


if __name__ == '__main__':
    configure()
    uvicorn.run('main:app', port=8000, host='127.0.0.1', reload=True)
else:
    configure()