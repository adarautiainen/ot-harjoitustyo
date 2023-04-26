class User:
    """Tämä luokka kuvaa käyttäjää.

    Attributes:
        username: Merkkijono, joka kuvaa käyttäjätunnusta.
        password: Merkkijono, joka kuvaa salasanaa.
    """

    def __init__(self, username, password):
        """Luokan konstruktori luo uuden käyttäjän.

        Args:
            username: Merkkijono, joka kuvaa käyttäjätunnusta.
            password: Merkkijono, joka kuvaa salasanaa.
        """

        self.username = username
        self.password = password
