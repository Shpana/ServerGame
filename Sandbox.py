
import engine
import pygame

from src.StartMenu          import StartMenu
from src.SettingsMenu       import SettingsMenu
from src.CreateGameMenu     import CreateGameMenu
from src.JoinGameMenu       import JoinGameMenu
from src.WaitRoom           import WaitRoom
from src.Game               import Game

class Sandbox (engine.Application):

    def __init__(self):
        super().__init__()
        engine._scene_factory.PushScene("start_menu", StartMenu())
        engine._scene_factory.PushScene("settings_menu", SettingsMenu())
        engine._scene_factory.PushScene("create_game_menu", CreateGameMenu())
        engine._scene_factory.PushScene("join_the_game_menu", JoinGameMenu())
        engine._scene_factory.PushScene("wait_room", WaitRoom())
        engine._scene_factory.PushScene("game", Game())
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
