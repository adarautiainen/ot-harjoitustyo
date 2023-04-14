import unittest
from repos.budget_repo import budget_repo
from repos.user_repo import user_repo
from budget_user.user import User
from budget_user.budget import Budget


class TestBudgetRepository(unittest.TestCase):
    def setUp(self):
        budget_repo.delete_budgets()
        user_repo.delete_users()

        self.budget1 = Budget("test 1")
        self.budget2 = Budget("test 2")
        self.user_maija = User("maija", "maija789")
        self.user_elena = User("elena", "elena789")

    def test_create(self):
        budget_repo.create_budget(self.budget1)
        budgets = budget_repo.find_budgets()
        self.assertEqual(len(budgets), 1)
        self.assertEqual(budgets[0].content, self.budget1.content)

    def test_find_budgets(self):
        budget_repo.create_budget(self.budget1)
        budget_repo.create_budget(self.budget2)
        budgets = budget_repo.find_budgets()

        self.assertEqual(len(budgets), 2)
        self.assertEqual(budgets[0].content, self.budget1.content)
        self.assertEqual(budgets[1].content, self.budget2.content)

    def test_find_by_user(self):
        maija = user_repo.create(self.user_maija)
        elena = user_repo.create(self.user_elena)

        budget_repo.create_budget(Budget(content="test 1", user=maija))
        budget_repo.create_budget(Budget(content="test 2", user=elena))

        maija_budgets = budget_repo.find_by_username(
            self.user_maija.username
        )

        self.assertEqual(len(maija_budgets), 1)
        self.assertEqual(maija_budgets[0].content, "test 1")

        elena_budgets = budget_repo.find_by_username(
            self.user_elena.username
        )

        self.assertEqual(len(elena_budgets), 1)
        self.assertEqual(elena_budgets[0].content, "test 2")


