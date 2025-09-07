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
green=(0,255,0)
blue=(71,159,214)
# colors by usage
background=light_sky_blue

##################
# game variables #
##################

# start the game with zero clicks
clicks=0
clicks_per_click=2

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
orange_cost=150

# yellow button
buy_yellow=Rect(0,140,100,70)
yellow_cost=250

#green button
buy_green=Rect(0,210,100,70)
green_cost=150

#clicker upgrde
buy_clicker=Rect(700,0,100,70)
clicker_cost=300

def on_mouse_down(pos, button):
    global clicks, clicks_per_click, background
    
    # check if mouse is in red box and that they have enough clicks to buy the red
    if buy_red.collidepoint(pos) and clicks >= red_cost:
        # decrease clicks by the cost of red
        clicks-=red_cost
        background=red
    elif buy_orange.collidepoint(pos)and clicks >= orange_cost:
        background=pumpkin
        clicks-=orange_cost 
    elif buy_yellow.collidepoint(pos)and clicks >= yellow_cost:
        background=lemon_yellow
        clicks-=yellow_cost
    elif buy_clicker.collidepoint(pos)and clicks >= clicker_cost:
        clicks_per_click+=2
        clicks-=clicker_cost
    elif cookie.collidepoint(pos):
        clicks+=clicks_per_click
    elif buy_green.collidepoint(pos)and clicks >= green_cost:
        background=green
        clicks-=green_cost
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
    screen.draw.filled_rect(buy_yellow, lemon_yellow)
    screen.draw.filled_rect(buy_clicker, black)
    screen.draw.filled_rect(buy_green,green)
    # TODO: draw the number of clicks on screen
    screen.draw.text(str(clicks), midright=(WIDTH,HEIGHT/2))

    # write_scree
    screen.draw.text(str(red_cost),buy_red.topleft) 
    screen.draw.text(str(orange_cost), buy_orange.topleft)
    screen.draw.text(str(yellow_cost),buy_yellow.topleft) 
    screen.draw.text(str(clicker_cost), buy_clicker.topleft)
    screen.draw.text(str(green_cost),buy_green.topleft)
    
pgzrun.go()

