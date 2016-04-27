import logging
import time
import yaml

import sys, os
rpath = os.path.join(os.path.dirname(os.path.realpath(__file__)), '../')
sys.path.append(rpath)
from tsdb.cluster import Database as DB
from tsdb.flaskapp import FlaskApp

with open(os.path.join(rpath, './conf/db.yaml'), 'r') as f:
    dbconf = yaml.load(f)
    DBHOST = dbconf['host']
    KEYSPC = dbconf['keyspace']

app = FlaskApp(__name__, DBHOST, KEYSPC)
app.init_dbsession()

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
    return 'Hello\n'

@app.route('/query')
def query_example():
    tick = time.time()
    rows = app.dbsession.execute("SELECT * from local")
    app.logger.info('%f s', time.time()-tick)
    return '{}\n'.format(rows[0].cluster_name)

if __name__ == '__main__':
    app.run(port=8000, debug=True)
