
import engine
import pygame

class Label (engine.Widget):

    def __init__(self, **kwargs):
        self._text       = "Label"
        self._text_color = (255, 255, 255)
        self._font_name  = "Menlo"
        self._font_size  = 30
        self._font_object = None
        self._text_object = None
        self.SetOptions(kwargs)
        self.SetTextStyle()

    def Render(self) -> None:
        _place = self._text_object.get_rect(center = (self._x, self._y))
        engine._window_surface.blit(self._text_object, _place)

    def SetTextStyle(self) -> None:
        self._font_object = pygame.font.SysFont(self._font_name, self._font_size)
        self._text_object = self._font_object.render(self._text, 1, self._text_color)    
