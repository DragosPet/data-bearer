import mysql.connector
import logging
import pandas as pd
from data_bearer.connectors.generic_connector import Connector


class MySqlConnector(Connector):
    """Class for MySQL connectivity."""

    __package_name__ = "mysql"

    def __init__(
        self,
        db_host=None,
        db_port=None,
        db_user=None,
        db_pass=None,
        db_target_database=None,
        log_level="INFO",
    ):
        """Connect to MySQL using connection properties."""

        self.set_logger(log_level)

        if db_host and db_port and db_user and db_pass and db_target_database:
            logging.info("All properties available, creating connection !")
            try:
                self.connection = mysql.connector.connect(
                    user=db_user,
                    password=db_pass,
                    host=db_host,
                    port=db_port,
                    database=db_target_database,
                )
            except Exception as e:
                self.connection = None
                logging.error(
                    f"Unable to initialize connection, please check db credentials. Received Error Type {type(e)}. Value : {e=}"
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
            cursor = self.connection.cursor()
            try:
                cursor = self.connection.cursor(dictionary=True)
                cursor.execute(sql_query)
                local_data = cursor.fetchall()
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
    con = MySqlConnector()
    test_df = con.fetch_data("SELECT CURRENT_DATE() AS TODAY;")
    print(test_df)
