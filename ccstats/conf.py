import os
import yaml
from default import default_value

class conf:
    def __init__(self):
        self.dv = default_value()
        self.conf_file = self.dv.conf_file

    def get_conf(self):
        conf_file = self.conf_file
        stream = open(conf_file, 'r')
        return yaml.load(stream)

    def store_dbinfo(self, info):
        """Write yaml file contains the info"""

        data = { "ccstats" : info }
        self.update_yaml(data)

    def update_yaml(self, data):

        conf_dir = self.dv.conf_dir
        conf_file = self.dv.conf_file

        self.ensure_dir(conf_dir)
        try:
            res = self.get_yaml(conf_file)
        except:
            res = {}
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

