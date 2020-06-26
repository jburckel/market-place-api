@echo off
IF "%1" == "prod" GOTO prod
IF "%1" == "PROD" GOTO prod
IF "%1" == "dev" GOTO dev
IF "%1" == "DEV" GOTO dev
IF "%1" == "test" GOTO test
IF "%1" == "TEST" GOTO test

:prod
uvicorn mpapi.main:app

:dev
uvicorn mpapi.main:app --reload

:test
pytest
flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics --exclude venv,.git
