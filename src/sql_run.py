import psycopg2
import getopt, sys, os, logging
from config.settings import DATABASES

logger = logging.getLogger("cons")

args = sys.argv[1:]
options = "io:"
long_opts = ["Insert_values", "Output="]

db = DATABASES["default"]
db_settings = {
    "dbname": db["NAME"],
    "user": db["USER"],
    "password": db["PASSWORD"],
    "host": db["HOST"],
    "port": db["PORT"],
}

def execute_sql_fixtures(files: list[str], path: str = ""):

    conn = psycopg2.connect(**db_settings)
    with conn:
        with conn.cursor() as cursor:
            for f in files:
                path = os.path.abspath(os.path.join(f"sql_scripts/{f}"))
                with open(path, "r") as f:
                    sql_script = f.read()
                cursor.execute(sql_script)


if __name__ == "__main__":
    sql_files = ["procedures.sql", "trigger_functions.sql", "triggers.sql"]
    args, vals = getopt.getopt(args, options, long_opts)
    for cur_arg, cur_val in args:
        if cur_arg in ("-i", "--Insert_values"):
            sql_files.append("insert_values.sql")
    execute_sql_fixtures(sql_files)
