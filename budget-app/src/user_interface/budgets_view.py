from tkinter import ttk, constants
import tkinter as tk
from service.service_budget import service_budget


class BudgetListView:

    def __init__(self, root, budgets, delete_budget):
        self._root = root
        self._budgets = budgets
        self._frame = None
        self._delete_budget = delete_budget

        self._initialize()

    def grid(self, **kwargs):
        self._frame.grid(kwargs)

    def destroy(self):
        self._frame.destroy()

    def _initialize_budget(self, budget):
        budget_frame = tk.Frame(master=self._frame)
        month_label = tk.Label(master=budget_frame, text=f"Month: {budget.month}")
        income_label = tk.Label(master=budget_frame, text=f"Income: {budget.income}")
        expense_label = tk.Label(master=budget_frame, text=f"Expense: {budget.expense}")

        delete_button = tk.Button(
            master=budget_frame,
            text="Delete",
            width=2,
            command=lambda: self._delete_budget(budget.budget_id)
        )

        month_label.grid(row=0, column=0, padx=5, pady=5, sticky=constants.W)
        income_label.grid(row=1, column=0, padx=5, pady=5, sticky=constants.W)
        expense_label.grid(row=2, column=0, padx=5, pady=5, sticky=constants.W)
        delete_button.grid(row=0, column=1, padx=5, pady=5, sticky=constants.EW)
        budget_frame.grid_columnconfigure(0, weight=1)
        budget_frame.grid()

    def _initialize(self):
        self._frame = tk.Frame(master=self._root)
        for budget in self._budgets:
            self._initialize_budget(budget)


class BudgetsView:
    def __init__(self, root, handle_logout):
        self._root = root
        self._handle_logout = handle_logout
        self._user = service_budget.current_user()
        self._frame = None
        self._create_entry = None
        self._budget_frame = None
        self._budget_view = None
        self._month_entry = None
        self._income_entry = None
        self._expense_entry = None

        self._initialize()

    def grid(self, **kwargs):
        self._frame.grid(kwargs)

    def destroy(self):
        self._frame.destroy()

    def _logout_handle(self):
        service_budget.logout()
        self._handle_logout()

    def _delete_budget(self, budget_id):
        service_budget.delete(budget_id)
        self._initialize_budget_list()

    def _initialize_budget_list(self):
        if self._budget_view:
            self._budget_view.destroy()

        budgets = service_budget.get_budgets()

        self._budget_view = BudgetListView(
            self._budget_frame,
            budgets,
            self._delete_budget
        )

        self._budget_view.grid()

    def _initialize_header(self):
        user_label = tk.Label(master=self._frame, text=f"You are logged in as {self._user.username}")
        logout_button = tk.Button(master=self._frame, text="Logout", command=self._handle_logout)

        user_label.grid(row=0, column=0, padx=5, pady=5, sticky=constants.W)
        logout_button.grid(row=0,
                           column=1,
                           padx=5,
                           pady=5,
                           sticky=constants.EW)

    def _handle_create(self):
        month = self._month_entry.get()
        income = self._income_entry.get()
        expense = self._expense_entry.get()
        if month and income and expense:
            service_budget.create_budget(month, income, expense)
            self._initialize_budget_list()
            self._month_entry.delete(0, constants.END)
            self._income_entry.delete(0, constants.END)
            self._expense_entry.delete(0, constants.END)

    def _initialize_footer(self):
        self._month_entry = ttk.Entry(master=self._frame)
        self._income_entry = ttk.Entry(master=self._frame)
        self._expense_entry = ttk.Entry(master=self._frame)

        month_label = tk.Label(master=self._frame, text="Month:")
        income_label = tk.Label(master=self._frame, text="Income:")
        expense_label = tk.Label(master=self._frame, text="Expense:")

        create_button = tk.Button(master=self._frame, text="Create", command=self._handle_create)

        month_label.grid(row=2, column=0, padx=5, pady=2, sticky=constants.W)
        income_label.grid(row=3, column=0, padx=5, pady=2, sticky=constants.W)
        expense_label.grid(row=4, column=0, padx=5, pady=2, sticky=constants.W)

        self._month_entry.grid(
            row=2,
            column=1,
            padx=5,
            pady=2,
            sticky=(constants.E, constants.W)
        )
        self._income_entry.grid(
            row=3,
            column=1,
            padx=5,
            pady=2,
            sticky=constants.EW
        )
        self._expense_entry.grid(
            row=4,
            column=1,
            padx=5,
            pady=2,
            sticky=(constants.E, constants.W)
        )
        create_button.grid(
            row=7,
            column=1,
            padx=5,
            pady=2,
            sticky=(constants.E, constants.W)
        )

    def _initialize(self):
        self._frame = tk.Frame(master=self._root)
        self._budget_frame = tk.Frame(master=self._frame)
        self._initialize_header()
        self._initialize_footer()
        self._initialize_budget_list()

        self._budget_frame.grid(
            row=1,
            column=0,
            columnspan=2,
            sticky=constants.EW
        )

        self._frame.grid_columnconfigure(0, weight=1)

