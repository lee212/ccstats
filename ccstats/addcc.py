from default import default_value
import getpass
from pprint import pprint

class addcc:
    def __init__(self):
        self.default_value = default_value()

    def confirm_info(self):
        self.display_info()
        if not self.ask_confirm():
            self.ask_info()

    def ask_confirm(self):
        yn = raw_input("Is correct? [Y/n]:") or "Y"
        if yn.upper() == "Y":
            return True
        return False

    def display_info(self):
        print ""
        print "- Information you entered -"
        print ""
        print "=" * 55
        print "cloudname:"
        pprint (self.cloudname)
        print "=" * 55
        print "db info:"
        pprint (self.dbinfo)

    def ask_info(self):
        self.ask_cloudname()
        self.ask_dbinfo()

    def ask_dbinfo(self):
        print "=" * 55
        print "To collect usage data, database information required. \n" +\
                "db type, hostname, id, password, portnumber."
        print "=" * 55
        db_type = raw_input("db type [%s]:" % self.get_default('db_type')) or \
                self.get_default('db_type')
        db_host = raw_input("db host:")
        db_port = raw_input("db port [%s]:" % self.get_default('db_' + db_type+\
                                                               '_port')) or \
                self.get_default('db_' + db_type + '_port')
        db_user = raw_input("db username [%s]: " % getpass.getuser())
        if not db_user:
            db_user = getpass.getuser()
        pprompt = lambda: (getpass.getpass(),
                           getpass.getpass('Retype password:'))
        db_p1, db_p2 = pprompt()
        while db_p1 != db_p2:
            print('Passwords do not match. Try again')
            db_p1, db_p2 = pprompt()

        self.set_dbinfo(db_type, db_host, db_port, db_user, db_p1)

    def ask_cloudname(self):
        x = raw_input("Which cloud do you want to add? \n" + \
                      "O) (default) Openstack \n" + \
                      "E) Eucalyptus \n" + \
                      "N) Nimbus \n") or "O"

        self.set_cloudname(x)
        print self.cloudname

    def set_cloudname(self, title):
        if title == "O":
            self.cloudname = "openstack"
        elif title == "E":
            self.cloudname = "eucalyptus"
        elif title == "N":
            self.cloudname = "nimbus"
        else:
            self.cloudname = "openstack"

    def set_dbinfo(self, db_type, db_host, db_port, db_user, db_pass):

        self.dbinfo = { "type": db_type, \
                       "host": db_host, \
                       "port": db_port, \
                       "user": db_user, \
                       "pass": db_pass }

    def get_default(self, name):
        try:
            return getattr(self.default_value, name)
        except:
            return None

if __name__ == "__main__":
    obj = addcc()
    obj.ask_info()
    obj.confirm_info()
