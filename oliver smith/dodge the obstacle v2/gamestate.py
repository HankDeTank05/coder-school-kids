#library
import pygame
import pygame_textinput
#project
from constants import *
from gui import Hud, Leaderboard
from player import Player
from obstacles import ObstacleManager


class GameState:

    def __init__(self):
        self._start_state = StartState()
        self._playing_state = PlayingState()

    def get_next_state(self) -> 'GameState':
        print("you should never see this")
        assert(False)

class StartState(GameState):

    def __init__(self):
        self._begin_game = False
        self._text = FONT.render("To play press right shift.", True, BLACK)
        self._text_rect = self._text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    
    def update(self, frame_time):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RSHIFT]:
            self._begin_game = True

    def draw(self, screen):
        screen.fill(GREEN)
        screen.blit(self._text, self._text_rect)

    def get_next_state(self) -> GameState:
        if self._begin_game:
            return PlayingState()
        else:
            return self

class PlayingState(GameState):
    
    def __init__(self):
        self._player = Player()
        self._obs_man = ObstacleManager()
        self._hud = Hud()
        self._time = 0

    def update(self, frame_time):
        self._player.update(frame_time)
        self._obs_man.update(frame_time)
        self._hud.update(frame_time, self._player.get_hp())
        self._time += frame_time

        # do collision
        collided_indices = []
        obses_list = self._obs_man.get_obses()
        for obs_index in range(len(obses_list)):
            obstacle = obses_list[obs_index]
            player_rect = self._player.get_rect()
            obs_rect = obstacle.get_rect()
            if player_rect.colliderect(obs_rect):
                self._player.take_damage(obstacle.get_dmg())
                collided_indices.append(obs_index)
        self._obs_man.remove_obses(collided_indices)

    def draw(self, screen):
        self._player.draw(screen)
        self._obs_man.draw(screen)
        self._hud.draw(screen)

    def get_next_state(self) -> GameState:
        if self._player.get_hp() <= 0:
            return GameOverState(self._time)
        else:
            return self

class GameOverState(GameState):

    def __init__(self, time):
        self._text_input = pygame_textinput.TextInputVisualizer(font_object=FONT)
        self._start_over = False
        self._text = FONT.render("To play again press left shift.", True, ORANGE)
        self._text_rect = self._text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        self._leaderboard = Leaderboard()
        self._score = time

    def update(self, frame_time):
        self._text_input.update(pygame.event.get())
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LSHIFT]:
            self._start_over = True
            name = self._text_input.value
            self._leaderboard.submit_score(your_name=name, your_score=self._score)

    def draw(self, screen):
        screen.fill(YELLOW)
        screen.blit(self._text, self._text_rect)
        screen.blit(self._text_input.surface, (0,0))

    def get_next_state(self) -> GameState:
        if self._start_over:
            return StartState()
        else:
            return self
