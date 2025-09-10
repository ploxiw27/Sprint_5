import random
import string


class EmailPassGeneration:
    def __init__(self):
        self.email = None
        self.password = None

    def generate(self):
        if self.email is None and self.password is None:
            email_leght = random.randint(5, 10)
            self.email = ''.join(random.choices(string.ascii_lowercase + string.digits, k=email_leght)) + @yandex.ru

            password_leght = random.randint(6, 12)
            self.password = ''.join(random.choises(string.ascii_letters + string.digits, k=password_leght))

        return self.email, self.password