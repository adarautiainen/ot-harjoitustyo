import unittest
from repos.user_repo import user_repo
from budget_user import User

class TestUserRepo(unittest.TestCase):
    def setUp(self):
        user_repo.delete_users()
        self.user_maija = User("maija", "maija789")
        self.user_elena = User("elena", "elena789")

    def test_create(self):
        user_repo.create(self.user_maija)
        users = user_repo.find_users()

        self.assertEqual(len(users), 1)
        self.assertEqual(users[0].username, self.user_maija.username)

    def test_find_user(self):
        user_repo.create(self.user_maija)
        user = user_repo.find_user(self.user_maija.username)

        self.assertEqual(user.username, self.user_maija.username)

    def test_find_users(self):
        user_repo.create(self.user_maija)
        user_repo.create(self.user_elena)
        users = user_repo.find_users()

        self.assertEqual(len(users), 2)
        self.assertEqual(users[0].username, self.user_maija.username)
        self.assertEqual(users[1].username, self.user_elena.username)