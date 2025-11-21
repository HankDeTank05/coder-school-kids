import pgzrun

import random
import time

from pygame import Rect

WIDTH = 1920
HEIGHT = 1080

#chicken banana
CHICKEN_BANANA=Actor('chicken_banana!')
CHICKEN_BANANA.center=(WIDTH/2,HEIGHT/2)

LEVEL_UP=Actor('levelup')
LEVEL_UP.center=(WIDTH/2,HEIGHT/2)

GAME_OVER=Actor('dolphin')
GAME_OVER.center=(WIDTH/2,HEIGHT/2)

# colors go here
lavender=(181,126,220)
columbia=(155,221,255)
corel=(255,64,64)
ruby=(251,153,2)
white=(255,255,255)

# rectangles go here
purple=Rect(0,0, WIDTH/2, HEIGHT/2)
blue=Rect(WIDTH/2,0,WIDTH/2,HEIGHT/2)
red=Rect(0,HEIGHT/2,WIDTH/2,HEIGHT/2)
orange=Rect(WIDTH/2,HEIGHT/2,WIDTH/2,HEIGHT/2)

# rectangle constants
#PURPLE_END = (, purple.y+purple.height)
BLUE_END = (blue.x+blue.width, blue.y+blue.height)
RED_END = (red.x+red.width, red.y+red.height)
ORANGE_END = (orange.x+orange.width, orange.y+orange.height)

#current rect color
purple_color=lavender
blue_color=columbia 
red_color=corel
orange_color=ruby

# sequence
colors=['purple', 'blue', 'red', 'orange']
my_sequence=['purple']
click_counter=0
is_clicked=False
click_index = 0
sequence_index=0
sequence_timer=0
curent_color=None
game_state='sequence'
level_timer=0
game_over_timer=0

# my_sequence.append(random.choice(colors))
# my_sequence.append(random.choice(colors))
# my_sequence.append(random.choice(colors))
# my_sequence.append(random.choice(colors))
# my_sequence.append(random.choice(colors))
#for color in my_sequence:
#    print(color)
#    time.sleep(3)

def start_over():
    global my_sequence 
    global click_index
    global sequence_index
    global sequence_timer
    global game_over_timer
    game_over_timer = 0
    click_index=0
    sequence_index=0
    sequence_timer=0 
    my_sequence=[]
    new_color=random.choice(colors)
    my_sequence.append(new_color)

def level_up():
    global click_index
    global game_state
    global sequence_index
    global sequence_timer
    global level_timer
    print("LEVEL UP!")
    click_index=0
    sequence_index=0
    sequence_timer=0 
    new_color=random.choice(colors)
    my_sequence.append(new_color)
    game_state='level up'
    level_timer=0


def on_mouse_down(pos):
    global purple_color
    global blue_color
    global red_color
    global orange_color
    global is_clicked
    global click_index
    global game_state
    print(pos)
    # is_clicked=True
    # purple 
    if game_state=='play':
        click=None 
        if purple.left<pos[0]<purple.right and purple.top<pos[1]<purple.bottom:
            click=check_rect('purple')
            purple_color=white
        elif blue.left<pos[0]<blue.right and blue.top<pos[1]<blue.bottom:
            click=check_rect('blue')
            blue_color=white
        elif orange.left<pos[0]<orange.right and orange.top<pos[1]<orange.bottom:
            click=check_rect('orange')
            orange_color=white
        elif red.left<pos[0]<red.right and red.top<pos[1]<red.bottom:
            click=check_rect('red')
            red_color=white

        if click ==True:
            print("CORRECT")
            click_index+=1
            if click_index==len(my_sequence):
                level_up()


        elif click==False:
            game_state='GAME_OVER'


def on_mouse_up(pos):
    global purple_color,blue_color,orange_color,red_color
    if purple_color ==white:
        purple_color=lavender
    if blue_color ==white:
        blue_color=columbia
    if red_color ==white:
        red_color=corel
    if orange_color ==white:
        orange_color=ruby

def update():
    global sequence_index
    global sequence_timer
    global curent_color
    global purple_color
    global blue_color
    global red_color
    global orange_color
    global click_counter
    global is_clicked
    global game_state
    global level_timer
    global game_over_timer
    if game_state=='sequence':
        if sequence_index<len(my_sequence):
            curent_color=my_sequence[sequence_index]
            sequence_timer+=1
            if sequence_timer>=60:
                sequence_timer=0
                sequence_index+=1
                if sequence_index==len(my_sequence):
                    game_state='play'
                    curent_color=None 
        else:
            curent_color=None
    elif game_state=='level up':
        level_timer+=1
        if level_timer>=180:
            game_state='sequence'
    elif game_state=='GAME_OVER':
        game_over_timer+=1
        if game_over_timer>=180:
            start_over()
            game_state='sequence'

def draw():
    screen.clear()
    screen.draw.filled_rect(purple,purple_color)
    screen.draw.filled_rect(blue,blue_color)
    screen.draw.filled_rect(red,red_color)
    screen.draw.filled_rect(orange,orange_color)
    #determine where the chicken banana is going to go
    
    if game_state=='sequence':
        if curent_color=='blue':
            CHICKEN_BANANA.center=blue.center
            CHICKEN_BANANA.draw()
        elif curent_color=='purple':
            CHICKEN_BANANA.center=purple.center
            CHICKEN_BANANA.draw()
        elif curent_color=='orange':    
            CHICKEN_BANANA.center=orange.center
            CHICKEN_BANANA.draw()
        elif curent_color=='red':
            CHICKEN_BANANA.center=red.center
            CHICKEN_BANANA.draw()
    elif game_state=='level up':
        LEVEL_UP.draw()
    elif game_state=='GAME_OVER':
        GAME_OVER.draw()

def check_rect(color: str) -> bool:
    print(f"This ran and color: {color} and getnext: {get_next()}")
    if get_next() == color:
        return True
    return False

def get_next() -> str:
    return my_sequence[click_index]

pgzrun.go()
 
