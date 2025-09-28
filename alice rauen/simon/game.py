import pgzrun

import random
import time

WIDTH = 640
HEIGHT = 480

#chicken banana
CHICKEN_BANANA=Actor('chicken_banana!')
CHICKEN_BANANA.center=(320,240)

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
my_sequence.append(random.choice(colors))
for color in my_sequence:
    print(color)
    time.sleep(3)

def on_mouse_down(pos):
    print(pos)
    # purple 
    if purple.left<pos[0]<purple.right and purple.top<pos[1]<purple.bottom:
        print('purple')
    elif blue.left<pos[0]<blue.right and blue.top<pos[1]<blue.bottom:
        print('blue')
    elif orange.left<pos[0]<orange.right and orange.top<pos[1]<orange.bottom:
        print('orange')
    elif red.left<pos[0]<red.right and red.top<pos[1]<red.bottom:
        print('red')

def update():
    pass


def draw():
    screen.draw.filled_rect(purple,lavender)
    screen.draw.filled_rect(blue,columbia)
    screen.draw.filled_rect(red,corel)
    screen.draw.filled_rect(orange,ruby)
    CHICKEN_BANANA.draw()



pgzrun.go()
 
