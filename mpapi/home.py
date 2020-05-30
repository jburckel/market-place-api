from fastapi import APIRouter, Depends
from fastapi.responses import HTMLResponse

from mpapi import settings


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
            <p>Technical contact: <a href='mailto:{settings.ADMIN_EMAIL}'>{settings.ADMIN_EMAIL}</a></p>
        </body>
    </html>
    """
