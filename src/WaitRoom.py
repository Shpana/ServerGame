
import engine
import pygame
from src.Server import Server
from src.Server import StartServer

class WaitRoom (engine.Scene):

    def __init__(self):
        super().__init__()
        self._ready_label = engine.Label(
        x = 400, y = 150, text = "Are you ready?", font_size = 100)

        self._ready_button = engine.Button(
        x = 525, y = 500, width = 150, height = 50, text = "I'm ready!")
        self._ready_button.BindCallback(self.ReadyCallback)

        self._back_button = engine.Button(
        x = 275, y = 500, width = 150, height = 50, text = "No, I'm not.")
        self._back_button.BindCallback(self.BackCallback)

    def Enable(self) -> None:
        self.PushObject(self._back_button)
        self.PushObject(self._ready_button)
        self.PushObject(self._ready_label)

    def Update(self) -> None:
        super().Update()

    def Render(self) -> None:
        super().Render()

    def Disable(self) -> None:
        pass

    def BackCallback(self) -> None:
        engine._scene_factory.SetCurrentScene("start_menu")
        self._server = None

    def ReadyCallback(self) -> None:
        if (engine._type_of_connect == "server"):
            engine._server = Server(engine._host)
            StartServer(engine._server)
        engine._scene_factory.SetCurrentScene("game")
