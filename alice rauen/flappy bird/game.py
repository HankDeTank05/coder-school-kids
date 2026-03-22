import os
os.environ['SDL_VIDEO_WINDOW_POS'] = f'{50},{50}'
import pgzrun
import random

WIDTH = 1280
HEIGHT = 720

bird=Actor('bird')
bird.pos = 100, 100
go_up=False

bg_1=Actor('bg')
bg_1.topleft = 0,0
bg_2=Actor('bg')
bg_2.topleft = WIDTH,0
bg_speed = 1

go=Actor('game')
go.topleft=0,0
show_go=False

GREEN=(67,179,174)
PIPE_WIDTH = 160
pipe_gap = 500
pipe_top=Rect(0,0,PIPE_WIDTH, 10)
pipe_Bottom=Rect(0,HEIGHT-100,PIPE_WIDTH, 100)
pipe_speed = 2

score=0
stop_moving = False

def respawn_pipes():
    global pipe_Bottom, pipe_top, score, pipe_speed,bg_speed,pipe_gap 
    pipe_top.topleft = WIDTH,0
    pipe_top.height=random.randint(25, 200)
    pipe_Bottom.topleft = WIDTH,pipe_top.height + pipe_gap
    pipe_Bottom.height = HEIGHT - pipe_Bottom.top
    score+=1
    pipe_speed+=1
    if pipe_gap > 200:
        pipe_gap-=1

    

def on_key_down(key):
    global go_up
    if key==key.UP:
        go_up=True

def update():
    global go_up, show_go
    # move the bird down
    bird.y+=5
    # print(score) 
    if go_up==True:
        go_up=False 
        bird.y-=130

    if bird.y - bird.height//2 <= 0:
        bird.y = bird.height//2
    elif bird.y + bird.height//2 >= HEIGHT:
        bird.y = HEIGHT - bird.height//2
    
    if not stop_moving:
        # move the backdrop
        bg_1.x-=bg_speed
        bg_2.x-=bg_speed

        if bg_1.midright[0]<=0:
            bg_1.topleft = WIDTH,0
        if bg_2.midright[0]<=0:
            bg_2.topleft = WIDTH,0

        # move the pipes
        pipe_top.x-=pipe_speed
        pipe_Bottom.x-=pipe_speed

    if pipe_top.midright[0]<0 and pipe_Bottom.midright[0]<0:
        respawn_pipes()

    if bird.colliderect(pipe_top) or bird.colliderect(pipe_Bottom):
        show_go=True
    

def draw():
    global stop_moving
    
    screen.clear()
    bg_1.draw() 
    bg_2.draw()
    
    bird.draw()
    screen.draw.filled_rect(pipe_top,GREEN)
    screen.draw.filled_rect(pipe_Bottom,GREEN)
    if show_go:
        go.draw()
        stop_moving=True
    screen.draw.text(str(score), (0,0), fontsize=70, color=(0,15,137))

pgzrun.go()