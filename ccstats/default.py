import os
class default_value:
    db_type = "mysql"
    db_mysql_port = "3306"
    db_mongo_port = "27017"

    HOME = os.environ['HOME']
    conf_dir = HOME + "/" + ".ccstats"
    conf_file = conf_dir + "/" + "ccstats.yaml"

    ccstats_db_type = "mongo"
    ccstats_db_host = "localhost"
    ccstats_db_port = 27017
    ccstats_db_id = "ccstats_admin"
    ccstats_db_pass = "ccstats_pass"
    ccstats_db_name = "ccstats"

    ccstats_metric_type = "mongo"
    ccstats_metric_host = "localhost"
    ccstats_metric_port = 27017
    ccstats_metric_id = "fgmetrics"
    ccstats_metric_pass = ""
    ccstats_metric_name = "cloudmetrics"
