import uuid


class Budget:

    """Tämä luokka kuvaa budjettia.

    Attributes:
        month: Merkkijono, joka kuvaa minkä kuukauden budjetti kyseessä.
        income: Integer, joka kuvaa tulojen määrää.
        expense: Integer, joka kuvaa menojen määrää.
        user: User-olio, joka kuvaa budjetin luojaa.
        budget_id: Merkkijono, joka kuvaa budjetin id:tä.

    """

    def __init__(self, month, income, expense, user=None, budget_id=None):
        """Luokan konstruktori luo uuden budjetin.

        Args:
            month: Merkkijono, joka kuvaa minkä kuukauden budjetti kyseessä.
            income: Integer, joka kuvaa tulojen määrää.
            expense: Integer, joka kuvaa menojen määrää.
            user: User-olio, joka kuvaa budjetin luojaa.
            budget_id: Merkkijono, joka kuvaa budjetin id:tä
                       Oletusarvo on generoitu uuid.
        """

        self.month = month
        self.income = income
        self.expense = expense
        self.user = user
        self.budget_id = budget_id or str(uuid.uuid4())
