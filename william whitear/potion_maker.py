import pygame

# rendering variables
SCREEN_WIDTH = 1280 
SCREEN_HEIGHT = 720
FPS = 100

# game constants
MIN_ACID = 1 
MAX_ACID = 5
ITEMS_ON_SCREEN = 2
ITEM_X = []
for item_index in range(ITEMS_ON_SCREEN):
    x = (SCREEN_WIDTH / (ITEMS_ON_SCREEN + 1)) * (item_index + 1)
    ITEM_X.append(x)

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
item_categories = ["element", "acid"]
category_index = 0
elements_text = [
    "ice",
    "earth",
    "magic"
]
current_element_index = 0
current_acid = MIN_ACID


# key states 
up_arow_prev_state = False
up_arow_curr_state = False
dn_arow_prev_state = False
dn_arow_curr_state = False 
lt_arow_curr_state = False
lt_arow_prev_state = False
rt_arow_prev_state = False
rt_arow_curr_state = False

while running: 
    #allows the player to quit the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    ############################
    ### PART 1: UPDATE STUFF ###
    ############################

    keys = pygame.key.get_pressed()

    # read for up and down arrow key presses here
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

    # TODO: next time, read for left and right arrow key presses here

    # render element text 
    element_text = font.render(elements_text[current_element_index], True, WHITE)
    element_text_rect = element_text.get_rect()
    element_text_rect.center = pygame.math.Vector2(ITEM_X[0], SCREEN_HEIGHT / 2)

    #render acid text
    acid_text = font.render(f"acid: {current_acid}", True, WHITE)
    acid_text_rect = acid_text.get_rect()
    acid_text_rect.center = pygame.math.Vector2(ITEM_X[1], SCREEN_HEIGHT / 2)


    ##########################
    ### PART 2: DRAW STUFF ###
    ##########################

    # clear the screen before drawing anything else
    screen.fill(BLACK)

    # this code is rendering the text on screen
    screen.blit(element_text, element_text_rect)
    screen.blit(acid_text, acid_text_rect)

    # this code makes everything we've drawn appear on screen
    pygame.display.flip()

    ###################################
    ### PART 3: PREP FOR NEXT FRAME ###
    ###################################

    up_arow_prev_state = up_arow_curr_state
    dn_arow_prev_state = dn_arow_curr_state

    clock.tick(FPS)

pygame.quit()