@echo off
IF "%1" == "prod" GOTO prod
IF "%1" == "PROD" GOTO prod
IF "%1" == "dev" GOTO dev
IF "%1" == "DEV" GOTO dev

:prod
uvicorn mpapi.main:app

:dev
uvicorn mpapi.main:app --reload
