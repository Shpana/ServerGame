
import pygame
import os
import sys
import engine

class Window (object):

    def __init__(self, **kwargs):
        self._width         = 800
        self._height        = 600
        self._title         = "Server Game"
        self._bg_color      = (18, 19, 25)
        self._center_align  = True
        self._frame_rate    = 60
        self._surface       = None
        self.SetOptions(kwargs)

    def Update(self) -> None:
        pygame.display.flip()
        pygame.time.Clock().tick(self._frame_rate)

    def Render(self) -> None:
        self._surface.fill(self._bg_color)

    def Close(self) -> None:
        sys.exit(0)

    def Create(self) -> None:
        if (self._center_align): os.environ["SDL_VIDEO_CENTERED"] = "1"
        self._surface = pygame.display.set_mode((self._width, self._height))
        self.SetTitle(self._title)

        engine._window_width   = self._width
        engine._window_height  = self._height
        engine._window_surface = self._surface

    def SetOptions(self, kwargs) -> None:
        # "_" + key, исользую потому что я все локальные переменные класса
        # помечаю 'оператором' нижнее подчёркивание. Это не обязательно.
        for key in kwargs: self.__dict__["_" + key] = kwargs[key]

    def SetTitle(self, value) -> None:
        pygame.display.set_caption(value)
