#!/bin/bash

if [ "$1" = "dev" ] | [ "$1" = "DEV" ]; then
 uvicorn mpapi.main:app --reload
else
  uvicorn mpapi.main:app
fi
