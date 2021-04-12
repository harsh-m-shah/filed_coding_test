"""
Module for DB Connection
"""
from flask_sqlalchemy import SQLAlchemy
from src import app


class DBConnection:
    """
    Singleton class for getting DB Connection instance
    """
    _instance = None

    @staticmethod
    def get_instance():
        """
        Static method for getting instance
        :return: DBConnection object
        """
        if DBConnection._instance is None:
            DBConnection()
        return DBConnection._instance

    def __init__(self):
        if DBConnection._instance is not None:
            raise Exception("Cannot create new instance because this class is a singleton class.")
        DBConnection._instance = self
        self.db = SQLAlchemy(app)

    def get_db_instance(self):
        """
        Method for getting db object
        :return: DB object
        """
        return self.db
