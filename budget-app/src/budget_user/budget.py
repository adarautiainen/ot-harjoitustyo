import uuid


class Budget:

    def __init__(self, month, income, expense, user=None, budget_id=None):
        self.month = month
        self.income = income
        self.expense = expense
        self.user = user
        self.budget_id = budget_id or str(uuid.uuid4())


