
class Scene ():

    def __init__(self):
        self._objects_buffer = []

    def Enable(self) -> None:
        pass

    def Update(self) -> None:
        for obj in self._objects_buffer: obj.Update()

    def Render(self) -> None:
        for obj in self._objects_buffer: obj.Render()

    def Disable(self) -> None:
        pass

    def PushObject(self, object) -> int:
        self._objects_buffer.append(object)
        return len(self._objects_buffer) - 1

    def ClearObjectBuffer(self) -> None:
        self._objects_buffer = []
