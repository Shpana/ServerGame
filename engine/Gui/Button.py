
import engine
import pygame

class Button (object):

    def __init__(self, **kwargs):
        self._x          = 0
        self._y          = 0
        self._width      = 50
        self._height     = 50
        self._path       = None
        self._surface    = None
        self._rect       = None
        self._callback   = None
        self._is_hovered = False
        self._is_pressed = False
        self._offset     = True
        self.SetOptions(kwargs)
        self.SetSprite()

    def Update(self) -> None:
        x, y = pygame.mouse.get_pos()
        if (self._rect.collidepoint(x, y)):
            self._is_hovered = True
            self._is_pressed = engine._mouse_pressed

            if (self._is_pressed and self._offset):
                self._offset = False
                self._callback[0](*self._callback[1])

            if (not self._is_pressed):
                self._offset = True
                
        else:
            self._is_hovered = False

    def Render(self) -> None:
        if (self._is_pressed):
            engine.ChangeAlpha(self._sprite, 150)

        elif (self._is_hovered):
            engine.ChangeAlpha(self._sprite, 200)

        else:
            engine.ChangeAlpha(self._sprite, 255)

        engine._window_surface.blit(self._sprite, (
        self._x, self._y
        ))

    def BindFunction(self, func, args = []):
        self._callback = [func, args]

    def SetOptions(self, kwargs) -> None:
        # "_" + key, исользую потому что я все локальные переменные класса
        # помечаю 'оператором' нижнее подчёркивание. Это не обязательно.
        for key in kwargs: self.__dict__["_" + key] = kwargs[key]

    def SetSprite(self) -> None:
        self._sprite = pygame.image.load(self._path)
        self._sprite = pygame.transform.scale(self._sprite, (self._width, self._height))
        self._rect = pygame.Rect(self._x, self._y, self._width, self._height)
