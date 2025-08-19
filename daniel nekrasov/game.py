# language imports
import copy
import random

# library imports
import pygame

# game imports
import common as c
import better_math as bm
import player as p
import bullet as b
import enemy as e
import time_manager as tm
import circle as cir # TODO: come back and get rid of this import

clock = pygame.time.Clock()
running = True
dt = 0

time_man = tm.TimeManager()
bullet_man = b.BulletManager()
player = p.Player(color=c.GREEN, speed=500, bullet_man=bullet_man, time_man=time_man)
franks = [ e.Frank(50, pygame.math.Vector2(c.SCREEN_WIDTH, random.randrange(c.SCREEN_HEIGHT))) ] #list of franks

#main game loop
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    c.screen.fill(c.BLACK)

    # side = random.choice(["u", "d", "l", "r"])
    # if side == "u":
    #     franks.append(e.Frank(50, pygame.math.Vector2(random.randrange(c.SCREEN_WIDTH), 0)))
    # elif side == "d":
    #     franks.append(e.Frank(50, pygame.math.Vector2(random.randrange(c.SCREEN_WIDTH), c.SCREEN_HEIGHT)))
    # elif side == "l":
    #     franks.append(e.Frank(50, pygame.math.Vector2(0, random.randrange(c.SCREEN_HEIGHT))))
    # elif side == "r":
    #     franks.append(e.Frank(50, pygame.math.Vector2(c.SCREEN_WIDTH, random.randrange(c.SCREEN_HEIGHT))))

    # step 1: update stuff
    player.update(dt * time_man.get_timescale())
    bullet_man.update(dt * time_man.get_timescale())

    player_circle = cir.Circle(player.get_pos(), player.SIZE)
    for frank in franks:
        frank.update(dt * time_man.get_timescale(), player.get_pos())
        frank_circle = cir.Circle(frank.pos, frank.SIZE)
        # collision between frank and u
        if bm.circle_collide(player_circle, frank_circle ) == True:
            # kb dir is knockback dir
            kb_dir = pygame.math.Vector2(player.get_pos() - frank.pos)
            kb_dir.normalize_ip()
            kb_dir *= dt
            player.knockback(kb_dir)


    # step 2: draw stuff
    for frank in franks:
        frank.draw()
    
    player.draw()
    bullet_man.draw()
    pygame.display.flip()

    dt = clock.tick() / 1000
    #print(dt)

pygame.quit()
