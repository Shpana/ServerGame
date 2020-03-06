
import os
import sys
import threading
import engine

class Application ():

    def __init__(self):
        self._running = True
        threading.Thread.__init__(self)

    def Start(self) -> None:
        pass

    def Update(self) -> None:
        pass

    def Render(self) -> None:
        pass

    def Close(self) -> None:
        self._running = False
        engine._running = False
        os.abort()
        sys.exit()

    def Run(self) -> None:
        self.Start()
        while (self._running):
            self.Update()
            self.Render()

        engine._running = False
        del engine._server_thread
