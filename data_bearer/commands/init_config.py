import os
import configargparse
from data_bearer.utils.run_utils import persist_local_config

parser = configargparse.ArgParser()

parser.add(
    "-w",
    "--workdir",
    required=True,
    help="Workdir path for storing and reading the state config and sql files."
)

parser.add(
    "-rp",
    "--replace_flag",
    required=True,
    help="Flag for replacing existing config (if available).",
    choices=["Y","N"]
)

parser.add(
    "-c",
    "--connection_type",
    required=True,
    help="Database connection type. Values in POSTGRES, SQLITE"
)

parser.add(
    "-dh",
    "--db_host",
    required=True,
    help="Database host server."
)

parser.add(
    "-dpt",
    "--db_port",
    required=True,
    help="Database host server port."
)

parser.add(
    "-dp",
    "--db_password",
    required=True,
    help="Database host server password."
)

parser.add(
    "-du",
    "--db_user",
    required=True,
    help="Database User."
)

parser.add(
    "-dt",
    "--db_target_db",
    required=True,
    help="Target Database for sql execution."
)

def init_config(args) :
    
    workdir = args.workdir
    db_host = args.db_host
    db_port = args.db_port
    db_user = args.db_user
    db_password = args.db_password
    db_target_db = args.db_target_db

    connection_type = args.connection_type
    replace_flag = args.replace_flag

    if os.path.exists(f"{workdir}/run_config.yaml") :
        print(f"Config already exists.")
        if replace_flag == 'Y' :
            print("Replace flag is marked as Y. Replacing config.")
            config_data = {
                "DB_HOST": db_host,
                "CONNECTION_TYPE" : connection_type,
                "DB_PORT": db_port,
                "DB_USERNAME": db_user,
                "DB_PASSWORD": db_password,
                "DB_DATABASE": db_target_db
                }
            print(f"Exporting config : {config_data.keys()}")
            persist_local_config(
                workdir=workdir,
                args=config_data
                )
        else : 
            print("Config exists and replace flag is marked as N. Stopping.")

def main() :
    args = parser.parse_args()
    init_config(args)

if __name__ == "__main__" :
    main()    


