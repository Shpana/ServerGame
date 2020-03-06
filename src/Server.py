
import socket
import engine
import sys
import pickle

class Server (object):

    def __init__(self, host = "localhost"):
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self._sock.bind((host, 9090))
        self._clients = []
        self._running = True
        print("Server Start")

    def Run(self) -> None:
        while engine._running:
            _data, _addr = self._sock.recvfrom(4096)

            if (_addr not in self._clients):
                self._clients.append(_addr)
                print(f"Connection from {_addr}.")

            data = pickle.loads(_data)

            for client in self._clients:
                if (_addr != client):
                    self._sock.sendto(_data, client)

        self._sock.close()


def StartServer(server) -> None:
    import threading
    engine._server_thread = threading.Thread(target = server.Run)
    engine._server_thread.start()
