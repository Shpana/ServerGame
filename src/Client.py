
import threading
import socket
import engine
import pickle
from random import randint

class Client (object):

    def __init__(self):
        self._server = (engine._host, 9090)
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self._sock.bind((engine._host, 0))
        self._thread = threading.Thread(target = self.Update)
        self._thread.start()
        self.SendMessage("")

    def SendMessage(self, data = []) -> None:
        data = pickle.dumps(data)
        self._sock.sendto(data, self._server)

    def Update(self) -> None:
        while (True):
            _data, _addr = self._sock.recvfrom(4096)
            data = pickle.loads(_data)
            print(type(data))
            if (type(data) != list):
                continue

            mass = engine.Matrix(data[0]._cols, data[0]._rows)

            for i in range(len(data[0])):
                if (data[0][i] == 1): mass[i] = 2
                elif (data[0][i] == 2): mass[i] = 1
                else: mass[i] = 0

            engine._player._matrix = mass
            engine._player._current_area = data[1]
            engine._player._current_player = 1
            engine._player._count_of_turns = 1
