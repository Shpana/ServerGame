
import pygame
pygame.font.init()

_mouse_pressed    = False
_key_pressed      = False
_current_scene    = None
_window_width     = None
_window_height    = None
_window_surface   = None
_server           = None
_server_thread    = None
_player           = None
_host             = None
_running          = True
_type_of_connect  = None
_events           = dict()

# Entry Point
from engine.EntryPoint.EntryPoint       import StartApplication
from engine.EntryPoint.Application      import Application

# Render Engine
from engine.RenderEngine.Window         import Window
from engine.RenderEngine.SceneFactory   import SceneFactory
from engine.RenderEngine.Scene          import Scene
_scene_factory = SceneFactory()

# Utils
from engine.Utils.Matrix                import Matrix
from engine.Utils.ChangeAlpha           import ChangeAlpha

# Events
from engine.Events.EventsEmmiter        import EventsEmmiter
from engine.Events.EventsListener       import EventsListener
from engine.Events.Events               import Init

# GUI
from engine.Gui.Widget                  import Widget
from engine.Gui.Button                  import Button
from engine.Gui.Label                   import Label
from engine.Gui.Checkbox                import Checkbox
from engine.Gui.LineInput               import LineInput

Init()
