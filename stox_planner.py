import math
from vector import Vector2D

def is_line_intersecting_obstacle(start: Vector2D, end: Vector2D, obstacle: Vector2D, radius: float) -> bool:

    line_vec = end - start
    to_obstacle_vec = obstacle - start
    projection = ((to_obstacle_vec.X * line_vec.X) + (to_obstacle_vec.Y * line_vec.Y)) / abs(line_vec)
    closest_point = start + line_vec * (projection / abs(line_vec))
    distance_to_obstacle = abs(closest_point - obstacle)
    return distance_to_obstacle < radius

import math
from vector import Vector2D

def calculate_subgoal(start: Vector2D, goal: Vector2D, obstacle: Vector2D, obstacle_radius: float, margin: float = 70.0) -> Vector2D:
    """
    Calcula o subgoal a partir do ponto onde a linha entre o robô e o goal intersecta o obstáculo.
    O subgoal será a 90 graus do ponto de interseção, na linha entre o robô e o goal.
    """
    
    line_vec = goal - start
    line_vec_norm = line_vec * (1 / abs(line_vec))  

    to_obstacle_vec = obstacle - start

    projection_length = (to_obstacle_vec.X * line_vec_norm.X + to_obstacle_vec.Y * line_vec_norm.Y)

   
    intersection_point = start + line_vec_norm * projection_length

    
    distance_to_obstacle = abs(intersection_point - obstacle)
    if distance_to_obstacle > obstacle_radius:
        return None  

    
    angle_to_goal = math.atan2(line_vec.Y, line_vec.X)
    angle_90_degrees = angle_to_goal + math.pi/2 

    
    safe_distance = obstacle_radius + margin

    subgoal = Vector2D(
        intersection_point.X + math.cos(angle_90_degrees) * safe_distance,
        intersection_point.Y + math.sin(angle_90_degrees) * safe_distance
    )

    return subgoal

