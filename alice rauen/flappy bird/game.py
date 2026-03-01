import os
os.environ['SDL_VIDEO_WINDOW_POS'] = f'{50},{50}'
import pgzrun
import random

WIDTH = 1280
HEIGHT = 720

bird=Actor('bird')
bird.pos = 100, 358
go_up=False

bg_1=Actor('bg')
bg_1.topleft = 0,0
bg_2=Actor('bg')
bg_2.topleft = WIDTH-1,0

GREEN=(0,255,0)
PIPE_WIDTH = 160
PIPE_GAP = 300
pipe_top=Rect(0,0,PIPE_WIDTH, 10)
pipe_Bottom=Rect(0,HEIGHT-100,PIPE_WIDTH, 100)

def respawn_pipes():
    global pipe_Bottom, pipe_top 
    pipe_top.topleft = WIDTH,0
    pipe_top.height=random.randint(25 ,200)
    pipe_Bottom.height=random.randint(400,500)
    pipe_Bottom.topleft = WIDTH,HEIGHT-pipe_Bottom.size[1]
    

def on_key_down(key):
    global go_up
    if key==key.UP:
        go_up=True

def update():
    global go_up
    # move the bird down
    bird.y+=5

    if go_up==True:
        go_up=False 
        bird.y-=130

    if bird.y - bird.height//2 <= 0:
        bird.y = bird.height//2
    elif bird.y + bird.height//2 >= HEIGHT:
        bird.y = HEIGHT - bird.height//2
    
    # move the backdrop
    bg_1.x-=1
    bg_2.x-=1

    if bg_1.midright[0]<0:
        bg_1.topleft = WIDTH,0
    if bg_2.midright[0]<0:
        bg_2.topleft = WIDTH-1,0

    # move the pipes
    pipe_top.x-=2
    pipe_Bottom.x-=2

    if pipe_top.midright[0]<0 and pipe_Bottom.midright[0]<0:
        respawn_pipes()
    

def draw():
    screen.clear()
    bg_1.draw() 
    bg_2.draw()
    
    bird.draw()
    screen.draw.filled_rect(pipe_top,GREEN)
    screen.draw.filled_rect(pipe_Bottom,GREEN)

pgzrun.go()