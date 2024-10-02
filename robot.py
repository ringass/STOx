import pygame
from vector import Vector2D
from simulator_interfaces import *
from stox_planner import is_line_intersecting_obstacle, calculate_subgoal

class Robot(Drawable, Updatable):
    def __init__(self, pos: Vector2D, radius: float = 50.0, angle: float = 0.0):
        self.__pos = pos
        self.__radius = radius
        self.__goal = None
        self.__engines_vel = [0.0, 0.0, 0.0]  # Inicializa as velocidades dos motores
        self.subgoal = None
        self.tolerance = 10.0  # Define uma tolerância para garantir que o subgoal seja alcançado

    # Método para definir as velocidades dos motores
    def set_engines_vel(self, eng1: float, eng2: float, eng3: float) -> None:
        self.__engines_vel[0] = eng1
        self.__engines_vel[1] = eng2
        self.__engines_vel[2] = eng3

    def set_goal(self, goal: Vector2D) -> None:
        self.__goal = goal

    def update(self) -> None:
        if self.__goal:
            
            obstacle = Vector2D(500, 500)
            obstacle_radius = 50  

            if self.subgoal is None:
                self.subgoal = calculate_subgoal(self.__pos, self.__goal, obstacle, obstacle_radius)
            
            
            if self.subgoal is not None and abs(self.__pos - self.subgoal) < self.tolerance:
                self.subgoal = None  

            
            destination = self.subgoal if self.subgoal else self.__goal

            
            direction = destination - self.__pos
            direction = direction * (1.0 / abs(direction))  
            self.__pos = self.__pos + direction

    def draw(self, screen: pygame.Surface) -> None:
        
        pygame.draw.circle(screen, (255, 255, 255), (int(self.__pos.X), int(self.__pos.Y)), int(self.__radius))

        
        pygame.draw.circle(screen, (255, 0, 0), (500, 500), 50)  

        
        if self.__goal:
            pygame.draw.line(screen, (128, 0, 128), (self.__pos.X, self.__pos.Y), (self.__goal.X, self.__goal.Y), 2)

        
        if self.subgoal:
            
            pygame.draw.line(screen, (0, 0, 255), (self.__pos.X, self.__pos.Y), (self.subgoal.X, self.subgoal.Y), 2)

            
            pygame.draw.line(screen, (0, 0, 255), (self.subgoal.X, self.subgoal.Y), (self.__goal.X, self.__goal.Y), 2)

