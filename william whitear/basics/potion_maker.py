import pygame

# constant variables
SCREEN_WIDTH = 1280 
SCREEN_HEIGHT = 720
FPS = 100

# colors
BLACK = pygame.Color(0,0,0)
WHITE = pygame.Color(255, 255, 255)
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

elements_text = [
    "ice",
    "earth",
    "magic"
]
current_element_index = 0

# key states 
up_arow_prev_state = False
up_arow_curr_state = False
dn_arow_prev_state = False
dn_arow_curr_state = False 

while running: 
    #alloes the player to quit the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    ############################
    ### PART 1: UPDATE STUFF ###
    ############################

    # read for up and down arrow key presses here
    keys = pygame.key.get_pressed()
    up_arow_curr_state = keys[pygame.K_UP]
    if up_arow_curr_state == True and up_arow_prev_state == False: # it cheaks if you are pressing the up arrow #
        current_element_index += 1 # it adds one to the variable
        if current_element_index == 3: # if the index variable is too big, then....
            current_element_index -= 3 # decrease the index variable back to zero
    dn_arow_curr_state =  keys[pygame.K_DOWN]
    if dn_arow_curr_state == True and dn_arow_prev_state == False:
        current_element_index -= 1
        if current_element_index == -1:  
            current_element_index += 3

    # TODO: eventually, comment out the following line of code
    print(elements_text[current_element_index])

    element_text = font.render(elements_text[current_element_index], True, WHITE) 
    text_rect = element_text.get_rect()
    text_rect.center = pygame.math.Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    ##########################
    ### PART 2: DRAW STUFF ###
    ##########################
    screen.fill(BLACK)

    # this code is rendering the element text on screen
    screen.blit(element_text, text_rect)

    pygame.display.flip()

    ###################################
    ### PART 3: PREP FOR NEXT FRAME ###
    ###################################

    up_arow_prev_state = up_arow_curr_state
    dn_arow_prev_state = dn_arow_curr_state

    clock.tick(FPS)

pygame.quit()