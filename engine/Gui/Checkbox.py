
import engine
import pygame

class Checkbox (engine.Widget):

    def __init__(self, **kwargs):
        self._color = (150, 150, 255)
        self.SetOptions(kwargs)

        self._width      = 40
        self._height     = 40
        self._rect       = None
        self._checked    = False
        self._is_hovered = False
        self._is_pressed = False
        self._is_ready   = True
        self.SetRectangle()

    def Update(self) -> None:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        self._is_hovered = self._rect.collidepoint(mouse_x, mouse_y)
        self._is_pressed = engine._mouse_pressed
        if (self._is_hovered and self._is_pressed and self._is_ready): self.ToggleChecked()
        else: self._is_ready = not self._is_pressed

    def Render(self) -> None:
        if (self._checked): pygame.draw.rect(engine._window_surface, self._color, self._rect)
        else: pygame.draw.rect(engine._window_surface, self._color, self._rect, 1)

    def ToggleChecked(self) -> None:
        self._checked = not self._checked
        self._is_ready = False

    def SetRectangle(self) -> None:
        self._rect = pygame.Rect(
            self._x - self._width // 2, self._y - self._height // 2,
            self._width, self._height
        )

    def IsChecked(self) -> bool:
        return self._checked
