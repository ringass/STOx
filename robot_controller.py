from simulator_interfaces import Updatable, EventSensitive
from robot import Robot
from vector import Vector2D

class Objective():
    def __init__(self, vector: Vector2D, angle:float) -> None:
        self.vector = vector
        self.angle = angle

class RobotController(Updatable, EventSensitive):
    def __init__(self, robot: Robot) -> None:
        self.__robot:Robot = robot
        self.__objective:Objective= None
    
    def update(self) -> None:
        pass
    
    def handle_event(self, event) -> None:
        pass
    