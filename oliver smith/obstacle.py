# language imports (this is stuff built into python)
import random

# library imports (this is stuff that's not ours, but not built in to python)
import pygame

# project imports (this is our stuff we created)
import common as c

class Obstacle:

    # costructor
    def __init__(self, width, height, speed, explodey):
        self._rect = pygame.Rect(random.randint(0, c.WIDTH - width), -height,
                                 width, height)
        self._speed = speed
        self._explodey = explodey

    def update(self, frame_time, slow_down_timer):
        # move the obstacle
        if slow_down_timer > 0:
            self._rect.move_ip(0, self._speed * frame_time / 4)
            # TODO: set the obstacle spawn delay to 2
        else:
            self._rect.move_ip(0, self._speed * frame_time)

        if self._rect.y > c.HEIGHT:
            pass
        