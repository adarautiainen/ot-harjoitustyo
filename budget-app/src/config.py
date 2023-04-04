import os
from dotenv import load_dotenv

path = "db/db.sqlite3"  # pylint: disable=invalid-name

dirname = os.path.dirname(__file__)

dbpath = os.path.join(dirname, path)

os.makedirs(os.path.dirname(dbpath), exist_ok=True)

try:
    load_dotenv(dotenv_path=os.path.join(dirname, "..", ".env"))
except FileNotFoundError:
    pass

BUDGET_FILENAME = os.getenv("BUDGET_FILENAME") or "budgets.csv"
BUDGET_FILE_PATH = os.path.join(dirname, "..", "data", BUDGET_FILENAME)

DATABASE_FILENAME = os.getenv("DATABASE_FILENAME") or "database.sqlite"
DATABASE_FILE_PATH = os.path.join(dirname, "..", "data", DATABASE_FILENAME)
