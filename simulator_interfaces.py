import abc
from pygame import Surface

class Drawable(metaclass=abc.ABCMeta):    
    @abc.abstractmethod
    def draw(self, screen: Surface) -> None:
        return
    
class Updatable(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def update(self) -> None:
        return
    
class EventSensitive(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def handle_event(self, event) -> None:
        return