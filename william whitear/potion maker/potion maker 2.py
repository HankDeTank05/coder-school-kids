import pygame
import os.path

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
TEXT = pygame.color.Color(235, 235, 235)
HIGHLIGHT = pygame.color.Color(0, 220, 220)
ACENT = pygame.color.Color(120, 160, 255)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HIGHT))
pygame.display.set_caption("potion maker.")
clock = pygame.time.Clock()
running = True 

item_catagories = ["element", "acid"]
catagory_index = 0

element_text = ["water", "wind", "earth", "fire", "magic"]
current_element_index = 0 

current_acid = MIN_ACID
acid_count = 0

potion_effects = {
    ("water", 1): "water breathing",
    ("water", 2): "ice sheald",
    ("water", 3): "tidal wave",

    ("wind", 1): "Feather Fall",
    ("wind", 2): "Swift Dash",
    ("wind", 3): "Hurricane",

    ("earth", 1): "Stone Skin",
    ("earth", 2): "Root Bind", 
    ("earth", 3): "Earthquake",

    ("fire", 1): "Fire Resistance",
    ("fire", 2): "flame burst",
    ("fire", 3): "inferno",

    ("magic", 1): "mana boost",
    ("magic", 2): "spell power",
    ("magic", 3): "arcane overlode"
}

def prev_catagory():
    global catagory_index
    catagory_index = (catagory_index - 1) % len(item_catagories)
 
def next_catagory():
    global catagory_index
    catagory_index = (catagory_index + 1) % len(item_catagories)

def add_acid():
    acid_count += 1

def remove_acid():
    acid_count -= 1

def potion_scene():
    acid_up_arrow = pygame.image.load("up arrow.png")
    acid_up_arrow = pygame.transform.scale(acid_up_arrow, (160,160))

    acid_down_arrow = pygame.image.load("down arrow.png")
    acid_down_arrow = pygame.transform.scale(acid_down_arrow, (160,160))


    screen.blit(acid_up_arrow,(200, 48))
    screen.blit(acid_down_arrow,(200, 220))
    potion_image = pygame.image.load("empty.png")
    potion_image = pygame.transform.scale(potion_image, (128,128))
    acid_image = pygame.image.load("acid 0.png")
    if acid_count == 1:
        acid_image = pygame.image.load("acid 1.png")
    elif acid_count == 2:
        acid_image = pygame.image.load("acid 2.png")
    if acid_count == 3:
        acid_image = pygame.image.load("acid 3.png")
    acid_image = pygame.transform.scale(acid_image, (96,96))

    screen.blit(acid_image,(232,150))
    screen.blit(potion_image,(1000, 100))

    


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(BACKGROUND)
#potion shop
#customer comes up, makes vague request
#fit potion to request and give to customer
    potion_scene()




    pygame.display.flip()
    clock.tick(60)





















































































































