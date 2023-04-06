from user_interface.login_view import Login
from user_interface.create_user import CreateUser


class UI:
    def __init__(self, root):
        self._root = root
        self._current = None

    def start(self):
        self._login_show()

    def _hide_current(self):
        if self._current:
            self._current.destroy()

        self._current = None

    def _login_show(self):
        self._hide_current()

        self._current = Login(
            self._root,
            self._create_user_show()
        )

        self._current.pack()

    def _create_user_show(self):
        self._hide_current()

        self._current = CreateUser(
            self._root,
            self._login_show()
        )

        self._current.pack()




