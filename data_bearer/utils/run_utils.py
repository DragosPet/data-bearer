"""
General helper functions.
"""
import os
from yaml import safe_load, safe_dump
from datetime import datetime

def persist_local_config(workdir, args) -> None:
    """Given input working directory and arguments dict, store the config for reusability."""
    if os.path.exists(workdir) :
        print("Creating local state storage")
        with open(f"{workdir}/run_config.yaml", 'w') as f :
            safe_dump(args, f)
    else :
        print("Unable to create local state storage. Input workdir is not available !")

def read_local_config(workdir) -> dict :
    """Given input working directory, read the variables from local storage."""
    options = {}
    if os.path.exists(workdir) :
        try :  
            with open(f"{workdir}/run_config.yaml", 'r') as f :
                options = safe_load(f)
        except : 
            print("Local state storage not available. Please initialize state first.")
    else : 
        print("Provided path not available. Please provide a valid working directory.")
    return options

def read_sql_files(workdir) -> list :
    """Given input working directory, list the sql files stored for execution."""
    file_list = []
    if os.path.exists(workdir):
        if os.path.exists(f"{workdir}/sql") :
            print("Listing sql files available !")
            file_list = os.listdir(f"{workdir}/sql")
        else :
            print("No SQL folder available in the working directory!")            
    else :
        print("Parent path is not available!")
    return file_list
    

def format_header() -> str:
    "Formatting properties for Data Bearer commands."
    return f"""
{'-'*51}
{'-'*20}DATA BEARER{'-'*20}
{'-'*51}
"""

def export_dataframe(export_path, data) -> None:
    """Given input Dataframe, export data content to local path."""
    if os.path.exists(export_path) : 
        file_name = f"{export_path}/export_sql_{datetime.now().strftime('%Y%m%d%H%M%S')}.csv"
        data.to_csv(
            file_name,
            sep=",",
            index=False
        )
    else :
        print("Provided path is not available. Please input a valid path.")


if __name__ == '__main__' : 
    test_args = {
        "arg1": "db_test",
        "arg2": 123,
        "arg3": "."
    }
    persist_local_config(".",test_args)
    print(read_local_config("."))