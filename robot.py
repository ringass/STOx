from pygame import Surface
import math
import pygame
from vector import Vector2D
from simulator_interfaces import *
from stox_planner import is_line_intersecting_obstacle, calculate_subgoal


class Robot(Drawable, Updatable):
    def __init__(self, pos: Vector2D, radius: float = 50.0, angle: float = 0.0) -> None:
        self.__pos = pos
        self.__radius = radius
        self.__angle = angle
        self.__engines_vel = [0.0, 0.0, 0.0]
        self.__goal = None
        self.subgoal = None

        self.tolerance = 05.0

    def set_engines_vel(self, eng1: float, eng2: float, eng3: float) -> None:
        self.__engines_vel[0] = eng1
        self.__engines_vel[1] = eng2
        self.__engines_vel[2] = eng3

    def set_goal(self, goal: Vector2D) -> None:
        self.__goal = goal

    def __update_linearly(self) -> None:
        vel: Vector2D = Vector2D(0, 0)
        ang: float = self.__angle + math.pi / 6

        for eng_vel in self.__engines_vel:
            vel += Vector2D.from_polar(eng_vel, ang)
            ang += 2 * math.pi / 3

        self.__pos += vel

    def __update_angularly(self) -> None:
        ang_vel: float = sum(self.__engines_vel) / self.__radius
        self.__angle += ang_vel
        self.__angle %= 2 * math.pi

    def update(self) -> None:

        if self.__goal is None or abs(self.__pos - self.__goal) < self.tolerance:

            self.__engines_vel = [0.0, 0.0, 0.0]

        else:

            obstacle = Vector2D(500, 500)
            obstacle_radius = 50

            if self.subgoal is None and is_line_intersecting_obstacle(
                self.__pos, self.__goal, obstacle, obstacle_radius
            ):
                self.subgoal = calculate_subgoal(
                    self.__pos, self.__goal, obstacle, obstacle_radius
                )

            if self.subgoal and abs(self.__pos - self.subgoal) < self.tolerance:
                self.subgoal = None

            destination = self.subgoal if self.subgoal else self.__goal

            if destination:
                direction = destination - self.__pos
                direction = direction * (2.5 / abs(direction))
                self.__pos += direction

            # self.__update_linearly()
            # self.__update_angularly()

    def draw(self, screen: Surface) -> None:
        pygame.draw.arc(
            screen,
            (255, 255, 255),
            (
                int(self.__pos.X - self.__radius),
                int(self.__pos.Y - self.__radius),
                int(2 * self.__radius),
                int(2 * self.__radius),
            ),
            math.pi / 6 - self.__angle,
            11 * math.pi / 6 - self.__angle,
            int(self.__radius),
        )

        center: Vector2D = self.__pos
        top_front: Vector2D = center + Vector2D.from_polar(
            self.__radius, math.pi / 6 + self.__angle
        )
        bottom_front: Vector2D = center + Vector2D.from_polar(
            self.__radius, -math.pi / 6 + self.__angle
        )
        pygame.draw.polygon(
            screen,
            (255, 255, 255),
            [center.to_tuple(), top_front.to_tuple(), bottom_front.to_tuple()],
        )

        pygame.draw.circle(screen, (255, 0, 0), (500, 500), 50)

        if self.__goal:
            pygame.draw.line(
                screen,
                (128, 0, 128),
                (self.__pos.X, self.__pos.Y),
                (self.__goal.X, self.__goal.Y),
                2,
            )

        if self.subgoal:
            pygame.draw.line(
                screen,
                (0, 0, 255),
                (self.__pos.X, self.__pos.Y),
                (self.subgoal.X, self.subgoal.Y),
                2,
            )
            pygame.draw.line(
                screen,
                (0, 0, 255),
                (self.subgoal.X, self.subgoal.Y),
                (self.__goal.X, self.__goal.Y),
                2,
            )
