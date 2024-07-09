from core.server.protocol import Protocol
from core.server.requests import GetRequest, SendRequest, NewRequest, DelRequest, EditRequest


def session():
    print("Starting session...")
    while True:
        print("Enter a request:")
        request = input("> ").split(" ", 1)
        print(request)
        match request[0]:
            case "GET":
                request = GetRequest(request[1])
            case "SEND":
                request = SendRequest(request[1])
            case "NEW":
                request = NewRequest(request[1])
            case "DEL":
                request = DelRequest(request[1])
            case "EDIT":
                request = EditRequest(request[1])
            case _:
                print("Invalid request type.")
                continue

        protocol = Protocol(request)
        print(protocol.parse())

