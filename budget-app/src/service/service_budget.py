from budget_user.budget import Budget
from budget_user.user import User

from repos.budget_repo import (budget_repo as default_budget_repo)
from repos.user_repo import (user_repo as default_user_repo)


def get_budget_row(row):
    return Budget(row["month"], row["income"], row["expense"],
                  row["user"], row["budget_id"]) if row else None


class UsernameExistsError(Exception):
    pass


class InvalidCredentialsError(Exception):
    pass


class BudgetService:

    def __init__(self, budget_repo=default_budget_repo, user_repo=default_user_repo):
        """Luokan konstruktori, joka luo sovelluslogiikkapalvelun.

        Args:
            budget_repo: Oletusarvoltaan BudgetRepository-olio,
                        jolla BudgetRepository-luokan metodit.
            user_repo: Oletusarvoltaan UserRepository-olio,
                        jolla UserRepository-luokan metodit.
        """

        self._user = None
        self._budget_repo = budget_repo
        self._user_repo = user_repo

    def create_budget(self, month, income, expense):
        """Luo uuden budjetin.

        Args:
            month: Merkkijono, joka kuvaa minkä kuukauden budjetti kyseessä.
            income: Integer, joka kuvaa tulojen määrää.
            expense: Integer, joka kuvaa menojen määrää.

        Returns:
            Budget-olion joka luotiin.
        """

        budget = Budget(month=month, income=income, expense=expense, user=self._user)
        return self._budget_repo.create_budget(budget)

    def get_budgets(self):
        """Palauttaa kirjautuneen käyttäjän luomat budjetit.

        Returns:
            Palauttaa käyttäjän budjetit Budget-olio listana.
            Jos ei ole kirjautunutta käyttäjää palauttaa tyhjän listan.
        """

        if not self._user:
            return []

        budgets = self._budget_repo.find_by_user(self._user.username)
        return budgets

    def login(self, username, password):
        """Käyttäjä kirjataan sisään.

        Args:
            username: Merkkijono, joka on kirjautuvan käuttäjän käyttäjätunnus.
            password: Merkkijono, joka on kirjautuvan käyttäjän salasana.

        Raises:
            InvalidCredentialsError:
                Virhe, jos käyttäjätunnus ja salasana eivät täsmää.

        Returns:
            Kirjautunut käyttäjä User_oliona.
        """

        user = self._user_repo.find_user(username)
        if not user or user.password != password:
            raise InvalidCredentialsError("Wrong username or password")

        self._user = user
        return user

    def current_user(self):
        """Palauttaa kirjautuneen käyttäjän.

        Returns:
            User-oliona kirjautuneen käyttäjän.
        """
        return self._user

    def get_users(self):
        """Palauttaa kaikki käyttäjät.

        Returns:
             Palauttaa listana User-oliot käyttäjistä.
        """

        return self._user_repo.find_users()

    def logout(self):
        """Kirjaa käyttäjän ulos.
        """

        self._user = None

    def delete(self, budget_id):
        """Poistaa tietyn budjetin.

        Args:
            budget_id: Budjetin id, joka poistetaan.
        """

        self._budget_repo.delete_budget(budget_id)

    def create_user(self, username, password, login=True):
        """Luo uuden käyttäjän.

        Args:
            username: Merkkijono, joka kuvaa käyttäjätunnusta.
            password: Merkkijono, joka kuvaa salasanaa.
            login: Oletusarvo True

        Raises:
            UsernameExistsError:
                Virhe, jos käyttäjätunnus on jo jollakin käyttäjällä.

        Returns:
            Käyttäjän User-oliona.
        """

        user_exists = self._user_repo.find_user(username)
        if user_exists:
            raise UsernameExistsError(f"Username {username} already exists")

        user = self._user_repo.create(User(username, password))

        if login:
            self._user = user

        return user


service_budget = BudgetService()
