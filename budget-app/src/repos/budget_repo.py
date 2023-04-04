from pathlib import Path
from budget_user.budget import Budget
from repos.user_repo import user_repo
from config import BUDGET_FILE_PATH

class BudgetRepository:

    def __init__(self, file_path):
        self._file_path = file_path