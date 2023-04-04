import sqlite3
from config import dbpath


connection = sqlite3.connect(dbpath)
connection.row_factory = sqlite3.Row


def get_database_connection():
    return connection
