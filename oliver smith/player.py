# library imports (this is stuff that's not ours, but not built in to python)
import pygame

# project imports (this is our stuff we created)
import common as c


class Player:

    # constructor
    def __init__(self):
        self._size: pygame.math.Vector2 = pygame.math.Vector2(50, 50)
        self._pos: pygame.math.Vector2 = pygame.math.Vector2(c.WIDTH // 2 - self._size.x // 2,
                                       c.HEIGHT - self._size.y - 10)
        self._speed: int | float = 350
        self._rect: pygame.Rect = pygame.Rect(self._pos, self._size)

    # Game functions

    def update(self, frame_time):

        # move the player
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

        # Moving player
        #self.pos += player_move

        # move the rectangle
        self._rect.move_ip(player_move)

        # Keeps player in the screen

        # If player is partialy or totaly off screen on the left
        if self._rect.left < 0:
            self._rect.left = 0

        # If player is partialy or totaly off screen on the right
        elif self._rect.right >= c.WIDTH:
            self._rect.right = c.WIDTH - 1

        # If player is partialy or totaly off screen on the bottom
        if self._rect.bottom >= c.HEIGHT:
            self._rect.bottom = c.HEIGHT - 1

    def draw(self):
        pygame.draw.rect(c.SCREEN, c.BLUE, self._rect)

    # getters

    def get_pos(self) -> pygame.math.Vector2:
        return self._pos
    
    # setters

    def set_pos(self, new_pos: pygame.math.Vector2):
        self._pos = new_pos
        self._rect.update(self._pos, self._size)

    def set_x(self, new_x: int | float):
        self.set_pos(pygame.math.Vector2(new_x, self._pos.y))

    def set_y(self, new_y: int | float):
        self.set_pos(pygame.math.Vector2(self._pos.x, new_y))

    def set_speed(self, new_speed: int | float):
        self._speed = new_speed

    def change_speed(self, speed_change: int | float):
        self._speed += speed_change