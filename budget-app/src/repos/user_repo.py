from budget_user.user import User
from database_connection import get_database_connection


def get_user_row(row):
    return User(row["username"], row["password"]) if row else None


class UserRepository:
    """Tietokantaoperaatiosta vastaava luokka liittyen käyttäjiin.
    """

    def __init__(self, connection):
        """Luokan konstruktori.

        Args:
            connection: Tietokantayhteyden connection-olio
        """

        self._connection = connection

    def create(self, user):
        """Tallentaa käyttäjän tietokantaan.

        Args:
            user: Käyttäjä, joka tallennetaan User-oliona.

        Returns:
            Käyttäjä, joka on tallennettu User-oliona.
        """

        cursor = self._connection.cursor()
        cursor.execute(
            "insert into users (username, password) values (?, ?)",
            (user.username, user.password)
        )
        self._connection.commit()

        return user

    def find_user(self, username):
        """Palauttaa käyttäjätunnuksen perusteella käyttäjän.

        Args:
            username: Käyttäjätunnus, jonka käyttäjä halutaan palauttaa.

        Returns:
            Palauttaa User-olion, jonka käyttäjätunnuksen omaava käyttäjä kyseessä.
            Jos käyttäjää ei ole tietokannassa palauttaa None.
        """

        cursor = self._connection.cursor()
        cursor.execute(
            "select * from users where username = ?",
            (username,)
        )
        row = cursor.fetchone()

        return get_user_row(row)

    def find_users(self):
        """Palauttaa kaikki käyttäjät tietokannasta.

        Returns:
            Palauttaa listana User-oliot.
        """

        cursor = self._connection.cursor()
        cursor.execute("select * from users")
        rows = cursor.fetchall()

        return list(map(get_user_row, rows))

    def delete_users(self):
        """Poistaa kaikki käyttäjät.
        """
        cursor = self._connection.cursor()
        cursor.execute("delete from users")
        self._connection.commit()


user_repo = UserRepository(get_database_connection())
