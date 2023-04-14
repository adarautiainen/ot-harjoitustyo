import uuid


class Budget:

    def __init__(self, content, user=None, budget_id=None):
        self.content = content
        self.user = user
        self.budget_id = budget_id or str(uuid.uuid4())
