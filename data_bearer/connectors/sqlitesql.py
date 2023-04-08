"""
Connector for SQLITE database interaction.
"""
import logging
import sqlite3
import pandas as pd
from data_bearer.connectors.generic_connector import Connector


class SqliteConnector(Connector):
    """Class for Sqlite connectivity."""

    __package_name__ = "sqlite"

    def __init__(
        self,
        db_target_database=None,
        log_level="WARN",
        use_files="n",
        logs_path=None
    ):
        """Connect to Sqlite using connection properties."""

        self.set_logger(log_level, use_file=use_files, path=logs_path)

        if db_target_database:
            logging.info("All properties available, creating connection !")
            try:
                self.connection = sqlite3.connect(db_target_database)
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
    con = SqliteConnector()
    test_df = con.fetch_data("SELECT CURRENT_DATE;")
    print(test_df.info())
