from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from mpapi import api, home, token


app = FastAPI()


app.include_router(home.router)


app.include_router(token.router)


app.include_router(
    api.v1.router,
    prefix="/api/v1"
)
