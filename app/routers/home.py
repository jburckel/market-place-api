from fastapi import APIRouter, Depends
from fastapi.responses import HTMLResponse

from app import settings


router = APIRouter()

@router.get("/", response_class=HTMLResponse, tags=['home'])
def read_root():
    return f"""
    <html>
        <head>
            <title>MarketPlaceAPI Home</title>
        </head>
        <body>
            <h1>Welcome to {settings.APP_NAME}!</h1>
            <p>Contact: {settings.ADMIN_EMAIL}</p>
        </body>
    </html>
    """
