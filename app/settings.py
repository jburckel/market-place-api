from starlette.config import Config
from starlette.datastructures import URL, Secret

config = Config(".env")


DEBUG = config('DEBUG', cast=bool, default=False)
TESTING = config('TESTING', cast=bool, default=False)
APP_NAME = config('APP_NAME', cast=str, default="Market Place API")
ADMIN_EMAIL = config('ADMIN_EMAIL', cast=str, default="admin@test.com")
ACCESS_TOKEN_EXPIRATION = config('ACCESS_TOKEN_EXPIRATION', cast=int, default=30)
JWT_SECRET_KEY = config('JWT_SECRET_KEY', cast=Secret)
JWT_ALGORITHM = config('ADMIN_EMAIL', cast=str, default="HS256")

DATABASE_URL = config('DATABASE_URL', cast=URL, default="sqlite:///app.db")
if TESTING:
    DATABASE_URL = DATABASE_URL.replace(database='test_' + DATABASE_URL.database)
