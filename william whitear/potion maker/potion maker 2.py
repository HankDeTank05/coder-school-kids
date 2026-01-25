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
    ITEM_X.append((SCREEN_WIDTH / ITEMS_ON_SCREEN + 1)) * (i = 1))

HIGHLIGHT_RECT_WIDTH = 180
HIGHLIGHT_RECT_HIGHT = 60 

BACKGROUND = pygame.color(24, 28, 38)
PANEL = pygame.color(40, 45, 60,)
TEXT = pygame.color(235, 235, 235)
HIGHLIGHT = pygame.color (0, 220, 220)
ACENT = pygame.color(120, 160, 255)

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HIGHT))
pygame.display.set_caption("potion maker.")
clock = pygame.time.Clock
running = True 

item_catagories = ["element", "acid"]
catagory_index = 0

element_text = ["water", "wind", "earth", "fire", "magic"]
current_element_index = 0 

current_acid = MIN_ACID


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

prev_keys = pygame.key.get_pressed()
def prev_catagory():
    global catagory_index
    catagory_index = (catagory - 1) % len(item_catagories)
 
 def prev_catagory():
    global catagory_index = (catagory -1) % len(item_catagories)

def next_catagory():
    global current_element_index
    current_element_index = (current_element_index - 1) % len(element_text)
































































































































