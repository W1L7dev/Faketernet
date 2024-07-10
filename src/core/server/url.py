#############################################
#   URL.py   #   url maker for the server   #
#############################################

import random
import string


class UrlArgument:
    def __init__(self, key: str, value: str):
        self.key = key
        self.value = value

    def __str__(self):
        return f"{self.key}={self.value}"

    def __repr__(self):
        return f"UrlArgument({self.key}, {self.value})"

class Url:
    def __init__(self, url: str):
        self.url = url
        self.args = self.url.split("?")[1].split("&") if "?" in self.url else []

    def __str__(self):
        return self.url

    def __repr__(self):
        return f"Url({self.url})"

    def generate(self):
        self.url = "".join(random.choices(string.ascii_letters + string.digits, k=8))
        return self

    def add_argument(self, argument: UrlArgument):
        self.args.append(argument)
        return self
