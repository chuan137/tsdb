from cassandra.cluster import Cluster
from flask import Flask
import logging
import time

DBHOST = '141.52.65.167'
# DBHOST = '127.0.0.1'
KEYSPC = 'system'

app = Flask(__name__)

def setup_dbsession(app):
    cluster = Cluster([DBHOST])
    app.config['cluster'] = cluster
    app.config['session'] = cluster.connect(KEYSPC)

@app.before_first_request
def setup_logging():
    if not app.debug:
        logstr = '[Flask] [%(levelname)s] %(message)s'
        logfmt = logging.Formatter(logstr)
        shandler = logging.StreamHandler()
        shandler.setFormatter(logfmt)
        app.logger.addHandler(shandler)
        app.logger.setLevel(logging.DEBUG)

@app.route('/')
def hello():
    app.logger.info('ok')
    app.logger.info(app.config['session'])
    return 'Hello\n'

@app.route('/query')
def query_example():
    # tick = time.time()
    rows = app.config['session'].execute("SELECT * from local")
    # app.logger.info('%f s', time.time()-tick)
    return '{}\n'.format(rows[0].cluster_name)

setup_dbsession(app)

if __name__ == '__main__':
    app.run(port=8000, debug=True)
