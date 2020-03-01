
class Application ():

    def __init__(self):
        self._running = True

    def Create(self) -> None:
        pass

    def Update(self) -> None:
        pass

    def Render(self) -> None:
        pass

    def Close(self) -> None:
        self._running = False

    def Start(self) -> None:
        while (self._running):
            self.Update()
            self.Render()
