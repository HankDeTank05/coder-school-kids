import pgzrun

# screen size
WIDTH = 800
HEIGHT = 450

##########
# colors #
##########

# colors by name
black=(255, 255, 255)
white=(0, 0, 0)
light_sky_blue = (135, 206, 250)
red=(255,0,56)
lemon_yellow=(255,244,79)
pumpkin=(255,117,24)

# colors by usage
background=light_sky_blue

##################
# game variables #
##################

# start the game with zero clicks
clicks=0

# create the cookie that we want to click
cookie=Actor('cookie')
cookie.pos= WIDTH/2 , HEIGHT/2 # <-- x, y

#######################
# create some buttons #
#######################

# red button
buy_red=Rect(0,0,100,70) # <-- x, y, width, height
red_cost=250

# orange button
buy_orange=Rect(0,70,100,70)
ORANGE_COST=150
def on_mouse_down(pos, button):
    global clicks, background
    
    # check if mouse is in red box and that they have enough clicks to buy the red
    if buy_red.collidepoint(pos) and clicks >= red_cost:
        # decrease clicks by the cost of red
        clicks-=red_cost
        background=red
    elif buy_orange.collidepoint(pos)and clicks >= ORANGE_COST:
        background=pumpkin
        clicks-=orange_cost 
    else:
        # TODO: make it so they must click the cookie in order to get clicks
        clicks+=2
    
    print(clicks) # TODO: get rid of this once the clicks are being drawn on the screen!

def draw():
    screen.clear()

    # screen is light blue
    screen.fill(background)
    
    # draw the cookie
    cookie.draw()

    # draw the red button
    screen.draw.filled_rect(buy_red, red)
    screen.draw.filled_rect(buy_orange,pumpkin)
    

    # TODO: draw the number of clicks on screen
    screen.draw.text(str(clicks), midright=(WIDTH,HEIGHT/2))

    # write_scree
    screen.draw.text(str(red_cost),buy_red.topleft) 
    
    
pgzrun.go()

