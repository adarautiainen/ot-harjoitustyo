from tkinter import ttk, constants
import tkinter as tk
from service.service_budget import service_budget


class BudgetListView:
    """Luokka joka vastaa budjettien listauksesta."""

    def __init__(self, root, budgets, delete_budget):
        """Luokan konstruktori, joka luo uuden budjettilistausnäkymän.

        Args:
            root: Tkinter-elementti, näkymä alustetaan sen sisälle.
            budgets: Budget-olioita, jotka näkymässä näytetään.
            delete_budget: Arvo, jota kutsutaan kun budjetti poistetaan.
        """

        self._root = root
        self._budgets = budgets
        self._frame = None
        self._delete_budget = delete_budget

        self._initialize()

    def grid(self, **kwargs):
        """Näyttää näkymän.

        Args:
            **kwargs: Dictionary, jossa avaimet ovat grid-geometriahallinnan asetuksia.
        """

        self._frame.grid(kwargs)

    def destroy(self):
        """Tuhoaa näkymän."""

        self._frame.destroy()

    def _initialize_budget(self, budget):
        budget_frame = tk.Frame(master=self._frame, highlightbackground="orange", highlightthickness=1
                                , width=600, height=600)
        month_label = tk.Label(master=budget_frame, text=f"Month: {budget.month}")
        income_label = tk.Label(master=budget_frame, text=f"Income: {budget.income}")
        expense_label = tk.Label(master=budget_frame, text=f"Expenses: {budget.expense}")
        balance_label = tk.Label(master=budget_frame, text=f"Balance: "
                                                             f"{budget.income-budget.expense}")

        delete_button = tk.Button(
            master=budget_frame,
            text="Delete",
            command=lambda: self._delete_budget(budget.budget_id)
        )

        month_label.grid(row=0, column=0, padx=5, pady=5, sticky=constants.W)
        income_label.grid(row=1, column=0, padx=5, pady=5, sticky=constants.W)
        expense_label.grid(row=2, column=0, padx=5, pady=5, sticky=constants.W)
        balance_label.grid(row=3, column=0, padx=5, pady=5, sticky=constants.W)
        delete_button.grid(row=0, column=1, padx=5, pady=5, sticky=constants.EW)

        budget_frame.grid_rowconfigure(0, weight=1)
        budget_frame.grid_rowconfigure(1, weight=1)
        budget_frame.grid_rowconfigure(2, weight=1)
        budget_frame.grid_columnconfigure(0, weight=1)
        budget_frame.grid_columnconfigure(1, weight=1)

        budget_frame.grid(padx=5, pady=5, sticky=tk.EW)

    def _initialize(self):
        self._frame = tk.Frame(master=self._root)
        for budget in self._budgets:
            self._initialize_budget(budget)


class BudgetsView:
    """Luokka joka vastaa budjettien lisäämisestä ja listauksesta."""

    def __init__(self, root, handle_logout):
        """Luokan konstruktori, joka luo uuden budjettinäkymän.

         Args:
             root: Tkinter-elementti, käyttöliittymä alustetaan sen sisälle.
             handle_logout: Arvo, jota kutsutaan kun käyttäjä kirjautuu ulos.
         """

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
        self._error_var = None
        self._error_label = None

        self._initialize()

    def grid(self, **kwargs):
        """Näyttää näkymän.

        Args:
            **kwargs: Dictionary, jossa avaimet ovat grid-geometriahallinnan asetuksia.
        """

        self._frame.grid(kwargs)

    def destroy(self):
        """Tuhoaa näkymän. """

        self._frame.destroy()

    def _logout_handle(self):
        service_budget.logout()
        self._handle_logout()

    def _delete_budget(self, budget_id):
        service_budget.delete(budget_id)
        self._initialize_budget_list()

    def _show_error(self, message):
        self._error_var.set(message)
        self._error_label.grid(row=1, column=1, columnspan=2, padx=5, pady=5)

    def _remove_error(self):
        self._error_label.grid_remove()

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

        try:
            income = int(self._income_entry.get())
            expense = int(self._expense_entry.get())
            if income <= 0 or expense <= 0:
                self._show_error("Values cannot be zero or negative.")
            elif income > 0 and expense > 0 and (month and income and expense):
                service_budget.create_budget(month, income, expense)
                self._initialize_budget_list()
                self._month_entry.delete(0, constants.END)
                self._income_entry.delete(0, constants.END)
                self._expense_entry.delete(0, constants.END)
                self._remove_error()
            else:
                self._show_error("Values you entered are not correct.")
        except ValueError:
            self._show_error("Values you entered are not correct.")
            return

    def _initialize_footer(self):
        self._month_entry = ttk.Entry(master=self._frame)
        self._income_entry = ttk.Entry(master=self._frame)
        self._expense_entry = ttk.Entry(master=self._frame)

        month_label = tk.Label(master=self._frame, text="Month:")
        income_label = tk.Label(master=self._frame, text="Income:")
        expense_label = tk.Label(master=self._frame, text="Expenses:")

        create_button = tk.Button(master=self._frame, text="Create", command=self._handle_create)

        month_label.grid(row=2, column=0, padx=5, pady=5, sticky=constants.W)
        income_label.grid(row=3, column=0, padx=5, pady=5, sticky=constants.W)
        expense_label.grid(row=4, column=0, padx=5, pady=5, sticky=constants.W)

        self._month_entry.grid(
            row=2,
            column=1,
            sticky=constants.W,
            padx=5,
            pady=5
        )
        self._income_entry.grid(
            row=3,
            column=1,
            sticky=constants.W,
            padx=5,
            pady=5
        )
        self._expense_entry.grid(
            row=4,
            column=1,
            sticky=constants.W,
            padx=5,
            pady=5
        )
        create_button.grid(
            row=7,
            column=1,
            padx=5,
            pady=2,
            sticky=constants.EW
        )

    def _initialize(self):
        self._frame = tk.Frame(master=self._root)
        self._budget_frame = tk.Frame(master=self._frame)
        self._initialize_header()
        self._initialize_footer()
        self._initialize_budget_list()

        self._error_var = tk.StringVar(self._frame)
        self._error_label = tk.Label(
            master=self._frame,
            textvariable=self._error_var,
            foreground="orange"
        )
        self._error_label.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        self._budget_frame.grid(
            row=1,
            column=0,
            columnspan=2,
            sticky=constants.EW
        )

        self._frame.grid_columnconfigure(0, weight=1)

        self._remove_error()
