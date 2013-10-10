from bson.code import Code
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

    # GROUP
    def _group(self, key_name, cond={}):

        # These functions for counting
        reducer = Code("""
                       function(obj, prev) {
                          prev.count++;
                       }
                       """)

        if key_name == "date":
            _key = "function(doc) {" + \
                    "new_date = new Date(doc." + key_name + ");" + \
                    "var month = new_date.getMonth() + 1;" + \
                    "var day = new_date.getDate();" + \
                    "return { date: String(new_date.getFullYear()) + " + \
                    "(month < 10 ? '0' : '') + month + (day > 10 ? '0': '')" + \
                    " + day};}"
        else:
            _key = { key_name: True }

        res = self.dbconn.group(
            key = _key,
            condition = cond,
            initial = { "count": 0 },
            reduce = reducer)
        return res

    def count_all(self):
        self._count()

    def count_sierra_openstack_grizzly(self):
        return self._count({"cloudPlatformIdRef":10})

    # Count with running status
    def count_running_vms_all(self):
        return self._count({"state":"Extant"})

    # sog: sierra_openstack_grizzly
    def count_running_vms_sog(self):
        return self._count({"state":"Extant",\
                            "cloudPlatformIdRef":10})

    # search date by weekly, monthly, quarterly
    def weekly_report(self):
        cond = self.weekly_condition
        self.weekly_count(cond)
        self.weekly_walltime(cond)

    def weekly_condition(self):
        # Condition for 7 days
        seven_days_ago = self.get_days_ago(7)
        today = self.get_days_ago(0)

        # Total usage
        cond = { "t_start": \
                {"$gt": seven_days_ago, \
                 "$lt": today}}

        return cond

    def weekly_count(self, cond):
        # total_vm_count_lanched_during_a_last_week
        total_vm_count = self._count(cond)
        print total_vm_count

        res = self._group("state", cond)
        print res
        # Daily usage
        res2 = self._group("date", cond)
        print res2

    def weekly_walltime(self, cond):
        reducer2 = Code("""                                                       
                        function(obj, prev){
                        state = obj.state; 
                        start = new Date(obj.t_start); 
                        if (state == "Extant"){
                        end = new Date();
                       }else{
                        end = new Date(obj.t_end)};
                        walltime= end.getTime() - start.getTime(); 
                        prev.count++;
                        prev.total += walltime;
                       }
                        """)

    def get_days_ago(self, days_to_subtract):
        return str(date.today() - timedelta(days=days_to_subtract))
    
    def count_running_vms_sog(self, from_date, to_date):
        return
