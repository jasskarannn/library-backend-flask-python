#!/bin/bash

flask db upgrade
gunicorn -b 0.0.0.0:8080 --access-logfile - "wsgi:flask_app"
#dummy
