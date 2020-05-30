from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from mpapi import home
from mpapi import api

app = FastAPI()

app.include_router(home.router)

app.include_router(
    api.v1.router,
    prefix="/api/v1",
    tags=["v1"]
)
