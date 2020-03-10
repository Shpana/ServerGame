
import engine
import pygame

from random import randint
from src.Mesh import Mesh
from src.Client import Client

class Game (engine.Scene):

    def __init__(self):
        super().__init__()
        self._cols  = 20
        self._rows  = 20
        self._scale = 20
        self._matrix = engine.Matrix(self._cols, self._rows)
        self._matrix[0] =  1
        self._matrix[len(self._matrix) - 1] = 2

        self._was_cut = False
        self._is_cutting    = False
        self._start_cut_pos = [0, 0]
        self._end_cut_pos   = [0, 0]
        self._mesh = Mesh(self._cols, self._rows, self._scale)

        self._matrix_copy = [0] * len(self._matrix)

        self._current_player = 1
        self._current_area   = randint(1, 10)
        self._count_of_turns = 2

        self._current_area_label = engine.Label(
        x = 650, y = 200, text = f"Current area is {self._current_area}.")

        self._current_player_label = engine.Label(
        x = 650, y = 100, text = f"{self._current_player}'s player turn.")

        self._send_button = engine.Button(
        x = 650, y = 300, text = "Send", width = 150, height = 50)
        self._send_button.BindCallback(self.SendMessage)

        self._settings_button = engine.Button(
        x = 650, y = 400, width = 150, height = 50, text = "Settings")
        self._settings_button.BindCallback(engine._scene_factory.SetCurrentScene, ["settings_menu"])

        self._quit_button = engine.Button(
        x = 650, y = 500, width = 150, height = 50, text = "Quit")
        self._quit_button.BindCallback(self.Quit)

    def Enable(self) -> None:
        self.PushObject(self._current_area_label)
        self.PushObject(self._current_player_label)
        self.PushObject(self._send_button)
        self.PushObject(self._settings_button)
        self.PushObject(self._quit_button)
        self._client = Client()

    def Update(self) -> None:
        super().Update()
        self.Cut()
        self._mesh.Update()
        self.CutTerritory()

        self._current_player_label._text = f"{self._current_player}'s player turn."
        self._current_player_label.SetTextStyle()

        self._current_area_label._text = f"Current area is {self._current_area}."
        self._current_area_label.SetTextStyle()

        if (self._matrix.count(0) == 0):
            self.GameOver()

    def Render(self) -> None:
        self._mesh.RenderMatrix(self._matrix)
        self._mesh.Render()
        super().Render()

    def Disable(self) -> None:
        del self

    def Cut(self) -> None:
        self._was_cut = self._is_cutting
        self._is_cutting = pygame.mouse.get_pressed()[0]

        if (not self._was_cut and self._is_cutting):
            self._start_cut_pos = pygame.mouse.get_pos()
        elif (self._was_cut and not self._is_cutting):
            self._end_cut_pos = pygame.mouse.get_pos()

    def CutTerritory(self) -> None:
        if (self._count_of_turns > 0):
            if (self._was_cut and not self._is_cutting and \
            self._mesh._in_rect and self._current_player == 1):

                mpos = self._mesh.GetMatrixPos(self._start_cut_pos, self._end_cut_pos)
                code = self._matrix.FillRect(*mpos, self._current_area)
                print(code)
                if (code == 1): self._count_of_turns -= 1

    def GameOver(self) -> None:
        # TODO: Подвести итоги
        engine._server = None
        engine._player = None
        _max = max(self._matrix.count(1), self._matrix.count(2))
        if (_max == 2):
            print("Player 2 win. You ЛОХ!")
        else:
            print("НИХЕРАСИБЕ. Ты победил.")
        engine._scene_factory.SetCurrentScene("start_menu")

    def SendMessage(self) -> None:
        if (self._current_player == 1):
            self._current_player = 2
            self._count_of_turns = 0
            self._current_player_label._text = f"{self._current_player}'s player turn."
            self._current_player_label.SetTextStyle()
            self._client.SendMessage([self._matrix, randint(1, 10)])

    def Quit(self) -> None:
        self.__init__()
        if (engine._server != None):
            engine._server._sock.close()
        engine._scene_factory.SetCurrentScene("start_menu")
