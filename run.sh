#!/bin/sh
set -e

# Start Gunicorn (ASGI server)
exec gunicorn analysis_service.wsgi:application --workers 4 --bind 0.0.0.0:8086

