# library imports 
import pygame

# game imports
from common import *
import player
import map

# pygame setup
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True
frame_time = 0


# game variables
p1 = player.Player()
# map_screen = map.MapScreen(
#     spawn_tile_pos=pygame.math.Vector2(2,2)
# )
world_map = map.Map(1, 2, 0, 0)
for i in range(2, 14):
    world_map.get_map_screen(0,0).set_tile_grass_floor(i, SCREEN_TILE_HEIGHT - 1)
    world_map.get_map_screen(0,1).set_tile_grass_floor(i, 0)
p1.spawn_at_tile(tile_pos=world_map.get_start_screen().get_spawn_tile_pos())

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    # screen.fill("purple")

    ##################
    # part 1: update #
    ##################
    keys = pygame.key.get_pressed()
    p1.update(frame_time, keys, current_map_screen=world_map.get_current_screen())
    world_map.get_current_screen().update(frame_time)

    # TODO: check for collision w/ map screen
    p1.rect
    for y in range(SCREEN_TILE_HEIGHT):
        for x in range(SCREEN_TILE_WIDTH):
            tile = world_map.get_current_screen().get_tile_at(x, y)
            tile_rect = tile.rect
            if tile.is_solid and p1.rect.colliderect(tile_rect):
                x_dif = abs(tile_rect.centerx - p1.rect.centerx)
                y_dif = abs(tile_rect.centery - p1.rect.centery)
                if x_dif > y_dif:
                    if tile_rect.centerx < p1.rect.centerx:
                        p1.rect.left = tile_rect.right
                    elif p1.rect.centerx < tile_rect.centerx:
                        p1.rect.right = tile_rect.left

                elif y_dif > x_dif:
                    if tile_rect.centery < p1.rect.centery:
                        p1.rect.top = tile_rect.bottom
                    elif p1.rect.centery < tile_rect.centery:
                        p1.rect.bottom = tile_rect.top


    ################
    # part 2: draw #
    ################
    #map_screen.draw(screen)
    world_map.get_current_screen().draw(screen)
    world_map.draw(screen)
    p1.draw(screen)

    # flip() the display to put your work on screen
    pygame.display.flip()

    frame_time = clock.tick(60)/1000  # limits FPS to 60

pygame.quit()