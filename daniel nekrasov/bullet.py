import copy

import pygame

import common as c

"""bullet functions"""

bullet_speed = 700
bullet_radius = 20
# these are parallel 
#data at the same index in dffernt lists belongs to the same object
bullet_pos = []
bullet_dir = []

def bullet_create(_pos, _dir):
  global bullet_pos, bullet_dir
  bullet_pos.append(copy.deepcopy(_pos))
  bullet_dir.append(copy.deepcopy(_dir) * bullet_speed)


def bullet_update(_dt):
    for index in range(len(bullet_pos)):
        bullet_pos[index] += bullet_dir[index] * _dt
    
    index = 0
    while index < len(bullet_pos):
        current_pos = bullet_pos[index]
        if current_pos.x < 0 or current_pos.x > c.SCREEN_WIDTH or current_pos.y < 0 or current_pos.y > c.SCREEN_HEIGHT :
            bullet_pos.pop(index)
            bullet_dir.pop(index)
        else:
            index += 1
    


def bullet_draw():
    for pos in bullet_pos:
        pygame.draw.circle(c.screen, c.BLUE, pos, bullet_radius)