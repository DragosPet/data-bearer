from data_bearer.utils.run_utils import *
import os
import pandas as pd

def test_local_config_generation():
    persist_local_config("test_files", {"CONNECTION_TYPE":"test"})

def test_local_config_read():
    options = read_local_config("test_files")
    keys = [x for x in options.keys()]
    assert(keys[0] == "CONNECTION_TYPE")

def test_read_sql_files():
    sql_files = read_sql_files("test_files")
    assert(sql_files == ["test_sql.sql"])

def test_export_dataframe():
    data = pd.DataFrame([(1,2),(3,4)], columns=["a","b"])
    export_dataframe("test_files", data)
    assert(1==1)    