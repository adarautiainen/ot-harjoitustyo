import sqlite3
from config import DATABASE_FILE_PATH, BUDGET_FILE_PATH

connection = sqlite3.connect(DATABASE_FILE_PATH)
connection.row_factory = sqlite3.Row

budget_connection = sqlite3.connect(BUDGET_FILE_PATH)
budget_connection.row_factory = sqlite3.Row


def get_database_connection():
    return connection


def get_budget_connection():
    return budget_connection
