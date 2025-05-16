import math
import pygame

#                   center of circle 1             radius of circle 1
#                   should be a vector2           should be a number     (same type as center1)      (same type as radius1)   this function returns boolean data (true or false)
#                  ||||||||||||||||||||||||||||  ||||||||||||||||||||  ||||||||||||||||||||||||||||  ||||||||||||||||||||     ||||
#                  vvvvvvvvvvvvvvvvvvvvvvvvvvvv  vvvvvvvvvvvvvvvvvvvv  vvvvvvvvvvvvvvvvvvvvvvvvvvvv  vvvvvvvvvvvvvvvvvvvv     vvvv
def circle_collide(center1: pygame.math.Vector2, radius1: int | float, center2: pygame.math.Vector2, radius2: int | float) -> bool:
    x_dist = center1.x - center2.x
    y_dist = center1.y - center2.y
    distance = math.sqrt(x_dist * x_dist + y_dist * y_dist)
    collided = distance <= radius1 + radius2
    return collided