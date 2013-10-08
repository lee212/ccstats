import pymongo
import pprint

from optparse import OptionParser

from stdin import stdInput
from default import default_value as dv
from conf import conf

class ccsDB:
    def __init__(self):
        self.conf = conf()

    def set_dbinfo(self):
        self.conf.store_dbinfo(self.db)
        '''
        get user input
        write to / update to yaml
        {stats:
         mongo host, port, id, pass, dbname }
         '''

    def _stdin_setup(self):
        """configure database information for storing statistics"""
        self.ask_dbinfo()
        while not self.confirm_dbinfo():
            self.ask_dbinfo()
        self.set_dbinfo()

    def ask_dbinfo(self):
        mgdb_host = stdInput.ask_info("mongo host", dv.ccstats_db_host)
        mgdb_port = stdInput.ask_info("mongo port", dv.ccstats_db_port) 
        mgdb_id = stdInput.ask_info("mongo id", dv.ccstats_db_id)
        mgdb_pass = stdInput.ask_info("mongo pass", pwd=True)
        mgdb_name = stdInput.ask_info("mongo db name", dv.ccstats_db_name)

        self.db = { "host": mgdb_host, \
                   "port": mgdb_port, \
                   "id": mgdb_id, \
                   "pass": mgdb_pass, \
                   "name": mgdb_name }

    def display_dbinfo(self):
        pprint.pprint (self.db)

    def confirm_dbinfo(self):
        self.display_dbinfo()
        return self.ask_confirm()

    def ask_confirm(self):
        yn = stdInput.ask_info("Is correct?", "Y")
        if yn.upper() == "Y":
            return True
        return False

if __name__ == "__main__":
    obj = ccsDB()

    parser = OptionParser()
    #parser.add_option("setup", action="store_true", dest="setup", \
    #                  default=False, help="setup stats db info")

    (options, args) = parser.parse_args()
    for arg in args:
        func = getattr(obj, "_stdin_" + arg)
        func()
