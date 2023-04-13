from tkinter import ttk, StringVar, constants
from service.service_budget import service_budget, InvalidCredentialsError

class LoginView:

    def __init__(self, root, login_handle, create_user):
        self._root = root
        self._login_handle = login_handle
        self._create_user = create_user
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

    def _login_handler(self):
        username = self._username_entry.get()
        password = self._password_entry.get()

        try:
            service_budget.login(username, password)
            self._login_handle()
        except InvalidCredentialsError:
            self._show_error("Wrong username or password")

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
        password_label = ttk.Label(master=self._root, text="Password")
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

        login_button = ttk.Button(
            master=self._frame,
            text="Login",
            command=self._login_handle
        )

        user_button = ttk.Button(
            master=self._frame,
            text="Create user",
            command=self._create_user
        )

        self._frame.grid_columnconfigure(0, weight=1, minsize=400)

        login_button.grid(padx=5, pady=5, sticky=constants.EW)
        user_button.grid(padx=5, pady=5, sticky=constants.EW)

        self._remove_error()


