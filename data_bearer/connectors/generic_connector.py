"""
Generic connector abstract class, for future inheritance of specific connectors.
"""
from abc import ABC
import logging
import os


class Connector(ABC):
    """Abstract class for generic connector component."""

    __package_name__ = None

    def __init__(self) -> None:
        pass

    def set_logger(self, log_level="WARN", use_file="n", path=None):
        """Define logging properties for classes"""
        if log_level == "INFO":
            logging_level = logging.INFO
        elif log_level == "WARN":
            logging_level = logging.WARN
        else:
            logging_level = logging.ERROR
        if use_file.upper() == "Y":
            if path:
                if os.path.exists(path=path) == False:
                    os.mkdir(path=path)

                logging.basicConfig(
                    format="%(asctime)s %(levelname)s %(message)s",
                    datefmt="%m/%d/%Y %I:%M:%S",
                    filename=f"{path}/{self.__package_name__}.log",
                    filemode="a",
                    level=logging_level,
                )
            else:
                logging.basicConfig(
                    format="%(asctime)s %(levelname)s %(message)s",
                    datefmt="%m/%d/%Y %I:%M:%S",
                    level=logging_level,
                )
        else:
            logging.basicConfig(
                format="%(asctime)s %(levelname)s %(message)s",
                datefmt="%m/%d/%Y %I:%M:%S",
                level=logging_level,
            )

    def __str__(self) -> str:
        return str(self.__package_name__)

    def __repr__(self) -> str:
        return str(self.__package_name__)
