from simulator_interfaces import EventSensitive
from pygame.locals import *
import pygame
from vector import Vector2D


class WindowEvents(EventSensitive):
    def __init__(self, robot):
        self.robot = robot
        self.goal = None

    def handle_event(self, event) -> None:
        if event.type == QUIT:
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            self.goal = pygame.mouse.get_pos()
            self.robot.set_goal(Vector2D(self.goal[0], self.goal[1]))
