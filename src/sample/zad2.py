
import string


class Password:
    def __init__(self):
        self.special_characters = set(string.punctuation.replace("_", ""))

    def ValidPassword(self, password):
        if not isinstance(password, str):
            raise TypeError("Password is not of type string!")

        if len(password) >= 8:
            if any(x.isupper() for x in password) and any(x.isdigit() for x in password) and any(
                    x in self.special_characters for x in password):
                return True
            else:
                return False
        else:
            return False
