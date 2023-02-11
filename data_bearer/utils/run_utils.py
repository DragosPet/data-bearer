"""
General helper functions.
"""
import os
from yaml import safe_load, safe_dump

def persist_local_config(workdir, args) -> None:
    """Given input working directory and arguments dict, store the config for reusability."""
    if os.path.exists(workdir) :
        print("Creating local state storage")
        with open(f"{workdir}/run_config.yaml", 'w') as f :
            safe_dump(args, f)
    else :
        print("Unable to create local state storage. Input workdir is not available !")

def read_local_config(workdir) -> list :
    """Given input working directory, read the variables from local storage."""
    options = {}
    if os.path.exists(workdir) :

        with open(f"{workdir}/run_config.yaml", 'r') as f :
                options = safe_load(f)
        try :  
            with open(f"{workdir}/run_config.yaml", 'r') as f :
                options = safe_load(f)
        except : 
            print("Local state storage not available. Please initialize state first.")
    else : 
        print("Provided path not available. Please provide a valid working directory.")
    return options

def format_header() -> str:
    "Formatting properties for Data Bearer commands."
    return f"""
{'-'*21}
---- DATA BEARER ----
{'-'*21}
"""


if __name__ == '__main__' : 
    test_args = {
        "arg1": "db_test",
        "arg2": 123,
        "arg3": "."
    }
    persist_local_config(".",test_args)
    print(read_local_config("."))