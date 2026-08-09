#!/usr/bin/python3

class User:
    """User class."""

    def __init__(self):
        self.__password = None

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        self.__password = value

    def is_valid_password(self, password):
        if not isinstance(password, str):
            return False
        return password == self.__password


if __name__ == "__main__":
    import doctest
    doctest.testmod()
