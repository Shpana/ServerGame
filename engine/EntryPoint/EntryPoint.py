
import engine
import threading

def StartApplication(app_object) -> None:
    _app = app_object()
    _app.Run()  # После того как внутренний цикл закончится,
    del _app     # экземпляр класса удалится.
