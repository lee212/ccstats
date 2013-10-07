import os
class default_value:
    db_type = "mysql"
    db_mysql_port = "3306"
    db_mongo_port = "27017"

    HOME = os.environ['HOME']
    conf_dir = HOME + "/" + ".ccstats"
    conf_file = conf_dir + "/" + "ccstats.yaml"
