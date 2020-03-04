
import engine

class SceneFactory ():

    def __init__(self):
        self._scenes = dict()
        self._previous_scene = None

    def Update(self) -> None:
        self._scenes[engine._current_scene].Update()

    def Render(self) -> None:
        self._scenes[engine._current_scene].Render()

    def PushScene(self, name, scene) -> None:
        self._scenes[name] = scene

    def PopScene(self, name) -> None:
        self._scenes.pop(name)

    def SetCurrentScene(self, name) -> None:
        self._scenes[engine._current_scene].Disable() if engine._current_scene else None
        self._previous_scene = engine._current_scene if engine._current_scene else None
        engine._current_scene = name
        self._scenes[engine._current_scene].Enable()

    def SetPreviousScene(self):
        self._scenes[engine._current_scene].Disable() if engine._current_scene else None
        _temp = engine._current_scene
        engine._current_scene = self._previous_scene
        self._previous_scene = _temp
        self._scenes[engine._current_scene].Enable()
