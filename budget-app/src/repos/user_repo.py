from budget_user.user import User
from database_connection import get_database_connection


def get_user_row(row):
    return User(row["username"], row["password"]) if row else None


class UserRepository:

    def __init__(self, connection):
        self._connection = connection

    def create_table(self):
        cursor = self._connection.cursor()
        cursor.execute('''
            create table users (
                username text primary key,
                password text
            );
        ''')

        self._connection.commit()

    def create(self, user):
        cursor = self._connection.cursor()
        cursor.execute(
            "insert into users (username, password) values (?, ?)",
            (user.username, user.password)
        )
        self._connection.commit()

        return user

    def find_user(self, username):
        cursor = self._connection.cursor()
        cursor.execute(
            "select * from users where username = ?",
            (username,)
        )
        row = cursor.fetchone()

        return get_user_row(row)

    def find_users(self):
        cursor = self._connection.cursor()
        cursor.execute("select * from users")
        rows = cursor.fetchall()

        return list(map(get_user_row, rows))

    def delete_users(self):
        cursor = self._connection.cursor()
        cursor.execute("delete from users")
        self._connection.commit()


user_repo = UserRepository(get_database_connection())
