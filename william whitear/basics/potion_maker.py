import pygame

# constant variables
SCREEN_WIDTH = 1280 
SCREEN_HEIGHT = 720
FPS = 100

# colors
BLACK = pygame.Color(0,0,0)
ELECTRIC_CYAN = pygame.Color(0,255,255)
FOREST_GREEN = pygame.Color(34,139,34)
DARK_VIOLET = pygame.Color(148,0,211)

#pygame setup
pygame.init()
screen = pygame.display.set_mode( (SCREEN_WIDTH, SCREEN_HEIGHT) )
clock = pygame.time.Clock()
running = True

# game variables
font = pygame.font.Font(size = 32)
ice_text = font.render("ice", True, ELECTRIC_CYAN)
earth_text = font.render("earth", True, FOREST_GREEN)
magic_text = font.render("magic", True, DARK_VIOLET)

while running: 
    #alloes the player to quit the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    ############################
    ### PART 1: UPDATE STUFF ###
    ############################

    text_rect = magic_text.get_rect()
    text_rect.center = pygame.math.Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    ##########################
    ### PART 2: DRAW STUFF ###
    ##########################
    screen.fill(BLACK)

    screen.blit(magic_text, text_rect)

    pygame.display.flip()

    ###################################
    ### PART 3: PREP FOR NEXT FRAME ###
    ###################################
    clock.tick(FPS)

pygame.quit()