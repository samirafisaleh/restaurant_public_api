import multiprocessing
import os
# https://docs.gunicorn.org/en/stable/settings.html



###################################################
# Config File Configuration
###################################################

###################################################
# Debug Configuration
###################################################
reload = True
check_config = False
print_config = False





###################################################
# Logging Configuration
###################################################
accesslog = "../../logging/gunicorn/access.log"
errorlog  = "../../logging/gunicorn/error.log"
loglevel = 'info'
capture_output = True



###################################################
# Process Naming Configuration
###################################################
proc_name = 'Since'


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
bind = '0.0.0.0:8000'

###################################################
# Worker Processes Configuration
###################################################
workers=1
worker_class="sync"
threads = 2
max_requests = 100
timeout = 30
graceful_timeout = 30
keepalive = 30
