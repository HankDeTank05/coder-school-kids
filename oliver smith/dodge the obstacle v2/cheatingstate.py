#library

import pygame

#project

from constants import *


class CheatingState:
    
    def __init__(self):
        pass

class NotCheatingState(CheatingState):

    def __init__(self):
        super().__init__()

    def update(self, frame_time):
        pass

    def draw(self, screen):
        pass

    def get_next_state(self, player_y: int | float) -> CheatingState:
        if player_y < 0:
            print("switching to is cheating state")
            return IsCheatingState()
        else:
            return self

class IsCheatingState(CheatingState):

    def __init__(self):
        super().__init__()
        self._cheat_time = 0
        self._text = FONT.render("YOU'RE A BAD PERSON ", True, RED)
        self._text_rect = self._text.get_rect(center=(WIDTH // 2, HEIGHT // 2))

    def update(self, frame_time):
        self._cheat_time += frame_time

    def draw(self, screen):
        screen.blit(self._text, self._text_rect)

    def get_next_state(self, player_y: int | float) -> CheatingState:
        if player_y < 0:
            if self._cheat_time >= CHEAT_TIME_PREVENTION:
                print("switching to post cheating state")
                return PostCheating()
            else:
                return self
        else:
            return NotCheatingState()

class PostCheating(CheatingState):

    def __init__(self):
        super().__init__()
        self._post_cheat_time = 0

    def update(self, frame_time):
        self._post_cheat_time += frame_time

    def draw(self, screen):
        pass

    def get_next_state(self, player_y: int | float) -> CheatingState:
        if self._post_cheat_time >= 2:
            print("switching to not cheating state")
            return NotCheatingState()
        else:
            return self
