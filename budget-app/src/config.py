import os

dirname = os.path.dirname(__file__)

BUDGET_FILENAME = os.getenv("BUDGET_FILENAME") or "budgets.sqlite"
BUDGET_FILE_PATH = os.path.join(dirname, "..", "data", BUDGET_FILENAME)

DATABASE_FILENAME = os.getenv("DATABASE_FILENAME") or "database.sqlite"
DATABASE_FILE_PATH = os.path.join(dirname, "..", "data", DATABASE_FILENAME)
