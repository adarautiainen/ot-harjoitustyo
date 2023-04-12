from tkinter import ttk, constants
from service.service_budget import service_budget


class BudgetListView:

    def __init__(self, root, budgets):
        self._root = root
        self._budgets = budgets
        self._frame = None

        self._initialize()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        for budget in self._budgets:
            self._initialize_budget(budget)

    def _initialize_budget(self, budget):
        budget_frame = ttk.Frame(master=self._frame)
        label = ttk.Label(master=budget_frame, text=budget.content)

        label.grid(row=0, column=0, padx=5, pady=5, sticky=constants.W)
        budget_frame.grid_columnconfigure(0, weight=1)
        budget_frame.pack(fill=constants.X)

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()


class BudgetsView:
    def __init__(self, root, handle_logout):
        self._root = root
        self._handle_logout = handle_logout
        self._user = service_budget.current_user()
        self._frame = None
        self._create_entry = None
        self._budget_frame = None
        self._budget_view = None

        self._initialize()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._budget_frame = ttk.Frame(master=self._frame)
        self._initialize_header()
        self._initialize_budget_list()
        self._initialize_footer()

        self._budget_frame.grid(
            row=1,
            column=0,
            columnspan=2,
            sticky=constants.EW
        )

        self._frame.grid_columnconfigure(0, weight=1, minsize=400)
        self._frame.grid_columnconfigure(1, weight=0)

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _logout_handle(self):
        service_budget.logout()
        self._handle_logout()

    def _handle_create(self):
        budget_content = self._create_entry.get()
        if budget_content:
            service_budget.create_budget(budget_content)
            self._initialize_budget_list()
            self._create_entry.delete(0, constants.END)

    def _initialize_budget_list(self):
        if self._budget_view:
            self._budget_view.destroy()

        budgets = service_budget.get_budgets()

        self._budget_view = BudgetListView(
            self._budget_frame,
            budgets
        )

        self._budget_view.pack()

    def _initialize_header(self):
        user_label = ttk.Label(master=self._frame, text=f"Logged in as {self._user}")
        logout_button = ttk.Button(master=self._frame, text="Logout", command=self._handle_logout)

        user_label.grid(row=0, column=0, padx=5, pady=5, sticky=constants.W)
        logout_button.grid(row=0, column=1, padx=5, pady=5, sticky=constants.EW)

    def _initialize_footer(self):
        self._create_entry = ttk.Entry(master=self._frame)

        create_button = ttk.Button(master=self._frame, text="Create", command=self._handle_create)
        self._create_entry.grid(
            row=2,
            column=0,
            padx=5,
            pady=5,
            sticky=constants.EW
        )
        create_button.grid(
            row=2,
            column=1,
            padx=5,
            pady=5,
            sticky=constants.EW
        )
