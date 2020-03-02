
class Widget (object):

    def __init__(self):
        self._x      = None
        self._y      = None
        self._width  = None
        self._height = None

    def Update(self) -> None:
        pass

    def Render(self) -> None:
        pass

    def SetOptions(self, kwargs) -> None:
        # "_" + key, исользую потому что я все локальные переменные класса
        # помечаю 'оператором' нижнее подчёркивание. Это не обязательно.
        for key in kwargs: self.__dict__["_" + key] = kwargs[key]
