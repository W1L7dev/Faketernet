class Request:
    def __init__(self, type: str, request: str):
        self.type = type
        self.request = request

    def __str__(self):
        return f"{self.type} {self.request}"

    def __repr__(self):
        return f"Request({self.type}, {self.request})"

    def __getitem__(self, index):
        return self.request[index]

    def split(self, separator: str):
        return tuple(self.request.split(separator))

class GetRequest(Request):
    def __init__(self, request: str):
        super().__init__("GET", request)

class SendRequest(Request):
    def __init__(self, request: str):
        super().__init__("SEND", request)

class NewRequest(Request):
    def __init__(self, request: str):
        super().__init__("NEW", request)

class DelRequest(Request):
    def __init__(self, request: str):
        super().__init__("DEL", request)

class EditRequest(Request):
    def __init__(self, request: str):
        super().__init__("EDIT", request)