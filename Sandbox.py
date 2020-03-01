
import engine
import pygame

class testScene (engine.Scene):

    def Update(self) -> None:
        print(0)

class Sandbox (engine.Application):

    def __init__(self):
        super().__init__()
        self._scene_factory = engine.SceneFactory()
        self._scene_factory.PushScene("default_scene", testScene())
        engine._current_scene = "default_scene"

        self._window = engine.Window()
        self._window.Create()

        engine.EventsEmmiter().BindCallback(pygame.QUIT, self.Close)
        id = engine.EventsEmmiter().BindCallback(pygame.K_a, print)
        engine.EventsEmmiter().BindArgs(pygame.K_a, id, ["Hello"])

    def Update(self) -> None:
        self._scene_factory.Update()
        self._window.Update()
        engine.EventsListener().Update()

    def Render(self) -> None:
        self._scene_factory.Render()
        self._window.Render()

engine.StartApplication(Sandbox)
