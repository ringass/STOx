#!/usr/bin/python
import pygame
from background import Background
from pygame.locals import *
from robot import Robot
from window_events import WindowEvents
from simulation_handler import SimulationHandler
from vector import Vector2D
from robot_controller import RobotController

def build_simulation_h(simulation_h: SimulationHandler) -> None:
    robot = Robot(Vector2D(100, 100))
    robot.set_engines_vel(0, 0, 0)
    
    simulation_h.add_object(RobotController(robot))
    simulation_h.add_object(Background())
    simulation_h.add_object(robot)
    simulation_h.add_object(WindowEvents(robot))  


def main() -> None:
    
    pygame.init()
    screen:pygame.Surface = pygame.display.set_mode((1000, 1000))
    pygame.display.set_caption('Omnidirectional control simulator')
    
    simulation_h:SimulationHandler = SimulationHandler()
    build_simulation_h(simulation_h)

    clock:pygame.time.Clock = pygame.time.Clock()
    while True:
        clock.tick(30)
        
        simulation_h.event_handler()
        simulation_h.update_handler()
        simulation_h.draw_handler(screen)

if __name__ == '__main__': main()