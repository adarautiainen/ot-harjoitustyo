from pathlib import Path
from budget_user.budget import Budget
from repos.user_repo import user_repo
from config import BUDGET_FILE_PATH

class BudgetRepository:

    def __init__(self, file_path):
        self._file_path = file_path

    def find_budgets(self):
        return self._read()

    def find_by_username(self, username):
        budgets = self.find_budgets()
        user_budgets = filter(
            lambda budget: budget.user and budget.user.username == username, budgets
        )
        return list(user_budgets)

    def create_budget(self, budget):
        budgets = self.find_budgets()
        budgets.append(budget)
        self._write(budgets)
        return budget

    def delete_every(self):
        self._write()

    def _ensure_file(self):
        Path(self._file_path).touch()

    def _read(self):
        budgets = []
        self._ensure_file()
        with open(self._file_path, encoding="utf-8") as file:
            for row in file:
                row = row.replace("\n", "")
                parts = row.split(";")

                budget_id = parts[0]
                content = parts[1]
                username = parts[2]

                user = user_repo.find_username(
                    username) if username else None

                budgets.append(
                    Budget(content, user, budget_id)
                )

            return budgets

    def _write(self, budgets):
        self._ensure_file()
        with open(self._file_path, "w", encoding="utf-8") as file:
            for budget in budgets:
                username = budget.user.username if budget.user else ""
                row = f"{budget.id};{budget.content};{username}"
                file.write(row+"\n")


budget_repo = BudgetRepository(BUDGET_FILE_PATH)

