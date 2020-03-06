
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
        x = 525, y = 400, width = 150, height = 50, text = "Join")
        self._submit_button.BindCallback(self.Submit)

        self._back_button = engine.Button(
        x = 275, y = 400, width = 150, height = 50, text = "Back")
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

    def Submit(self) -> None:
        if (self._test_line_input._text != ""): engine._host = self._test_line_input._text
        else: engine._host = "localhost"
        engine._type_of_connect = "client"
        engine._player = engine._scene_factory._scenes["game"]
        engine._player._matrix = engine.Matrix(engine._player._cols, engine._player._rows)
        engine._player._matrix[0] = 2
        engine._player._matrix[engine._player._cols * engine._player._rows - 1] = 1
        engine._player._current_area = "?"
        engine._player._current_player = 2
        engine._player._count_of_turns = 1
        engine._scene_factory.SetCurrentScene("wait_room")
