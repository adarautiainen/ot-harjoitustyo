from budget_user.budget import Budget
from budget_user.user import User

from repos.budget_repo import (budget_repo as default_budget_repo)
from repos.user_repo import (user_repo as default_user_repo)


class UsernameExistsError(Exception):
    pass


class InvalidCredentialsError(Exception):
    pass


class BudgetService:

    def __init__(self, budget_repo=default_budget_repo, user_repo=default_user_repo):
        self._user = None
        self._budget_repo = budget_repo
        self._user_repo = user_repo

    def login(self, username, password):
        user = self._user_repo.find_user(username)
        if not user or user.password != password:
            raise InvalidCredentialsError("Wrong username or password")

        self._user = user
        return user

    def logout(self):
        self._user = None

    def current_user(self):
        return self._user

    def get_users(self):
        return self._user_repo.find_users()

    def get_budgets(self):
        if not self._user:
            return []

        budgets = self._budget_repo.find_by_username(self._user.username)
        return list(budgets)

    def create_budget(self, content):
        budget = Budget(content=content, user=self._user)
        return self._budget_repo.create(budget)

    def create_user(self, username, password, login=True):
        user_exists = self._user_repo.find_user(username)
        if user_exists:
            raise UsernameExistsError(f"Username {username} already exists")

        user = self._user_repo.create(User(username, password))

        if login:
            self._user = user

        return user


service_budget = BudgetService()
