from datetime import date, timedelta

from db import ccsDB

class ccstats:
    def __init__(self):
        self.db = ccsDB()
        self.dbconn = self.db.conn.metric.instance

    # Experiments & test
    def stats_all(self):
        return

    # COUNT
    def _count(self, cond=None):
        return self.dbconn.find(cond).count()

    def count_all(self):
        self._count()

    def count_sierra_openstack_grizzly(self):
        return self._count({"cloudPlatformIdRef":10})

    # Count with running status
    def count_running_vms_all(self):
        return self._count({"state":"Extant"})

    def count_running_vms_sog(self):
        return self._count({"state":"Extant",\
                            "cloudPlatformIdRef":10})

    # search date by weekly, monthly, quarterly
    def weekly_report(self):

        seven_days_ago = self.get_days_ago(7)
        today = self.get_days_ago(0)

        # Total usage
        cond = { "t_start": \
                {"$gt": seven_days_ago, \
                 "$lt": today}})
        # Daily usage

    def get_days_ago(self, days_to_substract):
        return date.today() - timedelta(days=days_to_subtract)
    
    def count_running_vms_sog(self, from_date, to_date):
        return


