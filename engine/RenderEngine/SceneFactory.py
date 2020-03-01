

class SceneFactory ():

    def __init__(self):
        self._scenes = dict()

    def Update(self) -> None:
        from engine import _current_scene
        self._scenes[_current_scene].Update()

    def Render(self) -> None:
        from engine import _current_scene
        self._scenes[_current_scene].Render()

    def PushScene(self, name, scene) -> None:
        self._scenes[name] = scene

    def PopScene(self, name) -> None:
        self._scenes.pop(name)

    def SetCurrentScene(self, name) -> None:
        from engine import _current_scene
        _current_scene = name
