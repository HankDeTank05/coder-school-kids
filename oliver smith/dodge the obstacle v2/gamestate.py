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
    
    def update(self, frame_time, events, keys):
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

    def update(self, frame_time, events, keys):
        self._player.update(frame_time, keys)
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
            return GameOverState(self._time, False)
        else:
            return self

class GameOverState(GameState):

    def __init__(self, time: float, holding_tab: bool ):
        self._start_over = False # when this variable is true transitions to startstate
        self._to_lboard = False # when this variable is true you transition to LeaderboardState
        self._text = FONT.render("To play again press left shift.", True, ORANGE)
        self._text_rect = self._text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        self._score = time
        self._holding_tab= holding_tab

    def update(self, frame_time, events, keys):
        if keys[pygame.K_LSHIFT]:
            self._start_over = True
        if self._holding_tab and keys[pygame.K_TAB] == False:
            self._holding_tab = False
        elif not self._holding_tab and keys[pygame.K_TAB]:
            self._to_lboard = True
       
    def draw(self, screen):
        screen.fill(BLUE)
        screen.blit(self._text, self._text_rect)

    def get_next_state(self) -> GameState:
        if self._start_over:
            return StartState()
        elif self._to_lboard:
            return LeaderboardState(self._score)
        else:
            return self

class LeaderboardState(GameState):

    def __init__(self, time):
        self._to_game_over = False #when this variable is true you transition to Game over state
        self._text_input = pygame_textinput.TextInputVisualizer(font_object=FONT)
        self._leaderboard = Leaderboard()
        self._score = time
        self._holding_tab = True

    def update(self, frame_time, events, keys):
        self._text_input.update(events)
        if keys[pygame.K_RETURN]:
            name = self._text_input.value
            self._leaderboard.submit_score(your_name=name, your_score=self._score)
        if self._holding_tab and keys[pygame.K_TAB] == False:
            self._holding_tab = False
        elif not self._holding_tab and keys[pygame.K_TAB]:
            self._to_game_over = True

    def draw(self, screen):
        screen.blit(self._text_input.surface, (0,0))
        self._leaderboard.draw(screen)

    def get_next_state(self)-> GameState:
        if self._to_game_over:
            return GameOverState(self._score, True)
        else:
            return self 