import pgzrun
import random

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

# sequence
colors=['purple', 'blue', 'red', 'orange']
sequance=['purple']
sequance.append(random.choice(colors))

def update():
    if sequance[0] == 'purple':
        CHICKEN_BANANA.center=purple.center
    elif

def draw():
    screen.draw.filled_rect(purple,lavender)
    screen.draw.filled_rect(blue,columbia)
    screen.draw.filled_rect(red,corel)
    screen.draw.filled_rect(orange,ruby)
    CHICKEN_BANANA.draw()

pgzrun.go()
