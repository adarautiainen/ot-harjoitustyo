from database_connection import get_database_connection, get_budget_connection


def drop_tables(connection):
    cursor = connection.cursor()
    cursor.execute('''
        drop table if exists users;
    ''')
    connection.commit()


def create_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        create table users (
            username text primary key,
            password text
        );
    ''')
    connection.commit()


def initialize_database():
    connection = get_database_connection()
    connection2 = get_budget_connection()
    drop_tables(connection2)
    create_tables(connection2)
    drop_tables(connection)
    create_tables(connection)


if __name__ == "__main__":
    initialize_database()
