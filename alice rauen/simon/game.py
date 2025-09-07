import pgzrun

WIDTH = 640
HEIGHT = 480

#chicken banana

# colors go here

lavender=(181,126,220)
columbia_BLUE=(155,221,255)

# rectangles go here
purple=Rect(0,0, WIDTH/2, HEIGHT/2)

def update():
    pass

def draw():
    screen.draw.filled_rect(purple,lavender)


pgzrun.go()
