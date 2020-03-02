
import sys

class Application ():

    def __init__(self):
        self._running = True

    def Start(self) -> None:
        pass

    def Update(self) -> None:
        pass

    def Render(self) -> None:
        pass

    def Close(self) -> None:
        self._running = False
        sys.exit()

    def Run(self) -> None:
        self.Start()
        while (self._running):
            self.Update()
            self.Render()
