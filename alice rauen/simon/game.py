import pgzrun

import random
import time

WIDTH = 640
HEIGHT = 480

#chicken banana
CHICKEN_BANANA=Actor('chicken_banana!')
CHICKEN_BANANA.center=(320,240)

LEVEL_UP=Actor('LEVELUP')
LLEEVVEELL__UUPP
# colors go here
lavender=(181,126,220)
columbia=(155,221,255)
corel=(255,64,64)
ruby=(251,153,2)

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

# sequence
colors=['purple', 'blue', 'red', 'orange']
my_sequence=['purple']
number=0000
time_counter=0
curent_color=None

my_sequence.append(random.choice(colors))
my_sequence.append(random.choice(colors))
my_sequence.append(random.choice(colors))
my_sequence.append(random.choice(colors))
my_sequence.append(random.choice(colors))
#for color in my_sequence:
#    print(color)
#    time.sleep(3)

def on_mouse_down(pos):
    print(pos)
    # purple 
    if purple.left<pos[0]<purple.right and purple.top<pos[1]<purple.bottom:
        print('purple clicked')
    elif blue.left<pos[0]<blue.right and blue.top<pos[1]<blue.bottom:
        print('blue clicked')
    elif orange.left<pos[0]<orange.right and orange.top<pos[1]<orange.bottom:
        print('orange clicked')
    elif red.left<pos[0]<red.right and red.top<pos[1]<red.bottom:
        print('red clicked')

def update():
    global time_counter
    global number
    global curent_color
    if number<len(my_sequence):
        curent_color=my_sequence[number]
    else:
        curent_color=None
    time_counter+=1
    if time_counter==120:
        print(curent_color)
        time_counter=0
        number+=1
        # TODO: next time, if number is to big, set current color to None
        if number>=len(my_sequence):
            curent_color=None 

def draw():
    screen.draw.filled_rect(purple,lavender)
    screen.draw.filled_rect(blue,columbia)
    screen.draw.filled_rect(red,corel)
    screen.draw.filled_rect(orange,ruby)
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



pgzrun.go()
 
