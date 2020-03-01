
from engine import EventsEmmiter
from engine import _events
import pygame

class EventsListener ():

    @staticmethod
    def Update() -> None:
        for event in pygame.event.get():
            if (event.type in _events): EventsEmmiter().Emit(event.type)

            if (event.type == pygame.KEYDOWN):
                if (event.key in _events):  EventsEmmiter().Emit(event.key)

            if (event.type == pygame.KEYUP):
                if (event.key in _events):  EventsEmmiter().Emit(event.key)

    @staticmethod
    def ClearEvents() -> None:
        _evets = dict()
