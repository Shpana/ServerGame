
import engine

class SceneFactory ():

    def __init__(self):
        self._scenes = dict()

    def Update(self) -> None:
        self._scenes[engine._current_scene].Update()

    def Render(self) -> None:
        self._scenes[engine._current_scene].Render()

    def PushScene(self, name, scene) -> None:
        self._scenes[name] = scene

    def PopScene(self, name) -> None:
        self._scenes.pop(name)

    def SetCurrentScene(self, name) -> None:
        self._scenes[engine._current_scene].Off() if engine._current_scene else None
        engine._current_scene = name
        self._scenes[engine._current_scene].On()
