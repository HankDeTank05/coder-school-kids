import pygame

# rendering variables
SCREEN_WIDTH = 1280 
SCREEN_HEIGHT = 720
FPS = 100
selected = 1
# game constants
MIN_ACID = 1 
MAX_ACID = 5
ITEMS_ON_SCREEN = 2
ITEM_X = []
for item_index in range(ITEMS_ON_SCREEN):
    x = (SCREEN_WIDTH / (ITEMS_ON_SCREEN + 1)) * (item_index + 1)
    ITEM_X.append(x)

HIGHLIGHT_RECT_WIDTH = 100
HIGHLIGHT_RECT_HEIGHT = 50

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

elements_text = ["ice", "earth", "magic"]
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

def prev_category():
    global category_index
    category_index -= 1
    if category_index < 0:
        category_index = len(ITEM_X) - 1

def next_category():
    global category_index
    category_index += 1 
    if category_index >= len(ITEM_X):
        category_index = 0


def prev_element():
    global current_element_index
    current_element_index -= 1
    if current_element_index == -1:  
        current_element_index += 3

def next_element():
    global current_element_index
    current_element_index += 1 # it adds one to the variable
    if current_element_index == 3: # if the index variable is too big, then....
        current_element_index -= 3 # decrease the index variable back to zero


def increase_acid():
    global current_acid
    current_acid += 1 # increses the amont of acid in the potion
    if current_acid > MAX_ACID: # if there is too much acid in the potion...
        current_acid = MIN_ACID # makes the least amoont of acid in the potion

def decrease_acid():
    global current_acid
    current_acid -= 1
    if current_acid < MIN_ACID:
        current_acid = MAX_ACID

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
        if category_index == 0: # cheak if you should modify the element
            next_element()
        elif category_index == 1: # otherwise cheak if you should modify the acid
            increase_acid()
    dn_arow_curr_state =  keys[pygame.K_DOWN]
    if dn_arow_curr_state == True and dn_arow_prev_state == False:
        if category_index == 0:
            prev_element()
        elif category_index == 1:
            decrease_acid()

    # read for left and right arrow key presses here
    lt_arow_curr_state = keys[pygame.K_LEFT]
    if lt_arow_curr_state == True and lt_arow_prev_state == False:
        prev_category()
    rt_arow_curr_state = keys[pygame.K_RIGHT]
    if rt_arow_curr_state == True and rt_arow_prev_state == False:
        next_category()

    # render element text 
    element_text = font.render(elements_text[current_element_index], True, WHITE)
    element_text_rect = element_text.get_rect()
    element_text_rect.center = pygame.math.Vector2(ITEM_X[0], SCREEN_HEIGHT / 2)

    #render acid text
    acid_text = font.render(f"acid: {current_acid}", True, WHITE)
    acid_text_rect = acid_text.get_rect()
    acid_text_rect.center = pygame.math.Vector2(ITEM_X[1], SCREEN_HEIGHT / 2)

    #this makes the highlight rect
    hlight_rect = pygame.Rect(0, 0, HIGHLIGHT_RECT_WIDTH, HIGHLIGHT_RECT_HEIGHT)
    hlight_rect.center = pygame.math.Vector2(ITEM_X[category_index], SCREEN_HEIGHT / 2)


    ##########################
    ### PART 2: DRAW STUFF ###
    ##########################

    # clear the screen before drawing anything else
    screen.fill(BLACK)

    # this code is rendering the text on screen
    screen.blit(element_text, element_text_rect)
    screen.blit(acid_text, acid_text_rect)

    # this code is rendering the highlight rectangle on screen
    pygame.draw.rect(screen, WHITE, hlight_rect, 10)

    # this code makes everything we've drawn appear on screen
    pygame.display.flip()

    ###################################
    ### PART 3: PREP FOR NEXT FRAME ###
    ###################################

    up_arow_prev_state = up_arow_curr_state
    dn_arow_prev_state = dn_arow_curr_state
    lt_arow_prev_state = lt_arow_curr_state
    rt_arow_prev_state = rt_arow_curr_state

    clock.tick(FPS)

pygame.quit()