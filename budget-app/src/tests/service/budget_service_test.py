import unittest
from budget_user.budget import Budget
from budget_user.user import User
from service.service_budget import (
    BudgetService, UsernameExistsError, InvalidCredentialsError)


#class TestBudgetService(unittest.TestCase):
    #def setUp(self):

        #self.budget1 = Budget("Budget1")
        #self.budget2 = Budget("Budget2")
        #self.user_maija = User("maija", "maija789")