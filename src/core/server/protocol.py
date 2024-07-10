##################################################
#   PROTOCOL.py   #   HTTP-like protocol         #
##################################################

from core.server.requests import Request
class Protocol:
    def __init__(self, request: Request):
        self.request = request

    def parse(self):
        url = self.request.request
        if "?" in url:
            url, args = url.split("?")
            args = args.split("&")
            args = {arg.split("=")[0]: arg.split("=")[1] for arg in args}
        else:
            args = {}

        return url, args
