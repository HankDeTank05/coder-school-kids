# language imports
import copy

# library imports
import pygame

# game imports
import common as c
import character as char
import bullet

clock = pygame.time.Clock()
running = True
dt=0

player = char.Player(c.GREEN, 500)

#main game loop
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    c.screen.fill(c.BLACK)

    # step 1: update stuff
    #character.player_update(dt)
    player.update(dt)
    bullet.bullet_update(dt)

    # step 2: draw stuff
    #character.player_draw()
    player.draw()
    bullet.bullet_draw()
    pygame.display.flip()

    dt=clock.tick(60)/1000

pygame.quit()
