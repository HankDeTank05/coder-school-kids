import copy

import pygame

import common as c

SPEED = 700
RADIUS = 20

class Bullet:

    #constructer
    def __init__(self, pos, dir):
        self.pos = pos
        self.dir = dir
        self.speed = SPEED
        self.size = RADIUS

    def update(self, dt):
        # move
        self.pos += self.dir * dt

    def draw(self):
        pygame.draw.circle(c.screen, c.BLUE, self.pos, self.size)

class BulletManager:

    #constructor
    def __init__(self):
        self.bullets = []

    # create a bullet and add it to the manager
    def add_bullet(self, pos, dir):
        bullet = Bullet(copy.deepcopy(pos), copy.deepcopy(dir))
        self.bullets.append(bullet)

    def update(self, dt):
        for bullet in self.bullets:
            bullet.update(dt)

    def draw(self):
        for bullet in self.bullets:
            bullet.draw()

'''
bullet_speed = 700
bullet_radius = 20
# these are parallel 
#data at the same index in dffernt lists belongs to the same object
# bullet_pos = []
# bullet_dir = []

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
        #if bullet off screen...
        if current_pos.x < 0 or current_pos.x > c.SCREEN_WIDTH or current_pos.y < 0 or current_pos.y > c.SCREEN_HEIGHT :
            #...remove bullet from bullet list
            bullet_pos.pop(index)
            bullet_dir.pop(index)
        else:
            index += 1
    


def bullet_draw():
    for pos in bullet_pos:
        pygame.draw.circle(c.screen, c.BLUE, pos, bullet_radius)
'''