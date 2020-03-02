
import engine
import pygame

class Button (engine.Widget):

    def __init__(self, **kwargs):
        super().__init__()
        self._color       = (150, 150, 250)
        self._press_color = (100, 100, 200)
        self._hover_color = (125, 125, 225)
        self._text        = "Button"
        self.SetOptions(kwargs)

        self._label      = engine.Label(
            x = self._x, y = self._y, text = self._text
        )
        self._is_hovered = False
        self._is_pressed = False
        self._is_ready   = True
        self._rect       = None
        self._callback   = [0, []]
        self._current_color = self._color
        self.SetRectangle()

    def Update(self) -> None:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        self._is_hovered = self._rect.collidepoint(mouse_x, mouse_y)
        if (self._is_hovered): self.CheckPress()

    def Render(self) -> None:
        if (self._is_pressed): self._current_color = self._press_color
        elif (self._is_hovered): self._current_color = self._hover_color
        else: self._current_color = self._color
        pygame.draw.rect(engine._window_surface, self._current_color, self._rect)
        self._label.Render()

    def BindFunction(self, func, args = []) -> None:
        self._callback[0] = func
        self._callback[1] = args

    def SetRectangle(self) -> None:
        self._rect = pygame.Rect(
            self._x - self._width // 2, self._y - self._height // 2,
            self._width, self._height
        )

    def CheckPress(self) -> None:
        self._is_pressed = engine._mouse_pressed
        if (self._is_pressed and self._is_ready): self.DoCallback()
        else: self._is_ready = not self._is_pressed

    def DoCallback(self) -> None:
        self._callback[0](self._callback[1])
        self._is_ready = False
