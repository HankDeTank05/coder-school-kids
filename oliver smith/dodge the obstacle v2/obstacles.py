#language
import random
import copy
#library
import pygame
#project
from constants import *


class Obstacle:

    # constructor
    def __init__(self, rect: pygame.Rect, speed: float, dmg: float):
        self._rect: pygame.Rect = rect
        self._speed = speed
        self._dmg = dmg
        self._is_fast = random.randint(1, 100) < OBS_FAST_CHANCE
        # assert(self._rect != None) # if you got an error on this line the variable size_name doesn't have a value of "small", "normal", or "big"
        self._color = RED

    # game functions

    def update(self, frame_time):
        self._rect.move_ip(0, self._speed * frame_time)

    def draw(self, screen):
        pygame.draw.rect(screen, self._color, self._rect)

    # accessors

    def get_rect(self) -> pygame.Rect:
        return self._rect

    def get_dmg(self) -> int:
        return self._dmg

    # mutators

    def _set_start_pos(self):
        x = random.randint(0, WIDTH - self._rect.width)
        y = -self._rect.height
        self._rect.update(x, y, self._rect.width, self._rect.height)

class SmallObstacle(Obstacle):

    def __init__(self):
        temp_rect = pygame.Rect(0, 0, OBSTACLE_SMALL_WIDTH, OBSTACLE_SMALL_HEIGHT)
        super().__init__(temp_rect, OBSTACLE_SPEED_SMALL, OBSTACLE_DMG_SMALL)
        self._set_start_pos()

class NormalObstacle(Obstacle):
    
    def __init__(self):
        temp_rect = pygame.Rect(0, 0, OBSTACLE_NORMAL_WIDTH, OBSTACLE_NORMAL_HEIGHT)
        super().__init__(temp_rect, OBSTACLE_SPEED_NORMAL, OBSTACLE_DMG_NORMAL)
        self._set_start_pos()

class BigObstacle(Obstacle):
    
    def __init__(self):
        temp_rect = pygame.Rect(0, 0, OBSTACLE_BIG_WIDTH, OBSTACLE_BIG_HEIGHT)
        super().__init__(temp_rect, OBSTACLE_SPEED_BIG, OBSTACLE_DMG_BIG)
        self._set_start_pos()

class ObstacleManager:

    # constructor
    def __init__(self):
        self._obses: list[Obstacle] = []
        self._spawn_timer = 0

    # game functions

    # update all the obstacles
    def update(self, frame_time):
        self._spawn_timer += frame_time
        if self._spawn_timer >= OBSTACLE_SPAWN_DELAY:
            self._spawn_timer -= OBSTACLE_SPAWN_DELAY
            size_name = random.choice(OBSTACLE_SPAWN_CHANCE)
            if size_name == OBSTACLE_SIZE_SMALL:
                new_obs = SmallObstacle()
            elif size_name == OBSTACLE_SIZE_NORMAL:
                new_obs = NormalObstacle()
            elif size_name == OBSTACLE_SIZE_BIG:
                new_obs = BigObstacle()
            else:
                assert(False) # crashes the game if size_name doesn't have a value listed above
                # (is there a problem with OBSTACLE_SPAWN_CHANCE or the if/elif sequence above?)
            self._obses.append(new_obs)
        for obs in self._obses:
            obs.update(frame_time)

    # draw all the obstacles
    def draw(self, screen):
        for obs in self._obses:
            obs.draw(screen)

    # accessors

    def get_obses(self) -> list[Obstacle]:
        return copy.deepcopy(self._obses)
    
    # mutators

    def remove_obses(self, obses_indices: list[int]):
        obses_indices.sort(reverse=True)
        for obs_index in obses_indices:
            self._obses.pop(obs_index)
