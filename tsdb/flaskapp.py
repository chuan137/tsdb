from flask import Flask
from .cluster import Database

class FlaskApp(Flask):
    
    def __init__(self, import_name, hosts, keyspace, **kwargs):
        super(FlaskApp, self).__init__(import_name, **kwargs)
        self.db = Database(hosts, keyspace)

    def init_dbsession(self):
        self.db.init_session()
        self.dbsession = self.db.session
#
# def flaskapp():
#     app = Flask(__name__)
#     app.config['DB'] = Database(hosts, keyspace)
#     app.config['DB'].init_session()
#     return app
#
