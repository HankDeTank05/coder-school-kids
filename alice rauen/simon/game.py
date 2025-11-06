# TO HENRY: Implement click checking logic, increment seq_index on clicks, etc

import pgzrun

import random
import time

from pygame import Rect

WIDTH = 640
HEIGHT = 480

#chicken banana
CHICKEN_BANANA=Actor('chicken_banana!')
CHICKEN_BANANA.center=(320,240)

LEVEL_UP=Actor('levelup')
# colors go here
lavender=(181,126,220)
columbia=(155,221,255)
corel=(255,64,64)
ruby=(251,153,2)
white=(255,255,255)

# rectangles go here
purple=Rect(0,0, WIDTH/2, HEIGHT/2)
blue=Rect(320,0,WIDTH/2,HEIGHT/2)
red=Rect(0,240,WIDTH/2,HEIGHT/2)
orange=Rect(320,240,WIDTH/2,HEIGHT/2)

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
number=0000
click_counter=0
is_clicked=False
seq_index = 0
curent_color=None

# my_sequence.append(random.choice(colors))
# my_sequence.append(random.choice(colors))
# my_sequence.append(random.choice(colors))
# my_sequence.append(random.choice(colors))
# my_sequence.append(random.choice(colors))
#for color in my_sequence:
#    print(color)
#    time.sleep(3)

def level_up():
    global seq_index
    print("LEVEL UP!")
    seq_index=0
    new_color=random.choice(colors)
    my_sequence.append(new_color)


def on_mouse_down(pos):
    global purple_color
    global blue_color
    global red_color
    global orange_color
    global is_clicked
    global seq_index
    print(pos)
    # is_clicked=True
    # purple 
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
        seq_index+=1
        if seq_index ==len(my_sequence):
            level_up()


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
    global number
    global curent_color
    global purple_color
    global blue_color
    global red_color
    global orange_color
    global click_counter
    global is_clicked
    if number<len(my_sequence):
        curent_color=my_sequence[number]
    else:
        curent_color=None
    # if is_clicked:
    #     click_counter+=1
    # if click_counter>=15:
    #     purple_color=lavender
    #     blue_color=columbia
    #     red_color=corel
    #     orange_color=ruby
    #     click_counter=0

def draw():
    screen.draw.filled_rect(purple,purple_color)
    screen.draw.filled_rect(blue,blue_color)
    screen.draw.filled_rect(red,red_color)
    screen.draw.filled_rect(orange,orange_color)
    #determine where the chicken banana is going to go
    
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
    elif curent_color == None:
        pass

def check_rect(color: str) -> bool:
    print(f"This ran and color: {color} and getnext: {get_next()}")
    if get_next() == color:
        return True
    return False

def get_next() -> str:
    return my_sequence[seq_index]

pgzrun.go()
 
