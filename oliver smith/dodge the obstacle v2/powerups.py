import pygame
import random
from constants import *


class Powerup:

    def __init__(self, rect: pygame.Rect, color):
        self._speed = OBSTACLE_SPEED_BIG
        self._rect: pygame.Rect = rect
        self._color = color
        self._stop_range_top = 0.4
        self._stop_range_btm = 1.0
        self._stop_point = random.randint(
            self._stop_range_top * HEIGHT,
            self._stop_range_btm * HEIGHT
        )
        self._stopped_time = 25
        self._current_stop_time = 0

    # game functions

    def update(self, frame_time):
        if self._rect.y < self._stop_point: #if the powerup is above the stopping point
            self._rect.move_ip(0, self._speed * frame_time) #keeps moving down
        else:
            self._current_stop_time += frame_time

    def draw(self, screen):
        pygame.draw.rect(screen, self._color, self._rect)

    # accessors
    
    def get_current_stop_time(self)-> float:
        return self._current_stop_time
    
    def get_stop_time(self) -> float:
        return self._stopped_time


class Invincibility(Powerup):

    def __init__(self):
        temp_rect = pygame.Rect(0, 0, OBSTACLE_NORMAL_WIDTH, OBSTACLE_NORMAL_HEIGHT)
        super().__init__(temp_rect, MIDNIGHT_BLUE)

class PowerupManager:

    def __init__(self):
        self._powers: list[Powerup] = []
        self._spawn_timer = 0

    def update(self, frame_time):
        for power in self._powers:
            power.update(frame_time)


    def draw(self, screen):
        for power in self._powers:
            power.draw(screen)