from db import ccsDB

class ccstats:
    def __init__(self):
        self.db = ccsDB()
        self.dbconn = self.db.conn.metric.instance

    def stats_all(self):
        return

    def count_all(self):
        return self.dbconn.count()

    def count_sierra_openstack_grizzly(self):
        return self.dbconn.find({"cloudPlatformIdRef":10}).count()
        


