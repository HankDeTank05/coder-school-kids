import os
import pygame
from common import *
from gamemath import tiles_to_pixels
from convenience import load_sprite

class Player(pygame.sprite.Sprite):

    def __init__(self):
        self.rect = pygame.Rect(
            pygame.math.Vector2(0,0), # this is in px, not tiles
            pygame.math.Vector2(TILE_WIDTH_PX, TILE_HEIGHT_PX)
        )
        # 72.png, 74.png, 76.png
        self._sprites = {
            'walk down': [
                load_sprite(os.path.join('elodie fredman', 'zeldalike', 'assets', 'sprites', 'link', 'walk_down_0.png')),
                load_sprite(os.path.join('elodie fredman', 'zeldalike', 'assets', 'sprites', 'link', 'walk_down_1.png'))

            ],
            'walk up': [
                load_sprite(os.path.join('elodie fredman', 'zeldalike', 'assets', 'sprites', 'link', 'walk_up_0.png')),
                load_sprite(os.path.join('elodie fredman', 'zeldalike', 'assets', 'sprites', 'link', 'walk_up_1.png'))

            ],
            'walk right': [
                load_sprite(os.path.join('elodie fredman', 'zeldalike', 'assets', 'sprites', 'link', 'walk_right_0.png')),
                load_sprite(os.path.join('elodie fredman', 'zeldalike', 'assets', 'sprites', 'link', 'walk_right_1.png')) 

            ],
            'walk left': [
                pygame.transform.flip(load_sprite(os.path.join('elodie fredman', 'zeldalike', 'assets', 'sprites', 'link', 'walk_right_0.png')), True, False),
                pygame.transform.flip(load_sprite(os.path.join('elodie fredman', 'zeldalike', 'assets', 'sprites', 'link', 'walk_right_1.png')), True, False)

            ]
        }
        self._anim_frame = 0
        self._anim_frame_time = 0
        self.image = self._sprites['walk down'][self._anim_frame]
        self._speed = PLAYER_SPEED 

    # game functions

    def update(self, frame_time, keys, current_map_screen):
        # note: delta means change
        pos_delta = pygame.math.Vector2(0,0)

        #calculate movement
        if keys[pygame.K_UP]:
            pos_delta.y -= 1
            self._anim_frame = 0
            self._anim_frame_time = 0
            self.image = self._sprites['walk up'][self._anim_frame]
        if keys[pygame.K_DOWN]:
            pos_delta.y += 1
            self._anim_frame = 0
            self._anim_frame_time = 0        
            self.image = self._sprites['walk down'][self._anim_frame]
        if keys[pygame.K_RIGHT]:
            pos_delta.x += 1
            self._anim_frame = 0
            self._anim_frame_time = 0
            self.image = self._sprites['walk right'][self._anim_frame]
        if keys[pygame.K_LEFT]:
            pos_delta.x -= 1
            self._anim_frame = 0
            self._anim_frame_time = 0
            self.image = self._sprites['walk left'][self._anim_frame]

        self._anim_frame_time += frame_time
        if self._anim_frame_time > PLAYER_ANIM_SPF:
            self._anim_frame += 1
            if self._anim_frame >= 

        # fix diagonal movement
        if pos_delta.x != 0 and pos_delta.y != 0:
            pos_delta = pos_delta.normalize()
        
        #move player 
        # self._pos += pos_delta * self._speed * frame_time
        self.rect.move_ip(pos_delta * self._speed * frame_time)

        # stay on screen
        # if self._pos.x < 0:
        #     self._pos.x = 0
        # elif self._pos.x > WIDTH - 1 - self._size.x:
        #     self._pos.x = WIDTH - 1 - self._size.x
        if self.rect.left < SCREEN_RECT.left:
            self.rect.left = SCREEN_RECT.left
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right
        
        # if self._pos.y < 0:
        #     self._pos.y = 0
        # elif self._pos.y > SCREEN_HEIGHT - 1 - self._size.y:
        #     self._pos.y = SCREEN_HEIGHT - 1 - self._size.y 
        if self.rect.top < SCREEN_RECT.top:
            self.rect.top = SCREEN_RECT.top
        elif self.rect.bottom > SCREEN_RECT.bottom:
            self.rect.bottom = SCREEN_RECT.bottom
                    
    def draw(self, screen):
        pygame.draw.rect(screen, (0,255,0), self.rect, width=1)
        screen.blit(self.image, self.rect)

    # accessors

    # mutators

    def spawn_at_tile(self, tile_pos: pygame.math.Vector2):
        self.rect.topleft = tiles_to_pixels(tile_pos)
    