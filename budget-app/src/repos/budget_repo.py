from budget_user.budget import Budget
from database_connection import get_database_connection


def get_budget_row(row):
    return Budget(row["content"], row["user"], row["budget_id"]) if row else None


class BudgetRepository:

    def __init__(self, connection):
        self._connection = connection

    def create_table(self):
        cursor = self._connection.cursor()
        cursor.execute("drop table if exists budgets")
        cursor.execute('''
            create table budgets (
                content text,
                user text references users,
                budget_id serial primary key
            );
        ''')

        self._connection.commit()

    def create_budget(self, budget):
        cursor = self._connection.cursor()
        cursor.execute(
            "insert into budgets (content, user, budget_id) values (?, ?, ?)",
            (budget.content, budget.user.username, budget.budget_id)
        )
        self._connection.commit()

        return budget

    def find_budgets(self):
        cursor = self._connection.cursor()
        cursor.execute("select * from budgets")
        rows = cursor.fetchall()

        return list(map(get_budget_row, rows))

    def find_by_user(self, user):
        cursor = self._connection.cursor()
        cursor.execute(
            "select * from budgets where user = ?",
            (user,)
        )
        rows = cursor.fetchall()

        budgets = []
        for row in rows:
            budget_dict = {
                "content": row["content"],
                "user": row["user"],
                "budget_id": row["budget_id"]
            }
            budgets.append(budget_dict)
        return budgets

    def delete_budgets(self):
        cursor = self._connection.cursor()
        cursor.execute("delete from budgets")
        self._connection.commit()


budget_repo = BudgetRepository(get_database_connection())
