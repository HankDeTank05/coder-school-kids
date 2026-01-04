import pgzrun

WIDTH=1920
HEIGHT=1080
 
WIDTH = 1280
HEIGHT = 720

#chicken banana
flappy=Actor('flappy')
flappy.pos = 100, 358
go_down=False
go_up=False




def on_key_down(key):
    global go_down, go_up
    if key==key.DOWN:
        go_down=True


    if key==key.UP:
        go_up=True


def on_key_up(key):
    global go_down, go_up 
    if key==key.DOWN:
        go_down=False
    
    if key==key.UP:
        go_up=False

def update():
    if go_down==True:
        flappy.y+=1
    if go_up==True:
        flappy.y-=1

def draw():
    screen.clear()
    flappy.draw()

pgzrun.go()