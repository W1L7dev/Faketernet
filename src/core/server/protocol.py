##################################################
#   PROTOCOL.py   #   HTTP-like protocol         #
##################################################

from core.server.requests import Request

class Protocol:
    def __init__(self, request: Request):
        self.request = request

    def parse(self):
        return self.request.split("&")