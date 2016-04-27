workers = 2

def post_response(worker, req, environ, resp):
    worker.log.info("%s", worker.pid)
