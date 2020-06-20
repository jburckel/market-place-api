import pytest
from datetime import timedelta

from pymongo import MongoClient

from starlette.config import environ

from fastapi.encoders import jsonable_encoder
from fastapi.testclient import TestClient

environ["TESTING"] = 'TRUE'
environ["DATABASE_NAME"] = 'PYTEST'

from mpapi import settings
from mpapi.main import app
from mpapi.core.auth import create_access_token
from mpapi.crud.users import Users

from .db_init import db_init, db_drop


@pytest.fixture(scope='session')
def client():
    db_init(settings.DATABASE_URI, settings.DATABASE_NAME)
    yield TestClient(app)


@pytest.fixture(scope='session')
def user_token():
    user = Users.get_many(limit=1)[0]
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRATION)
    access_token = create_access_token(
        data={"sub": str(user["_id"])}, expires_delta=access_token_expires
    )
    yield {"Authorization": f"Bearer {access_token.decode('utf-8')}"}


@pytest.fixture(scope="session", autouse=True)
def cleanup(request):
    def cleaning():
        db_drop(settings.DATABASE_URI, settings.DATABASE_NAME)
    request.addfinalizer(cleaning)
