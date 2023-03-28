import uuid

class Budget:
    # This class describes individual budget

    def __init__(self, content, value, user=None, budget_id=None):

        #content: string
        #value: int
        #user: describes owner of budget
        #budget_id: describes budgets' id

        self.content = content
        self.value = value
        self.user = user
        self.id = budget_id or str(uuid.uuid4())