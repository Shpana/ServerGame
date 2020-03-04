
import engine
import pygame

class JoinGameMenu (engine.Scene):

    def __init__(self):
        super().__init__()
        self._text_label = engine.Label(
        x = 400, y = 250, text = "Enter ID here", font_size = 40)

        self._test_line_input = engine.LineInput(
        x = 400, y = 300, width = 400, height = 50)

        self._submit_button = engine.Button(
        x = 525, y = 400, width = 150, height = 50, text = "JOIN")

        self._back_button = engine.Button(
        x = 275, y = 400, width = 150, height = 50, text = "BACK")
        self._back_button.BindCallback(engine._scene_factory.SetPreviousScene)

    def Enable(self) -> None:
        self.PushObject(self._test_line_input)
        self.PushObject(self._text_label)
        self.PushObject(self._submit_button)
        self.PushObject(self._back_button)

    def Update(self) -> None:
        super().Update()

    def Render(self) -> None:
        super().Render()

    def Disable(self) -> None:
        pass
