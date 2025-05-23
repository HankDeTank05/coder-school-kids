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

clock = pygame.time.Clock()
running = True
dt = 0

player = p.Player(c.GREEN, 500)
franks = [ e.Frank(50, pygame.math.Vector2(c.SCREEN_WIDTH, random.randrange(c.SCREEN_HEIGHT))) ] #list of franks
bullets = [] # list of bullets

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
    player.update(dt)
    for bullet in bullets:
        bullet.update(dt)
    for frank in franks:
        frank.update(dt, player.pos)
        # collision between frank and u
        if bm.circle_collide(player.pos, player.SIZE, frank.pos, frank.SIZE) == True:
            pass


    # step 2: draw stuff
    for frank in franks:
        frank.draw()
    for bullet in bullets:
        bullet.draw()
    player.draw()

    pygame.display.flip()

    dt = clock.tick()/1000
    print(dt)

pygame.quit()
