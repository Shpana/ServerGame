
from engine import _events

class EventsEmmiter ():

    @staticmethod
    def BindCallback(type, callback) -> int:
        if (not type in _events.keys()): _events[type] = []
        _events[type].append([callback, []])
        return len(_events[type]) - 1

    @staticmethod
    def BindArgs(type, id, args) -> None:
        _events[type][id][1] = args

    @staticmethod
    def UnbindCallback(type, id):
        if (type in _events.keys()): _events[type].pop(id)

    @staticmethod
    def Emit(type) -> None:
        if (type in _events.keys()):
            for event in _events[type]:
                callback = event[0]
                args = event[1]
                callback(*args)
