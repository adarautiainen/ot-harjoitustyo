from user_interface.login_view import LoginView
from user_interface.create_user import CreateUser
from user_interface.budgets_view import BudgetsView


class UI:
    """Luokka joka vastaa sovelluksen käyttöliittymästä"""

    def __init__(self, root):
        """Luokan konstruktori. Luo uuden luokan, joka vastaa käyttöliittymästä.

        Args:
            root: Tkinter-elementti, käyttöliittymä alustetaan sen sisälle.
        """

        self._root = root
        self._current = None

    def start(self):
        """Käynnistää käyttöliittymän."""

        self._login_show()

    def _hide_current(self):
        if self._current:
            self._current.destroy()

        self._current = None

    def _login_show(self):
        self._hide_current()

        self._current = LoginView(
            self._root,
            self._budgets_show,
            self._create_user_show
        )

        self._current.grid()

    def _budgets_show(self):
        self._hide_current()
        self._current = BudgetsView(self._root, self._login_show)
        self._current.grid()

    def _create_user_show(self):
        self._hide_current()

        self._current = CreateUser(
            self._root,
            self._budgets_show,
            self._login_show
        )

        self._current.grid()




