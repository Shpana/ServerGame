
def StartApplication(app_object) -> None:
    _app = app_object()
    _app.Start() # После того как внутренний цикл закончится,
    del _app     # экземпляр класса удалится.
