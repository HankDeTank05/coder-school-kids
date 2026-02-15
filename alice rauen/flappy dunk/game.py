import os
os.environ['SDL_VIDEO_WINDOW_POS'] = f'{50},{50}'
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

game_over=Actor('bird8910dot12345ngrhj')

score=0
did_score = False


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

def update():
    global go_up, score, did_score
    
    # move the ball down
    flappy.y+=5 

    # it makes the ball go up
    if go_up==True:
        go_up=False
        flappy.y-=130

    # this code makes the ball stop at the top of the screen
    # if flappy.y<0:
    #     flappy.y=0

    # they move the ring left 
    ring_speed=5
    ring_back.x-=ring_speed
    ring_front.x-=ring_speed

    # this code makes the ring loop around the screen
    if ring_back.right<0:
        ring_back.left=WIDTH
    if ring_front.right<0:
        ring_front.left=WIDTH
        did_score = False


    # this code checks for a basket
    if did_score == False:
        if flappy.midtop[1]<ring_front.midbottom[1]<flappy.midbottom[1]:
            if hoop_width/2-ball_width/2>=abs(flappy.center[0]-ring_front.center[0]):
                # print('swish')
                score+=3
                did_score = True
            elif (hoop_width/2-ball_width/2)+rim_width>=abs(flappy.center[0]-ring_front.center[0]):
                # print('basket')
                score+=1
                did_score = True
            else:
                # print('miss')
                pass
            # print(score)


def draw():
    screen.clear()
    ring_back.draw()
    flappy.draw()
    ring_front.draw()
    screen.draw.text(f"Score: {score}",(0,0),fontsize=50)

    # this code displays the game over screen
    if flappy.y>HEIGHT or flappy.y<0:
        game_over.draw()



pgzrun.go()