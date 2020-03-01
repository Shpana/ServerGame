
import pygame
pygame.font.init()

# Entry Point
from engine.EntryPoint.EntryPoint       import StartApplication
from engine.EntryPoint.Application      import Application

# Render Engine
_current_scene  = None
_window_width   = None
_window_height  = None
_window_surface = None
from engine.RenderEngine.Window         import Window
from engine.RenderEngine.SceneFactory   import SceneFactory
from engine.RenderEngine.Scene          import Scene

# Utils
from engine.Utils.Matrix                import Matrix

# Events
_events = dict()
from engine.Events.EventsEmmiter        import EventsEmmiter
from engine.Events.EventsListener       import EventsListener

# GUI
from engine.Gui.Label                   import Label
