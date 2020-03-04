
import engine
import pygame

from StartMenu          import StartMenu
from SettingsMenu       import SettingsMenu
from CreateNewGameMenu  import CreateNewGameMenu
from JoinGameMenu       import JoinGameMenu

class Sandbox (engine.Application):

    def __init__(self):
        super().__init__()
        engine._scene_factory.PushScene("start_menu", StartMenu())
        engine._scene_factory.PushScene("settings_menu", SettingsMenu())
        engine._scene_factory.PushScene("create_new_game_menu", CreateNewGameMenu())
        engine._scene_factory.PushScene("join_the_game_menu", JoinGameMenu())
        engine._scene_factory.SetCurrentScene("start_menu")

        self._window = engine.Window()
        self._window.Create()

        engine.EventsEmmiter().BindCallback("QUIT", self.Close)
        engine.EventsEmmiter().BindCallback(pygame.QUIT, self.Close)

    def Update(self) -> None:
        engine.EventsListener().Update()
        self._window.Update()
        engine._scene_factory.Update()

    def Render(self) -> None:
        self._window.Render()
        engine._scene_factory.Render()

engine.StartApplication(Sandbox)
