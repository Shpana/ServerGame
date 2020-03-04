
import engine
import pygame

class SettingsMenu (engine.Scene):

    def __init__(self):
        super().__init__()
        self._back_button = engine.Button(
        x = 400, y = 300, width = 250, height = 50, text = "BACK")
        self._back_button.BindCallback(engine._scene_factory.SetPreviousScene)

    def Enable(self) -> None:
        self.PushObject(self._back_button)

    def Update(self) -> None:
        super().Update()

    def Render(self) -> None:
        super().Render()

    def Disable(self) -> None:
        pass
