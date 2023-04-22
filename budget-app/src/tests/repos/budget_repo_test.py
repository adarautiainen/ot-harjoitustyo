import unittest
from repos.budget_repo import budget_repo
from repos.user_repo import user_repo
from budget_user.user import User
from budget_user.budget import Budget


class TestBudgetRepository(unittest.TestCase):
    def setUp(self):
        budget_repo.delete_budgets()
        user_repo.delete_users()

        self.budget1 = Budget(month="may", income="300", expense="100")
        self.budget2 = Budget(month="august", income="400", expense="200")
        self.user_maija = User("maija", "maija789")
        self.user_elena = User("elena", "elena789")

    def test_create_budget(self):
        budget_repo.create_budget(self.budget1)
        budgets = budget_repo.find_budgets()
        self.assertEqual(len(budgets), 1)
        self.assertEqual(budgets[0].month, self.budget1.month)

    def test_find_budgets(self):
        budget_repo.create_budget(self.budget1)
        budget_repo.create_budget(self.budget2)
        budgets = budget_repo.find_budgets()

        self.assertEqual(len(budgets), 2)
        self.assertEqual(budgets[0].month, self.budget1.month)
        self.assertEqual(budgets[1].month, self.budget2.month)

    def test_delete_budget(self):
        maija = user_repo.create(self.user_maija)
        created = budget_repo.create_budget(self.budget1)
        budgets = budget_repo.find_budgets()
        self.assertEqual(len(budgets), 1)
        budget_repo.delete_budget(created.budget_id)
        budgets = budget_repo.find_budgets()
        self.assertEqual(len(budgets), 0)

    def test_find_by_user(self):
        maija = user_repo.create(self.user_maija)
        elena = user_repo.create(self.user_elena)

        budget_repo.create_budget(Budget(month="may", income="300", expense="100", user=maija))
        budget_repo.create_budget(Budget(month="june", income="400", expense="100", user=elena))

        maija_budgets = budget_repo.find_by_user(
            self.user_maija.username
        )

        self.assertEqual(len(maija_budgets), 1)
        self.assertEqual(maija_budgets[0].month, "may")

        elena_budgets = budget_repo.find_by_user(
            self.user_elena.username
        )

        self.assertEqual(len(elena_budgets), 1)
        self.assertEqual(elena_budgets[0].month, "june")


