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
        self._scores: dict[str, float] = {}
        self._read_data()

    def submit_score(self, your_name: str, your_score: float) -> bool:
        # case 1 is your name is already in the keys and you have a new high score
        # case 2 is your name is not in the keys
        # case 3 is your name is already in the keys but you dont have a new high score
        #                          case 1                                                       case 2
        #  vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv    vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
        if (your_name in self._scores.keys() and your_score > self._scores[your_name]) or your_name not in self._scores.keys():
                self._scores[your_name] = your_score
                self._write_data()
                return True
        else: # case 3
            return False

    def _read_data(self):
        with open(FILE_NAME, "r") as lb_file:
            while True:
                line=lb_file.readline()
                if len(line) == 0:
                    break
                else:
                    items = line.split(',')
                    name = items[0]
                    score = float(items[1])
                    self._scores[name] = score
                    continue

    def _write_data(self):
        with open(FILE_NAME, "w") as lb_file:
            for (name, score) in zip(self._scores.keys(), self._scores.values()):
                lb_file.write(f"{name},{score}\n")

    def update(self, frame_time):
        pass

    def draw(self, screen):
        sorted_scores = dict(
            sorted(self._scores.items(), key=lambda item: item[1], reverse=True)
        )
        place = 1
        for pair in zip(self._scores.keys(), self._scores.values()):
            #print(pair)
            name = pair[0]
            score = pair[1]
            entry_text = FONT.render(f"{place}. {name} : {score}", True, TEAL)
            entry_text_rect = entry_text.get_rect(
                midtop = (WIDTH // 2, place * FONT_SIZE)
            )
            screen.blit(entry_text, entry_text_rect)
            place += 1

