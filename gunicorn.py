import os

bind = "0.0.0.0:8000"
workers = 3
worker_class = "gevent"
debug = True
daemon = True
pidfile = "/tmp/gunicorn.pid"
logifle = "/tmp/gunicorn.log"
