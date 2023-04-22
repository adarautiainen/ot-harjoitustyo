from budget_user.budget import Budget
from database_connection import get_database_connection


def get_budget_row(row):
    return Budget(row["month"], row["income"], row["expense"],
                  row["user"], row["budget_id"]) if row else None


class BudgetRepository:

    def __init__(self, connection):
        self._connection = connection

    def create_table(self):
        cursor = self._connection.cursor()
        cursor.execute("drop table if exists budgets")
        cursor.execute('''
            create table budgets (
                month text,
                income integer,
                expense integer,
                user text references users,
                budget_id serial primary key
            );
        ''')

        self._connection.commit()

    def create_budget(self, budget):
        cursor = self._connection.cursor()
        cursor.execute("select name from sqlite_master where type='table' and name='budgets'")
        table_exists = cursor.fetchone() is not None

        if not table_exists:
            self.create_table()

        cursor.execute(
            "insert into budgets (month, income, expense, user, budget_id) values (?, ?, ?, ?, ?)",
            (budget.month, budget.income, budget.expense,
             budget.user.username if hasattr(budget.user, 'username') else '',
             budget.budget_id)
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
            "select month, income, expense, user, budget_id from budgets where user = ?",
            (user,)
        )
        rows = cursor.fetchall()

        budgets = []
        for row in rows:
            budget = Budget(month=row[0], income=row[1], expense=row[2],
                            user=row[3], budget_id=row[4])
            budgets.append(budget)

        return budgets

    def delete_budget(self, budget_id):
        cursor = self._connection.cursor()
        cursor.execute("delete from budgets where budget_id = ?",
                       (budget_id,))
        self._connection.commit()

    def delete_budgets(self):
        cursor = self._connection.cursor()
        cursor.execute("delete from budgets")
        self._connection.commit()


budget_repo = BudgetRepository(get_database_connection())
