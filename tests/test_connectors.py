from data_bearer.connectors.pgsql import PostGresConnector
from data_bearer.connectors.sqlitesql import SqliteConnector
from data_bearer.connectors.mysql_connector import MySqlConnector

def test_pg_connection_read() :
    con = PostGresConnector()
    test_df = con.fetch_data("SELECT CURRENT_DATE AS TODAY;")
    assert(test_df.empty == True)


def test_sqlite_connection_read() :
    con = SqliteConnector(db_target_database="test_files/test_sqlite.db")
    test_df = con.fetch_data("SELECT CURRENT_DATE AS TODAY;")
    assert(test_df.empty == False)

def test_mysql_connection_read() :
    con = MySqlConnector()
    test_df = con.fetch_data("SELECT CURRENT_DATE AS TODAY;")
    assert(test_df.empty == True)