# Example file showing a basic pygame "game loop"
import pygame
import common as c 
import snake 
import random
import foodstuff
import trap as t
  
def draw_gridlines(screen):
    
    for pixel_x in range(0, c.SCREEN_WIDTH, c.TILE_SIZE):
        pygame.draw.line(surface = screen,color = c.COLOR_GRID,start_pos=(pixel_x,0),end_pos=(pixel_x, c.SCREEN_HEIGHT))
        
    for pixel_y in range(0, c.SCREEN_HEIGHT, c.TILE_SIZE):
        pygame.draw.line(surface = screen, color = c.COLOR_GRID, start_pos = (0, pixel_y), end_pos=(c.SCREEN_WIDTH, pixel_y))

def create_snake():
    # randomize start position
    start_x = random.randrange(c.GRID_WIDTH)
    start_y = random.randrange(c.GRID_HEIGHT)

    # randomize start direction
    left_max = c.EDGE_ZONE
    right_min = c.GRID_WIDTH - c.EDGE_ZONE
    top_max = c.EDGE_ZONE
    bottom_min = c.GRID_HEIGHT - c.EDGE_ZONE
    dir_all =[c.DIR_DOWN, c.DIR_LEFT, c.DIR_RIGHT, c.DIR_UP]

    while True:
        start_dir = dir_all[random.randrange(len(dir_all))] 

        # if we start in the left edge zone and we start facing left...
        if start_x <= left_max and start_dir == c.DIR_LEFT:
            continue # ...Repick starting dir
        # otherwise, if we start in the right edge zone and we start facing right...
        elif start_x >= right_min and start_dir == c.DIR_RIGHT:
            continue 
        # if we start in the top edge zone and we start facing up...
        if start_y <= top_max and start_dir == c.DIR_UP:
            continue
        #otherwise, if we start in the bottom edge zone and we start facing down...
        elif start_y >= bottom_min and start_dir == c.DIR_DOWN:
            continue 

        break

    # create snake
    global player_snake
    player_snake = snake.Snake(start_x, start_y, start_dir)

def create_food_manager():
    global foodmanager
    foodmanager = foodstuff.FoodManager(sp_max_food=30)

def create_trap_manager():
    global trapmanager 
    trapmanager = t.TrapManager(sp_max_traps=5)

def run():
    ################
    # PYGAME SETUP #
    ################

    pygame.init()
    screen = pygame.display.set_mode((c.SCREEN_WIDTH,c.SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True
    frame_time = 0

    ##############
    # GAME SETUP #
    ##############

    create_snake()
    create_food_manager()
    create_trap_manager()

    # trap =t.Trap(10,10)


    ##################
    # Main game loop #
    ##################

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the screen with a color to wipe away anything from last frame
        screen.fill(c.COLOR_BG)

        #part 1: update
        player_snake.update(frame_time)
        foodmanager.update(player_snake)
        trap.update(player_snake)
        if player_snake.check_collision() == True or trap.check_trap_act() == True:
            # reset the game 
            create_snake()
            create_food_manager()
            continue
        
        #part 2: draw
        draw_gridlines(screen)
        player_snake.draw(screen)
        foodmanager.draw(screen)
        trap.draw(screen)

        # flip() the display to put your work on screen
        pygame.display.flip()

        frame_time = clock.tick()/1000  # limits FPS to 60

    pygame.quit()

run()