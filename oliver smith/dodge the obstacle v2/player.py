# library 
import pygame

#project imports
from constants import *
from cheatingstate import NotCheatingState

class Player:

    # constructor
    def __init__(self):
        size = pygame.math.Vector2(50, 50)
        pos = pygame.math.Vector2(WIDTH // 2 - size.x // 2,
                                       HEIGHT - size.y - 10)
        self._speed: int | float = 350
        self._rect: pygame.Rect = pygame.Rect(pos, size)
        self._max_hp = PLAYER_MAX_HEALTH
        self._hp = self._max_hp

        self._cheating_state = NotCheatingState()

    # Game functions

    def update(self, frame_time):

        ###################
        # move the player #
        ###################

        keys = pygame.key.get_pressed()
        move_x = 0
        move_y = 0
        if keys[pygame.K_UP]:
            move_y -= 1
        if keys[pygame.K_DOWN]:
            move_y += 1
        if keys[pygame.K_LEFT]:
            move_x -= 1
        if keys[pygame.K_RIGHT]:
            move_x += 1
        player_move = pygame.math.Vector2(move_x, move_y)
        # correct diagonal movement
        if player_move.length() > 0:
            player_move = player_move.normalize() * self._speed * frame_time

        # move the rectangle
        self._rect.move_ip(player_move)

        ##############################
        # Keeps player in the screen #
        ##############################
        right_bound = WIDTH - 1
        bottom_bound = HEIGHT - HEALTH_BAR_HEIGHT

        # If player is partialy or totaly off screen on the left
        if self._rect.left < 0:
            self._rect.left = 0

        # If player is partialy or totaly off screen on the right
        elif self._rect.right > right_bound:
            self._rect.right = right_bound

        # If player is partialy or totaly off screen on the bottom
        if self._rect.bottom > bottom_bound:
            self._rect.bottom = bottom_bound
        
        self._cheating_state = self._cheating_state.get_next_state(player_y=self._rect.bottom)
        self._cheating_state.update(frame_time)


    def draw(self, screen):
        self._cheating_state.draw(screen)
        pygame.draw.rect(screen, BLUE, self._rect)

    # accessors

    def get_pos(self) -> pygame.math.Vector2:
        return pygame.math.Vector2(self._rect.topleft)
    
    def get_hp(self) -> int:
        return self._hp

    def get_rect(self) -> pygame.Rect:
        return self._rect

    # mutators

    def set_pos(self, new_pos: pygame.math.Vector2):
        self._rect.update(new_pos, self._rect.size)

    def set_x(self, new_x: int | float):
        self.set_pos(pygame.math.Vector2(new_x, self._rect.y))

    def set_y(self, new_y: int | float):
        self.set_pos(pygame.math.Vector2(self._rect.x, new_y))

    def set_speed(self, new_speed: int | float):
        self._speed = new_speed

    def change_speed(self, speed_change: int | float):
        self._speed += speed_change

    def take_damage(self, damage: int):
        self._hp -= damage
