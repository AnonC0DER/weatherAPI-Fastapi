import fastapi
import uvicorn
from starlette.staticfiles import StaticFiles
from api import weather
from api import report
from views import home

import sentry_sdk

sentry_sdk.init(
    dsn='https://1ac0e678f7eb4f9ba14ee889615eee7c@sentry.hamravesh.com/536',
    traces_sample_rate=1.0,
)

app = fastapi.FastAPI()

def configure():
    configure_routing()


def configure_routing():
    app.mount('/static', StaticFiles(directory='static'), name='static')
    app.include_router(home.router)
    app.include_router(weather.router)
    app.include_router(report.router)


if __name__ == '__main__':
    configure()
    uvicorn.run('main:app', port=80, host='127.0.0.1', reload=True)
else:
    configure()