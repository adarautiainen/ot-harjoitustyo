import unittest
from budget_user.budget import Budget
from budget_user.user import User
from service.service_budget import BudgetService, UsernameExistsError, InvalidCredentialsError

class FakeBudgetRepo:
    def __init__(self, budgets=None):
        self.budgets = budgets or []

    def find_budgets(self):
        return self.budgets

    def create_budget(self, budget):
        self.budgets.append(budget)
        return budget

    def find_by_user(self, username):
        user_budgets = filter(lambda budget: budget.user and budget.user.username == username,
                              self.budgets)
        return list(user_budgets)

    def delete(self, budget_id):
        budgets_no_id = filter(lambda budget: budget.id != budget_id, self.budgets)
        self.budgets = list(budgets_no_id)

    def delete_budgets(self):
        self.budgets = []


class FakeUserRepo:
    def __init__(self, users=None):
        self.users = users or []

    def find_users(self):
        return self.users

    def find_user(self, username):
        match = filter(lambda user: user.username == username, self.users)
        match_list = list(match)
        return match_list[0] if len(match_list) > 0 else None

    def create(self, user):
        self.users.append(user)

    def delete_users(self):
        self.users = []


class TestBudgetService(unittest.TestCase):
    def setUp(self):
        self.service_budget = BudgetService(budget_repo=FakeBudgetRepo(), user_repo=FakeUserRepo())
        self.user_maija = User(username="maija", password="maija789")
        self.budget1 = Budget(content="budget1", user=self.user_maija)
        self.budget2 = Budget(content="budget2", user=self.user_maija)

    def login(self, user):
        self.service_budget.login(user.username, user.password)

    def test_create_budget(self):
        self.service_budget.create_user(
            self.user_maija.username,
            self.user_maija.password
        )
        self.login(self.user_maija)
        self.service_budget.create_budget(self.budget1.content)
        budgets = self.service_budget.get_budgets()

        self.assertEqual(len(budgets), 1)
        self.assertEqual(budgets[0].content, "budget1")
        self.assertEqual(budgets[0].user.username, self.user_maija.username)

    def test_get_budgets(self):
        self.service_budget.create_user(
            self.user_maija.username,
            self.user_maija.password
        )
        self.login(self.user_maija)
        self.service_budget.create_budget(self.budget1.content)
        self.service_budget.create_budget(self.budget2.content)
        budgets = self.service_budget.get_budgets()

        self.assertEqual(len(budgets), 2)
        self.assertEqual(budgets[0].content, self.budget1.content)

    def test_login_valid(self):
        self.service_budget.create_user(
            self.user_maija.username,
            self.user_maija.password
        )
        user = self.service_budget.login(
            self.user_maija.username,
            self.user_maija.password
        )
        self.assertEqual(user.username, self.user_maija.username)

    def test_login_invalid(self):
        self.assertRaises(InvalidCredentialsError, lambda: self.service_budget.login("test", "invalid"))

    def test_current_user(self):
        self.service_budget.create_user(
            self.user_maija.username,
            self.user_maija.password
        )
        self.login(self.user_maija)
        current = self.service_budget.current_user()
        self.assertEqual(current.username, self.user_maija.username)

    def test_create_non_existing(self):
        username = self.user_maija.username
        password = self.user_maija.password

        self.service_budget.create_user(username, password)
        users = self.service_budget.get_users()

        self.assertEqual(len(users), 1)
        self.assertEqual(users[0].username, username)

    def test_create_existing(self):
        username = self.user_maija.username
        self.service_budget.create_user(username, "hello")

        self.assertRaises(UsernameExistsError, lambda: self.service_budget.create_user(username, "random"))