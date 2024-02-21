from multiprocessing import cpu_count


def max_workers():
    return cpu_count() + 1


reload = True
chdir = "/home/cristhian/www/cibertec/240V/02/"

name = "gunicorn"
pythonpath = "/home/cristhian/www/cibertec/240V/02/project/"
bind = "0.0.0.0:8000"
loglevel = "error"

limit_request_line = 0
max_requests = 1000
worker_class = "gevent"
workers = max_workers()

timeout = 300