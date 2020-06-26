#!/bin/bash

if [ "$1" = "dev" ] | [ "$1" = "DEV" ]; then
  uvicorn mpapi.main:app --reload
elif [ "$1" = "test" ] | [ "$1" = "TEST" ]; then
  pytest
  flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics --exclude venv,.git
else
  uvicorn mpapi.main:app
fi
