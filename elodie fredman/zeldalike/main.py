# library imports 
import pygame

# game imports
from common import *
import player
import map
import tile

# pygame setup
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True
frame_time = 0

# game variables
# map_screen = map.MapScreen(
#     spawn_tile_pos=pygame.math.Vector2(2,2)
# )
world_map = map.Map(3, 3, 1, 1)

# the code modifies the existing (default) map to make openings at the top and bottom to allow for transitions
world_map.create_opening(0,0, map.Edge.Bottom)
world_map.create_opening(0,1, map.Edge.Bottom)
world_map.create_opening(1,0, map.Edge.Bottom)
world_map.create_opening(1,1, map.Edge.Bottom)
world_map.create_opening(2,0, map.Edge.Bottom)
world_map.create_opening(2,1, map.Edge.Bottom)

# the code modifies the existing (default) map to make openings at the left and right to allow for transitions
world_map.create_opening(0,0, map.Edge.Right)
world_map.create_opening(0,1, map.Edge.Right)
world_map.create_opening(1,1, map.Edge.Right)
world_map.create_opening(0,2, map.Edge.Right)
world_map.create_opening(1,2, map.Edge.Right)
world_map.create_opening(2,0, map.Edge.Left)


# DUNGEON
dungeon_map = map.Map(2, 1, 0, 0)
dungeon_map.create_opening(0,0, map.Edge.Right)

# world map doors
world_map.get_map_screen_xy(1,1).set_tile_door(12,4, dungeon_map, pygame.math.Vector2(10,5))
dungeon_map.get_map_screen_xy(1,0).set_tile_door(12,4, world_map, pygame.math.Vector2(10,7))

# current map 
current_map = world_map
'''
if player in world map
collide with dungeon entrance / exit
    current map = dungeon_map

if player in dungeon_map
collide with entrance / exit
    current_map = world map
'''

# player
p1 = player.Player()
p1.spawn_at_tile(tile_pos=world_map.get_start_screen().get_spawn_tile_pos())
p1.set_current_screen(current_map.get_start_screen_coords())


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
    p1.update(frame_time, keys)
    world_map.get_map_screen_v2(map_screen_coords=p1.get_current_screen()).update(frame_time)

    # checks for collision between player and map tiles 
    for y in range(SCREEN_TILE_HEIGHT):
        for x in range(SCREEN_TILE_WIDTH):
            current_tile = current_map.get_map_screen_v2(p1.get_current_screen()).get_tile_at(x, y)
            tile_rect = current_tile.rect
            # if the player collides with the current tile...
            if p1.rect.colliderect(tile_rect):
                # ... and that tile is solid...
                if current_tile.is_solid:
                    # ... adjust player pos so they don't overlap with the solid tile.
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
                #... and the tile is a door...
                elif type(current_tile) is tile.TileDoor:
                    #... then switch the player map to the dungeon.
                    current_map = current_tile.transition_to_map
                    p1.set_current_screen(current_screen=current_map.get_start_screen_coords())
                    print(current_tile.transition_to_tile)
                    p1.spawn_at_tile(current_tile.transition_to_tile)
                    

    # check for collision w/ map screen edge to tranistion screens
    if p1.rect.colliderect(current_map.get_trans_box(edge=map.Edge.Left)):
        p1.screen_trans_left()
    if p1.rect.colliderect(current_map.get_trans_box(edge=map.Edge.Right)):
        p1.screen_trans_right()
    if p1.rect.colliderect(current_map.get_trans_box(edge=map.Edge.Top)):
        p1.screen_trans_up()
    elif p1.rect.colliderect(current_map.get_trans_box(edge=map.Edge.Bottom)):
        p1.screen_trans_down()


    ################
    # part 2: draw #
    ################
    #map_screen.draw(screen)
    current_map.get_map_screen_v2(p1.get_current_screen()).draw(screen)
    current_map.draw(screen)
    p1.draw(screen)

    # flip() the display to put your work on screen
    pygame.display.flip()

    frame_time = clock.tick(60)/1000  # limits FPS to 60

pygame.quit()