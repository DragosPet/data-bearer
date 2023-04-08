"""Command for client initialization
Generation of a run_config.yaml that will be used in the execution)."""

import os
from getpass import getpass
from data_bearer.utils.run_utils import persist_local_config, format_header


def init_config():
    """command function"""
    print(format_header())
    print("Starting configuration of client!")

    workdir = input("Input working directory (where to store the db config) : \n")
    connection_type = input("Input Connection TYPE ([POSTGRES/SQLITE/MYSQL]) : \n")
    replace_flag = input("Replace Existing Config (if any) ? : \n")
    db_host = input("Input Database Host (if necessary) : \n")
    db_port = input("Input Database Port (if necessary) : \n")
    db_user = input("Input Database User (if necessary) : \n")
    db_password = getpass("Input Database Password (if necessary) : \n")
    db_target_db = input("Input Target Database (if sqlite, path to db) : \n")

    config_data = {
        "DB_HOST": db_host,
        "CONNECTION_TYPE": connection_type,
        "DB_PORT": db_port,
        "DB_USERNAME": db_user,
        "DB_PASSWORD": db_password,
        "DB_DATABASE": db_target_db,
    }

    if os.path.exists(f"{workdir}/run_config.yaml"):
        print("Config already exists.")
        if replace_flag == "Y":
            print("Replace flag is marked as Y. Replacing config.")

            print(f"Exporting config : {config_data.keys()}")
            persist_local_config(workdir=workdir, args=config_data)
        else:
            print("Config exists and replace flag is marked as N. Stopping.")
    else:
        persist_local_config(workdir=workdir, args=config_data)

    print("All set !")
    print(format_header())


def main():
    """Function that will act just as a conveyer and will be mapped to the poetry commands."""
    init_config()


if __name__ == "__main__":
    main()
