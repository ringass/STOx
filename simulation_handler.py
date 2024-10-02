from simulator_interfaces import *
import pygame
from pygame.locals import *

class SimulationHandler:
    def __init__(self):
        self.__drawables:list[Drawable] = []
        self.__updatables:list[Updatable] = []
        self.__event_sensitive_objs:list[EventSensitive] = []
        
    def add_object(self, obj) -> None:
        if(isinstance(obj, Drawable)): self.__drawables.append(obj)
        if(isinstance(obj, Updatable)): self.__updatables.append(obj)
        if(isinstance(obj, EventSensitive)): self.__event_sensitive_objs.append(obj)
        
    def event_handler(self) -> None:
        for event in pygame.event.get():
            for e in self.__event_sensitive_objs: e.handle_event(event)
            
    def update_handler(self) -> None:
        for u in self.__updatables: u.update()

    def draw_handler(self, screen: pygame.Surface) -> None:
        for d in self.__drawables: d.draw(screen)
        pygame.display.flip()