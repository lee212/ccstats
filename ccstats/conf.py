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

