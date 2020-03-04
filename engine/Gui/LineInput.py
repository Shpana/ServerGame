
import engine
import pygame
import keyboard

class LineInput (engine.Widget):

    def __init__(self, **kwargs):
        super().__init__()
        self._color = (150, 150, 255)
        self.SetOptions(kwargs)

        self._label        = engine.Label(
        x = self._x, y = self._y, text = "")
        self._is_focused   = False
        self._is_hovered   = False
        self._rect         = None
        self._offset       = 2
        self._text         = ""
        self._pressed_keys = {
        "0": 0, "1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0,
        "8": 0, "9": 0, "backspace": 0, ".": 0}
        self.SetRectangle()

    def Update(self) -> None:
        if (self._is_focused): self.InputHandle()

        mouse_x, mouse_y = pygame.mouse.get_pos()
        self._is_hovered = self._rect.collidepoint(mouse_x, mouse_y)
        if (engine._mouse_pressed): self._is_focused = self._is_hovered

        if (self._is_focused): self._offset = 4
        else: self._offset = 2

    def Render(self) -> None:
        pygame.draw.rect(engine._window_surface, self._color, self._rect, self._offset)
        self._label.Render()

    def SetRectangle(self) -> None:
        self._rect = pygame.Rect(
            self._x - self._width // 2, self._y - self._height // 2,
            self._width, self._height
        )

    def InputHandle(self) -> None:
        for key in self._pressed_keys:
            temp = keyboard.is_pressed(key)
            was_pressed = self._pressed_keys[key]
            self._pressed_keys[key] = temp
            if (key == "backspace" and self._text != "" and temp and not was_pressed):
                self._text = self._text[0:len(self._text) - 1]
            elif (temp and key != "backspace" and not was_pressed): self._text += key

            if (temp):
                self._label._text = self._text
                self._label.SetTextStyle()
