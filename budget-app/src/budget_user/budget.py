import uuid


class Budget:

    def __init__(self, content, value, user=None, budget_id=None):
        self.content = content
        self.value = value
        self.user = user
        self.id = budget_id or str(uuid.uuid4())
