
import engine
import pygame

class Button (engine.Widget):

    def __init__(self, **kwargs):
        super().__init__()
        self._path       = None
        self.SetOptions(kwargs)

        self._is_hovered = False
        self._is_pressed = False
        self._is_ready   = True
        self._sprite     = None
        self._rect       = None
        self._callback   = [0, []]
        self.SetSprite()

    def Update(self) -> None:
        mouse_x, mouse_y = pygame.mouse.get_pos()

        self._is_hovered = self._rect.collidepoint(mouse_x, mouse_y)
        self._is_pressed = engine._mouse_pressed

        if (self._is_hovered and self._is_pressed and self._is_ready):
            self._callback[0](self._callback[1])
            self._is_ready = False

        else: self._is_ready = not self._is_pressed

    def Render(self) -> None:
        if (self._is_pressed): engine.ChangeAlpha(self._sprite, 150)
        elif (self._is_hovered): engine.ChangeAlpha(self._sprite, 200)
        else: engine.ChangeAlpha(self._sprite, 255)

        engine._window_surface.blit(self._sprite, (self._x, self._y))

    def BindFunction(self, func, args = []) -> None:
        self._callback[0] = func
        self._callback[1] = args

    def SetSprite(self) -> None:
        self._sprite = pygame.image.load(self._path)
        self._sprite = pygame.transform.scale(self._sprite, (self._width, self._height))
        self._rect   = pygame.Rect(self._x, self._y, self._width, self._height)
