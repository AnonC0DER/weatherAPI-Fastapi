import fastapi
import uvicorn
from starlette.staticfiles import StaticFiles
from api import weather
from views import home

app = fastapi.FastAPI()

app.mount('/static', StaticFiles(directory='weather/static'), name='static')
app.include_router(home.router)
app.include_router(weather.router)



uvicorn.run(app)