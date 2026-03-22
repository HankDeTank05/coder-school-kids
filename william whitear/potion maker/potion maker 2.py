import pygame
import os.path
import random

# this showes that this is in devlopment
IN_DEVELOPMENT = True
#screen 
SCREEN_WIDTH = 1280
SCREEN_HIGHT = 720
FPS = 60

# game constants
MIN_ACID = 1
MAX_ACID = 3
ITEMS_ON_SCREEN = 2

ITEM_X = []
for i in range(ITEMS_ON_SCREEN):
    ITEM_X.append((SCREEN_WIDTH / ITEMS_ON_SCREEN + 1) * (i + 1))

HIGHLIGHT_RECT_WIDTH = 180
HIGHLIGHT_RECT_HIGHT = 60 
pygame.init()
BACKGROUND = pygame.color.Color(24, 28, 38)
PANEL = pygame.color.Color(40, 45, 60,)
TEXT = pygame.color.Color(100, 50, 40)
HIGHLIGHT = pygame.color.Color(0, 220, 220)
ACENT = pygame.color.Color(120, 160, 255)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HIGHT))
pygame.display.set_caption("potion maker.")
clock = pygame.time.Clock()
running = True 

#print(pygame.font.get_fonts())
#print(pygame.font.match_font("oldenglishtext"))
font = pygame.font.Font("C:\windows\Fonts\OLDENGL.TTF", 90)

element_text = ["water", "wind", "earth", "fire", "magic"]
current_element_index = 0

current_acid = MIN_ACID
acid_count = 0

potion_screen = False

potion_effects = {
    ("water", 1): "faild potion",
    ("water", 2): "drowning",
    ("water", 3): "acid rain",

    ("wind", 1): "smoke potion",
    ("wind", 2): "invis potion",
    ("wind", 3): "faild potion",

    ("earth", 1): "resistance",
    ("earth", 2): "faild potion", 
    ("earth", 3): "acid breath",

    ("fire", 1): "lava potion",
    ("fire", 2): "scalding",
    ("fire", 3): "faild potion",

    ("magic", 1): "fairy potion",
    ("magic", 2): "light potion",
    ("magic", 3): "mana potion"
}

customers = []
customer_count = 0

mouse_pressed_last_frame = False
mouse_just_pressed = False

def prev_element():
    global current_element_index
    current_element_index = (current_element_index - 1) % len(element_text) 
    
 
def next_element():
    global current_element_index
    current_element_index = (current_element_index + 1) % len(element_text) 

def add_acid():
    global acid_count
    acid_count += 1
    if acid_count >= 4: 
        acid_count = 0

def remove_acid():
    global acid_count
    acid_count -= 1
    if acid_count <= -1:
        acid_count = 3
    
def potion_scene():

    potion_background = pygame.image.load("potion back.png")
    potion_background = pygame.transform.scale(potion_background,(720, 720))

    screen.blit (potion_background, (0,0) )


    acid_up_arrow = pygame.image.load("up arrow.png")
    acid_up_arrow = pygame.transform.scale(acid_up_arrow, (160,160))

    acid_down_arrow = pygame.image.load("down arrow.png")
    acid_down_arrow = pygame.transform.scale(acid_down_arrow, (160,160))

    screen.blit(acid_up_arrow,(200, 48))
    screen.blit(acid_down_arrow,(200, 220))

    if mouse_just_pressed:
        if pygame.mouse.get_pos()[0] >= 200 and pygame.mouse.get_pos()[0] <= 360 and pygame.mouse.get_pos()[1] >= 48 and pygame.mouse.get_pos()[1] <= 208:
            add_acid()
        
        if pygame.mouse.get_pos()[0] <= 360 and pygame.mouse.get_pos()[0] >= 200 and pygame.mouse.get_pos()[1] >= 220 and pygame.mouse.get_pos()[1] <= 380:
            remove_acid()

    left_arrow = pygame.image.load("left arrow.png")
    left_arrow = pygame.transform.scale(left_arrow, (160,160))

    right_arrow = pygame.image.load("right arrow.png")
    right_arrow = pygame.transform.scale(right_arrow, (160,160))

    screen.blit(left_arrow,(650, 100))
    screen.blit(right_arrow,(800, 100))
 
    if mouse_just_pressed:
        if pygame.mouse.get_pos()[0] >= 650 and pygame.mouse.get_pos()[0] <= 810 and pygame.mouse.get_pos()[1] >= 100 and pygame.mouse.get_pos()[1] <= 260:
            next_element()
        
        if pygame.mouse.get_pos()[0] >= 800 and pygame.mouse.get_pos()[0] <= 960 and pygame.mouse.get_pos()[1] >= 100 and pygame.mouse.get_pos()[1] <= 260:
            prev_element()

    element = element_text[current_element_index]

    element_image = pygame.image.load(element + ".png")
    element_image = pygame.transform.scale(element_image, (112, 112))

    acid_image = pygame.image.load("acid 0.png")
    if acid_count == 1:
        acid_image = pygame.image.load("acid 1.png")
    elif acid_count == 2:
        acid_image = pygame.image.load("acid 2.png")
    elif acid_count == 3:
        acid_image = pygame.image.load("acid 3.png")
    acid_image = pygame.transform.scale(acid_image, (112,112))

    if acid_count == 0:
        potion = "empty"
    else:
        potion = potion_effects[(element, acid_count)]
 

    potion_image = pygame.image.load(potion + ".png")
    potion_image = pygame.transform.scale(potion_image, (250,250))
    

    order_paper = pygame.image.load("order paper.png")
    order_paper = pygame.transform.scale(order_paper, (380,380))


    screen.blit(order_paper,(850,300))
    screen.blit(acid_image,(228,155))
    screen.blit(potion_image,(1000, 50))
    screen.blit(element_image, (750, 125))
    
def shop_seen():
    global customers,customer_count
    
    #customers walk up to table
    if random.randint(1,100) <= 1:
        #1% chance
        customer_count += 1
        customer = pygame.image.load("wizard.png")
        customer = pygame.transform.scale(customer, (700,700))
        customers.append([customer, [0,100]])

    for customer in customers:
        screen.blit(customer[0], customer[1])
        #customer[1][0] += 1

    #foreground/table
    table = pygame.image.load("table 1.png")
    table = pygame.transform.scale(table, (1280,1280))
    sign = pygame.image.load("sign.png")
    sign = pygame.transform.scale(sign,(850,850))
    bell = pygame.image.load("bell.png") 
    bell = pygame.transform.scale(bell,(300,300))
    text = font.render("Waiting customers: " + str(customer_count), True, TEXT)

    screen.blit(table,(0,-400))
    screen.blit(sign,(350,0))
    screen.blit(bell,(50,290))
    screen.blit(text,(350,100))
    #order appears on paper
    #order carries over onto potion screen

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(BACKGROUND)
#potion shop
#customer comes up, makes vague request
#fit potion to request and give to customer
    if (not mouse_pressed_last_frame) and pygame.mouse.get_pressed()[0]:
        mouse_just_pressed = True
    else: 
        mouse_just_pressed = False
    if potion_screen:
        potion_scene() 
    else:
        shop_seen()



    mouse_pressed_last_frame = pygame.mouse.get_pressed()[0]
    pygame.display.flip()
    clock.tick(60)
    