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

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _user_handler(self):
        username = self._username_entry.get()
        password = self._password_entry.get()

        if len(username) == 0 or len(password) == 0:
            self._show_error("Username and password is required")
            return

        try:
            service_budget.create_user(username, password)
            self._create_user()
        except UsernameExistsError:
            self._show_error(f"Username {username} already exists")

    def _show_error(self, message):
        self._error_var.set(message)
        self._error_label.grid()

    def _remove_error(self):
        self._error_label.grid_remove()

    def _initialize_username(self):
        username_label = ttk.Label(master=self._frame, text="Username")
        self._username_entry = ttk.Entry(master=self._frame)
        username_label.grid(padx=5, pady=5, sticky=constants.W)
        self._username_entry.grid(padx=5, pady=5, sticky=constants.EW)

    def _initialize_password(self):
        password_label = ttk.Label(master=self._root)
        self._password_entry = ttk.Entry(master=self._frame)
        password_label.grid(padx=5, pady=5, sticky=constants.W)
        self._password_entry.grid(padx=5, pady=5, sticky=constants.EW)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._error_var = StringVar(self._frame)
        self._error_label = ttk.Label(
            master=self._frame,
            textvariable=self._error_var,
            foreground="orange"
        )
        self._error_label.grid(padx=5, pady=5)

        self._initialize_username()
        self._initialize_password()

        create_button = ttk.Button(
            master=self._frame,
            text="Login",
            command=self._create_user
        )

        login_button = ttk.Button(
            master=self._frame,
            text="Login",
            command=self._show_login
        )

        self._frame.grid_columnconfigure(0, weight=1, minsize=400)

        create_button.grid(padx=5, pady=5, sticky=constants.EW)
        login_button.grid(padx=5, pady=5, sticky=constants.EW)

        self._remove_error()
