from user_interface.login_view import Login
from user_interface.create_user import CreateUser


class UI:
    def __init__(self, root):
        self._root = root
        self._current = None

    def start(self):
        self._login_view()

    def _create_user(self):
        self._hide_current()

        self._current = CreateUser(
            self._root,
            self._login_view
        )

        self._current.pack()

    def _login_view(self):
        self._hide_current()

        self._current = Login(
            self._root,
            self._create_user
        )

        self._current.pack()

    def _hide_current(self):
        if self._current:
            self._current.destroy()

        self._current = None


