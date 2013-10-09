from db import ccsDB

class ccstats:
    def __init__(self):
        self.dbconn = ccsDB()

    def stats_all(self):
        return

    def count_all(self):
        return self.dbconn.instance.count()

    def count_sierra_openstack_grizzly(self):
        return self.dbconn.instance.find({"cloudPlatformIdRef":10}).count()
        


