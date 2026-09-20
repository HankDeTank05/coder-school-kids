# Example file showing a basic pygame "game loop"
from copy import deepcopy
import random

import pygame

from common import *

from snake import Snake

# pygame setup
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

# SNAKE STUFF

snakepigs=Snake(
    head_color = pygame.Color('orchid4'),
    tail_color=pygame.Color('slateblue1'),
    face_color=pygame.Color('orchid'),
    up_ctrl=pygame.K_UP,
    down_ctrl=pygame.K_DOWN,
    left_ctrl=pygame.K_LEFT,
    right_ctrl=pygame.K_RIGHT
)
snakesheep=Snake(
    head_color=pygame.Color('red'),
    tail_color=pygame.Color('salmon'),
    face_color=pygame.Color('coral'),
    up_ctrl=pygame.K_w,
    down_ctrl=pygame.K_s,
    left_ctrl=pygame.K_a,
    right_ctrl=pygame.K_d
)

# FOOD STUFF

food=[]
food_colors=[]
food_rects=[]
food_size=10 # radius of the circle

def spawn_food():
    x=random.randint(food_size,WIDTH-1-food_size)
    y=random.randint(food_size+13,HEIGHT-1-food_size)
    food.append(pygame.math.Vector2(x,y))
    food_colors.append(random.choice(FOOD_COLORS))
    food_rect=pygame.Rect(
        x-food_size, y-food_size, #top left corner
        food_size*2, food_size*2 #width and height
    )
    food_rects.append(food_rect)

def spawn_foods(count):
    for f in range(count):
        spawn_food()

def update_foods():
    pass

def draw_food():
    for i in range(len(food_colors)):
        food_pos = food[i]
        food_color = food_colors[i]
        pygame.draw.circle(screen, food_color ,food_pos, food_size)


def collision(mouth_rect)->None:
    # it checks if it eats any of the food
    food_index=mouth_rect.collidelist(food_rects)
    if food_index != -1: # -1 means we ate no food
        # if we DID eat food...
        # make the food react to being eaten (get rid of the piece that was eaten)
        food.pop(food_index) # ...remove the eaten food from the list
        food_rects.pop(food_index) # ...remove the corresponding rectangle
        eaten_color=food_colors.pop(food_index) # ...remove the corresponding color
        # make the snake react to eating the food (add a segment to the snake)
        '''
        new_seg = deepcopy(seg_list[-1])
        last_move = deepcopy(moves[-1])
        last_move *= -speed
        new_seg.move_ip(last_move.x, last_move.y)
        seg_list.append(new_seg)
        moves.append(pygame.math.Vector2(0,0))
        for i in range(len(colors)):
            colors[i] = head_color.lerp(tail_color, i/len(colors))
        colors.append(tail_color)
        # colors.append(eaten_color)
        '''



spawn_foods(STARTING_FOOD_COUNT)


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # UPDATE THE GAME

    keys = pygame.key.get_pressed()
    snakepigs.update(keys)
    snakesheep.update(keys)

    if snakepigs.hitbox is not None:
        collision(snakepigs.hitbox)
    if snakesheep.hitbox is not None:
        collision(snakesheep.hitbox)

    # DRAW THE GAME

    # fill the screen with a color to wipe away anything from last frame
    screen.fill(BACKGROUND_COLOR)

    # draw_snake(screen)
    snakepigs.draw(screen)
    snakesheep.draw(screen)
    draw_food()


    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()