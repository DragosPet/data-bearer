"""Command for SQL execution
Based on the run_config.yaml that should be initialized before."""

import os
import configargparse
from data_bearer.utils.run_utils import read_local_config, format_header, read_sql_files
from data_bearer.connectors.pgsql import PostGresConnector


parser = configargparse.ArgParser()

parser.add(
    "-w",
    "--workdir",
    required=True,
    help="Workdir path for storing and reading the state config and sql files.",
)

parser.add(
    "-i",
    "--interactive",
    required=True,
    help="Interactive Execution, allowing sql file discovery and execution",
    choices=['y','n']
)

parser.add(
    "-ep",
    "--export_path",
    required=False,
    help="Export path for the provided data.",
)

parser.add(
    "-sn",
    "--sql_file_name",
    required=False,
    help="SQL File that would be executed.",
)


def run_sql_code(args):
    """command function"""
    print(format_header())
    print("Execution of the provided sql code!")

    workdir = args.workdir
    sql_file_name = args.sql_file_name
    export_path = args.export_path
    if args.interactive == "y" :
        interactive_mode = True
    else : 
        interactive_mode = False        

    file_list = read_sql_files(workdir)
    if interactive_mode :
        print("") 
        print("Select which file to execute from sql path :")
        for el in file_list : 
            print(f"{el}")
        print("")
        sql_file_name = input("Input sql file name : \n")

    print("Checking if sql_file_name is in all sql scripts.")

    if sql_file_name in file_list :
        print("All good, sql file is available !")
        print("Executing sql script!")

        options = read_local_config(workdir)

        db_host = options["DB_HOST"]
        db_port = options["DB_PORT"]
        db_user = options["DB_USERNAME"]
        db_password = options["DB_PASSWORD"]
        db_target_db = options["DB_DATABASE"]

        conn_type = options["CONNECTION_TYPE"]
        print(f"Execution Context : {conn_type}")

        client = PostGresConnector(
            db_host,
            db_port,
            db_user,
            db_password,
            db_target_db,
            "WARN"
        )

        with open(f"{workdir}/sql/{sql_file_name}", 'r') as f:
            sql_string = " ".join(f.readlines())

        print(f"Executing sql : {sql_string}\n")
        data = client.fetch_data(sql_string)
        print(data.head())

        
    print(format_header())



def main():
    """Function that will act just as a conveyer and will be mapped to the poetry commands."""
    args = parser.parse_args()
    run_sql_code(args)


if __name__ == "__main__":
    main()
