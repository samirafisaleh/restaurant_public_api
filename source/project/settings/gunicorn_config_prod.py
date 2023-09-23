import multiprocessing
import os
# https://docs.gunicorn.org/en/stable/settings.html



###################################################
# Config File Configuration
###################################################

###################################################
# Debug Configuration
###################################################
reload = os.getenv("GUNICORN_RELOAD", True)
reload = True if reload == "true" else False
check_config = os.getenv("GUNICORN_CHECKCONFIG", True)
check_config = True if check_config == "true" else False
print_config = os.getenv("GUNICORN_PRINTCONFIG", True)
print_config = True if print_config == "true" else False





###################################################
# Logging Configuration
###################################################
accesslog = os.getenv("GUNICORN_ACCESS_LOGFILE", "../../logging/gunicorn/access.log")
errorlog  = os.getenv("GUNICORN_ERROR_LOGFILE", "../../logging/gunicorn/error.log")
loglevel = os.getenv("GUNICORN_LOGLEVEL", 'info')
capture_output = os.getenv("GUNICORN_CAPTURE_OUTPUT", False)
capture_output = True if capture_output == "true" else False



###################################################
# Process Naming Configuration
###################################################
proc_name = os.getenv("GUNICORN_PROC_NAME", 'University Of All')


###################################################
# SSL Configuration
###################################################

###################################################
# Security Configuration
###################################################

###################################################
# Server Hooks Configuration
###################################################
def on_starting(server):
    pass

def on_reload(server):
    pass

def when_ready(server):
    pass

def pre_fork(server, worker):
    pass

def post_fork(server, worker):
    pass

def post_worker_init(worker):
    pass

def worker_int(worker):
    pass

def worker_abort(worker):
    pass

def pre_exec(server):
    pass


def pre_request(worker, req):
    pass
    #worker.log.debug("%s %s", req.method, req.path)

def post_request(worker, req, environ, resp):
    pass


def child_exit(server, worker):
    pass

def worker_exit(server, worker):
    pass


def nworkers_changed(server, new_value, old_value):
    pass


def on_exit(server):
    pass


###################################################
# Server Mechanics Configuration
###################################################


###################################################
# Server Socket Configuration
###################################################
bind = os.getenv("GUNICORN_BIND", '0.0.0.0:8000')

###################################################
# Worker Processes Configuration
###################################################
workers=os.getenv("GUNICORN_WORKERS", 2)
worker_class=os.getenv("GUNICORN_WORKER_CLASS", "sync")
threads = os.getenv("GUNICORN_THREADS", 2)
max_requests = os.getenv("GUNICORN_MAX_REQUEST", 100)
timeout = os.getenv("GUNICORN_TIMEOUT", 30)
graceful_timeout = os.getenv("GUNICORN_GRACEFUL_TIMEOUT", 30)
keepalive = os.getenv("GUNICORN_KEEPALIVE", 30)
