import pgzrun

# screen size
WIDTH = 800
HEIGHT = 450

# colors
light_sky_blue = (135, 206, 250)
red=(255,0,56)
lemon_yellow=(255,244,79)
pumpkin=(255,117,24)

# start the game with zero clicks
clicks=0

# create the cookie that we want to click
cookie=Actor('cookie')
#           X , Y
cookie.pos= WIDTH/2 , HEIGHT/2

# create some buttons
buy_red=Rect(0,0,100,70)
red_cost=104

def on_mouse_down(pos, button):
    global clicks

    # check if mouse is in red box
    if buy_red.collidepoint(pos):
        # decrease clicks by the cost of red (aka, 104)
        clicks-=red_cost
    else:
        clicks+=2
    
    print(clicks)

def draw():
    screen.clear()

    # screen is light blue
    screen.fill(light_sky_blue)
    
    # draw the cookie
    cookie.draw()

    # draw the red button
    screen.draw.filled_rect(buy_red,red)
    
pgzrun.go()

