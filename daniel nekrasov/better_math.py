import math
import pygame
import circle as cir

def circle_collide(circle1: cir.Circle, circle2: cir.Circle) -> bool:
    x_dist = circle1.center.x - circle2.center.x
    y_dist = circle1.center.y - circle2.center.y
    distance = math.sqrt(x_dist * x_dist + y_dist * y_dist)
    collided = distance <= circle1.radius + circle2.radius
    return collided