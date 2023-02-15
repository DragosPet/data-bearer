from data_bearer.connectors.pgsql import PostGresConnector

def test_pg_connection_read() :
    con = PostGresConnector()
    test_df = con.fetch_data("SELECT CURRENT_DATE AS TODAY;")
    assert(test_df.empty == True)