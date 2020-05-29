from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from .routers import home

app = FastAPI()

app.include_router(home.router)
