from cassandra.cluster import Cluster

class Database(object):

    def __init__(self, hosts, keyspace):
        self.keyspace = keyspace
        self._cluster = Cluster(hosts)
        self._session = None

    def init_session(self):
        self._session = self._cluster.connect(self.keyspace)

    @property
    def cluster(self):
        return self._cluster
    @property
    def session(self):
        return self._session
