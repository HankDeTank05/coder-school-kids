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

ring_back=Actor("pigai123back")
ring_back.pos = 667, 467
ring_front=Actor("lionabz456frontsixseven")
ring_front.pos=667,563
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
    
    # if key==key.UP:

def update():
    global go_up
    
    flappy.y+=1
    if go_up==True:
        go_up=False
        flappy.y-=67
    ring_back.x-=1
    ring_front.x-=1
    if ring_back.right<0:
        ring_back.left=WIDTH

    if hoop_width/2-ball_width/2>=abs(flappy.center[0]-ring_back.center[0]):
        print('swish')
    elif (hoop_width/2-ball_width/2)+rim_width>=abs(flappy.center[0]-ring_back.center[0]):
        print('basket')
    else:
        print('mrs')





def draw():
    screen.clear()
    ring_back.draw()
    flappy.draw()
    ring_front.draw()

pgzrun.go()