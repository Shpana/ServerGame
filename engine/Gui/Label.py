
import pygame
import engine

class Label (object):

    def __init__(self, **kwargs):
        self._x          = 0
        self._y          = 0
        self._text       = "Label"
        self._text_color = (150, 150, 255)
        self._font_name  = "Consolas"
        self._font_size  = 30
        self._font_object = None
        self._text_object = None
        self.SetOptions(kwargs)

        self.SetFont(self._font_name, self._font_size)

    def Render(self) -> None:
        _place = self._text_object.get_rect(center = (self._x, self._y))
        engine._window_surface.blit(self._text_object, _place)

    def SetOptions(self, kwargs) -> None:
        # "_" + key, исользую потому что я все локальные переменные класса
        # помечаю 'оператором' нижнее подчёркивание. Это не обязательно.
        for key in kwargs: self.__dict__["_" + key] = kwargs[key]

    def SetFont(self, font_name, font_size) -> None:
        self._font_object = pygame.font.SysFont(font_name, font_size)
        self._font_name = font_name
        self._font_size = font_size
        self.SetText(self._text, self._text_color)

    def SetText(self, text, text_color) -> None:
        self._text_object = self._font_object.render(text, 1, text_color)
        self._text = text
        self._text_color = text_color
