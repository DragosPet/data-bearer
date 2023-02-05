"""
Connector for Postgresql database interaction.
"""
import logging
import psycopg
import pandas as pd
from data_bearer.connectors.generic_connector import Connector


class PostGresConnector(Connector):
    """Class for Postgresql connectivity."""

    __package_name__ = "postgres"

    def __init__(
        self,
        db_host=None,
        db_port=None,
        db_user=None,
        db_pass=None,
        db_target_database=None,
        log_level="WARN",
    ):
        """Connect to Postgres using connection properties."""

        self.set_logger(log_level)

        if db_host and db_port and db_user and db_pass and db_target_database:
            logging.info("All properties available, creating connection !")
            connection_string = f"""host={db_host} port={db_port} user={db_user} password={db_pass} dbname={db_target_database}"""
            print(connection_string)
            try:
                self.connection = psycopg.connect(connection_string)
            except:
                self.connection = None
                logging.error(
                    "Unable to initialize connection, please check db credentials"
                )
        else:
            logging.warning(
                """Missing connection properties,
                please make sure to correctly specify connection params."""
            )
            self.connection = None

    def __str__(self) -> str:
        return f"connection for : {self.__package_name__}"

    def __repr__(self) -> str:
        return f"connection for : {self.__package_name__}"

    def fetch_data(self, sql_query) -> pd.DataFrame:
        """Given class connection, return pandas Dataframe with db content."""
        if self.connection:
            logging.info("Connection available, starting data read!")
            logging.info("Opening new db cursor.")
            try:
                cursor = self.connection.cursor()
                local_data = cursor.execute(sql_query).fetchall()
                column_names = [i[0] for i in cursor.description]
                local_df = pd.DataFrame(local_data, columns=column_names)
            except:
                logging.error(
                    f"Something went wrong in the sql execution. Sql code : {sql_query}"
                )
                local_df = pd.DataFrame()
            logging.info("Query execution complete, closing cursor.")
            cursor.close()
        else:
            logging.warning("Connection has to be properly initialized first.")
            local_df = pd.DataFrame()

        return local_df


if __name__ == "__main__":
    con = PostGresConnector()
    test_df = con.fetch_data("SELECT CURRENT_DATE AS TODAY;")
    print(test_df)
