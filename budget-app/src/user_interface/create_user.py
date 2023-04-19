from tkinter import ttk, StringVar, constants
from service.service_budget import service_budget, UsernameExistsError


class CreateUser:

    def __init__(self, root, create_user, show_login):
        self._root = root
        self._create_user = create_user
        self._show_login = show_login
        self._frame = None
        self._username_entry = None
        self._password_entry = None
        self._error_var = None
        self._error_label = None

        self._initialize()

    def grid(self, **kwargs):
        self._frame.grid(kwargs)

    def destroy(self):
        self._frame.destroy()

    def _user_handler(self):
        username = self._username_entry.get()
        password = self._password_entry.get()

        if not username or not password:
            self._show_error("Username and password are required!")
            return

        try:
            service_budget.create_user(username, password, login=True)
            self._create_user()
        except UsernameExistsError:
            self._show_error(f"Username {username} already exists")

    def _show_error(self, message):
        self._error_var.set(message)
        self._error_label.grid(row=0, column=0, padx=5, pady=5)

    def _remove_error(self):
        self._error_label.grid_remove()

    def _initialize_username(self):
        username_label = ttk.Label(master=self._frame, text="Username")
        self._username_entry = ttk.Entry(master=self._frame)
        username_label.grid(row=1, column=0, padx=5, pady=5)
        self._username_entry.grid(row=1, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)

    def _initialize_password(self):
        password_label = ttk.Label(master=self._frame, text="Password")
        self._password_entry = ttk.Entry(master=self._frame)
        password_label.grid(row=2, column=0, padx=5, pady=5)
        self._password_entry.grid(row=2, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        self._error_var = StringVar(self._frame)
        self._error_label = ttk.Label(
            master=self._frame,
            textvariable=self._error_var,
            foreground="orange"
        )
        self._error_label.grid(row=1, column=0, columnspan=2,padx=5, pady=5)

        self._initialize_username()
        self._initialize_password()

        ttk.Label(master=self._frame).grid(row=2)

        create_button = ttk.Button(
            master=self._frame,
            text="Create user",
            command=self._user_handler
        )

        login_button = ttk.Button(
            master=self._frame,
            text="Back to login page",
            command=self._show_login
        )

        self._frame.grid_columnconfigure(1, weight=1, minsize=400)

        create_button.grid(columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)
        login_button.grid(columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)

        self._remove_error()
