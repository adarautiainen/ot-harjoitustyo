from tkinter import ttk, StringVar, constants
import tkinter as tk
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

    def grid(self, **kwargs):
        self._frame.grid(kwargs)

    def destroy(self):
        self._frame.destroy()

    def _login_handler(self):
        username = self._username_entry.get()
        password = self._password_entry.get()

        try:
            service_budget.login(username, password)
            self._login_handle()
        except InvalidCredentialsError:
            self._show_error("Wrong username or password! Try again.")

    def _show_error(self, message):
        self._error_var.set(message)
        self._error_label.grid(row=0, column=0, padx=5, pady=5)

    def _remove_error(self):
        self._error_label.grid_remove()

    def _initialize_username(self):
        username_label = tk.Label(master=self._frame, text="Username")
        self._username_entry = ttk.Entry(master=self._frame)
        username_label.grid(row=1, column=0, padx=5, pady=5)
        self._username_entry.grid(row=1, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)

    def _initialize_password(self):
        password_label = tk.Label(master=self._frame, text="Password")
        self._password_entry = ttk.Entry(master=self._frame, show="*")
        password_label.grid(row=2, column=0, padx=5, pady=5)
        self._password_entry.grid(row=2, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)

    def _initialize(self):
        self._frame = tk.Frame(master=self._root)
        self._root.geometry("500x500")

        self._error_var = StringVar(self._frame)
        self._error_label = tk.Label(
            master=self._frame,
            textvariable=self._error_var,
            foreground="orange"
        )
        self._error_label.grid(row=1, column=0, columnspan=2,padx=5, pady=5)

        self._initialize_username()
        self._initialize_password()

        tk.Label(master=self._frame).grid(row=2)

        login_button = tk.Button(
            master=self._frame,
            text="Login",
            command=self._login_handler
        )

        user_button = tk.Button(
            master=self._frame,
            text="Create user",
            command=self._create_user
        )

        self._frame.grid_columnconfigure(1, weight=1, minsize=400)

        login_button.grid(columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)
        user_button.grid(columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)

        self._remove_error()
