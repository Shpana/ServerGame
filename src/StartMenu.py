
import engine
import pygame

class StartMenu (engine.Scene):

    def __init__(self):
        super().__init__()
        self._dicor_label = engine.Label(
        x = 400, y = 100, text = "SERVER GAME", font_size = 75)

        self._create_button = engine.Button(
        x = 400, y = 200, width = 250, height = 50, text = "Create a game")
        self._create_button.BindCallback(engine._scene_factory.SetCurrentScene, ["create_game_menu"])

        self._join_button = engine.Button(
        x = 400, y = 300, width = 250, height = 50, text = "Join the game")
        self._join_button.BindCallback(engine._scene_factory.SetCurrentScene, ["join_the_game_menu"])

        self._settings_button = engine.Button(
        x = 400, y = 400, width = 250, height = 50, text = "Settings")
        self._settings_button.BindCallback(engine._scene_factory.SetCurrentScene, ["settings_menu"])

        self._quit_button = engine.Button(
        x = 400, y = 500, width = 250, height = 50, text = "Quit")
        self._quit_button.BindCallback(engine.EventsEmmiter().Emit, ["QUIT"])

    def Enable(self) -> None:
        self.PushObject(self._dicor_label)
        self.PushObject(self._create_button)
        self.PushObject(self._join_button)
        self.PushObject(self._settings_button)
        self.PushObject(self._quit_button)

    def Update(self) -> None:
        super().Update()

    def Render(self) -> None:
        super().Render()

    def Disable(self) -> None:
        pass
