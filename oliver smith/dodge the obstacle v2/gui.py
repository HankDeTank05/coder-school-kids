#library
import pygame

#project

from constants import *
from player import Player

class Hud:

    # constructor
    def __init__(self):
        # health bar
        self._max_health_bar_width = HEALTH_BAR_WIDTH
        self._health_pcent = 1

    # game functions

    def update(self, frame_time, player_hp: int):
        self._health_pcent = player_hp / PLAYER_MAX_HEALTH


    def draw(self, screen):
        # draw the background rectangle
        bg_rect = pygame.Rect((0, 0), (HEALTH_BAR_WIDTH, HEALTH_BAR_HEIGHT))
        bg_rect.midbottom = pygame.math.Vector2(WIDTH/2, HEIGHT-1)
        pygame.draw.rect(screen, BLACK, bg_rect)
        # draw the current health rectangle
        hp_rect = pygame.Rect(bg_rect.topleft, (self._health_pcent * HEALTH_BAR_WIDTH, HEALTH_BAR_HEIGHT))
        pygame.draw.rect(screen, RED, hp_rect)

class Leaderboard:

    def __init__(self):
        self._scores: list[float] = []

    def submit_score(self, your_score):
        #case 1: empty leaderboard
        #case 2: insert at end (new score is lowest)
        #        case 1                             case 2
        #  vvvvvvvvvvvvvvvvvvvvvv    vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
        if len(self._scores) == 0 or your_score < self._scores[len(self._scores) - 1]:
            self._scores.append(your_score)
        # TODO: case 3: insert in the middle of the list (your score is not highest or lowest)
        # TODO: case 4: insert at beginning of list (your score is the highest)


    def update(self, frame_time):
        pass

    def draw(self, screen):
        pass
