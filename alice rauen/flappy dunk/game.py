import pgzrun

WIDTH=1280
HEIGHT=720
 
WIDTH = 1280
HEIGHT = 720

#chicken banana
flappy=Actor('flappy')
flappy.pos = 100, 358
go_down=False
go_up=False
ball_width=160

ring=Actor("ring")
ring.pos = 667, 467
hoop_width=239
rim_width=73



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
    
    flappy.y+=1
    if go_up==True:
        flappy.y-=2
    ring.x-=1
    if ring.right<0:
        ring.left=WIDTH

    if hoop_width/2-ball_width/2>=abs(flappy.center[0]-ring.center[0]):
        print('swish')
    elif (hoop_width/2-ball_width/2)+rim_width>=abs(flappy.center[0]-ring.center[0]):
        print('basket')
    else:
        print('mrs')





def draw():
    screen.clear()
    ring.draw()
    flappy.draw()

pgzrun.go()