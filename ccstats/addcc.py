import os
import yaml
from default import default_value
import getpass
from pprint import pprint

class addcc:
    def __init__(self):
        self.default_value = default_value()

    def get_uniq_name(self):
        if self.cloudname in ['openstack', 'eucalyptus', 'nimbus' ]:
            uniq_name = self.cloudname + "_with_" + self.dbinfo['host'].replace(".", "_")
        else:
            uniq_name = self.cloudname
        return uniq_name

    def store_info(self):
        """Write yaml file contains the info"""

        data = { self.get_uniq_name(): self.__dict__ }
        self.update_yaml(data)

    def update_yaml(self, data):

        conf_dir = self.default_value.conf_dir
        conf_file = self.default_value.conf_file

        self.ensure_dir(conf_dir)
        try:
            res = self.get_yaml(conf_file)
        except:
            res = {}
        print res
        print data
        final = dict(res.items() + data.items())
        self.set_yaml(conf_file, final)

    def ensure_dir(self, conf_dir):
        if not os.path.exists(conf_dir):
                os.makedirs(conf_dir)

    def get_yaml(self, conf_file):
        stream = open(conf_file, 'r')
        return yaml.load(stream)

    def set_yaml(self, conf_file, data):
        with open(conf_file, 'w') as outfile:
            outfile.write( yaml.dump(data, default_flow_style=False) )

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
                      "N) Nimbus \n" + \
                     "Or you can simply type your unique cloud name. \n" + \
                     "For example, sierra_openstack_grizzly") or "O"

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
            self.cloudname = title

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
    obj.store_info()
