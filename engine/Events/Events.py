
import engine
import pygame

def ToggleMousePressed() -> None:
    engine._mouse_pressed = not engine._mouse_pressed

def ToggleKeyPressed() -> None:
    engine._key_pressed = not engine._key_pressed

def Init() -> None:
    # Мышь
    engine.EventsEmmiter().BindCallback(pygame.MOUSEBUTTONDOWN, ToggleMousePressed)
    engine.EventsEmmiter().BindCallback(pygame.MOUSEBUTTONUP, ToggleMousePressed)

    # Клавиатура
    engine.EventsEmmiter().BindCallback(pygame.KEYDOWN, ToggleKeyPressed)
    engine.EventsEmmiter().BindCallback(pygame.KEYUP, ToggleKeyPressed)
