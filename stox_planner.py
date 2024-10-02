import math
from vector import Vector2D


def is_line_intersecting_obstacle(
    start: Vector2D, goal: Vector2D, obstacle: Vector2D, obstacle_radius: float
) -> bool:

    line_goal = goal - start
    norm_line_goal = line_goal * (1 / abs(line_goal))

    line_obstacle = obstacle - start

    proj_len = line_obstacle.X * norm_line_goal.X + line_obstacle.Y * norm_line_goal.Y

    intersection_point = start + norm_line_goal * proj_len

    ds_obstacle = abs(intersection_point - obstacle)

    return ds_obstacle <= obstacle_radius


def calculate_subgoal(
    start: Vector2D,
    goal: Vector2D,
    obstacle: Vector2D,
    obstacle_radius: float,
    margin: float = 60.0,
) -> Vector2D:
    line_goal = goal - start
    norm_line_goal = line_goal * (1 / abs(line_goal))

    line_obstacle = obstacle - start

    proj_len = line_obstacle.X * norm_line_goal.X + line_obstacle.Y * norm_line_goal.Y

    intersection_point = start + norm_line_goal * proj_len

    ds_obstacle = abs(intersection_point - obstacle)
    if ds_obstacle > obstacle_radius:
        return None

    angle_to_goal = math.atan2(line_goal.Y, line_goal.X)
    angle_90_degrees = angle_to_goal + math.pi / 2

    safe_distance = 2 * obstacle_radius + margin

    subgoal = Vector2D(
        intersection_point.X + math.cos(angle_90_degrees) * safe_distance,
        intersection_point.Y + math.sin(angle_90_degrees) * safe_distance,
    )

    return subgoal
