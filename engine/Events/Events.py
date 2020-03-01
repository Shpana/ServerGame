
import engine
import pygame

def ToggleMousePressed() -> None:
    engine._mouse_pressed = not engine._mouse_pressed

def Init() -> None:
    engine.EventsEmmiter().BindCallback(pygame.MOUSEBUTTONDOWN, ToggleMousePressed)
    engine.EventsEmmiter().BindCallback(pygame.MOUSEBUTTONUP, ToggleMousePressed)
