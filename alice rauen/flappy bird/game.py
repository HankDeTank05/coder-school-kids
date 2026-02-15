import os
os.environ['SDL_VIDEO_WINDOW_POS'] = f'{50},{50}'
import pgzrun

WIDTH = 1280
HEIGHT = 720

bird=Actor('bird')
bird.pos = 100, 358
go_up=False

def on_key_down(key):
    global go_up
    if key==key.UP:
        go_up=True

def update():
    # move the bird down
    bird.y+=5

    if go_up==True:
        go_up=False 
        bird.y-=130

def draw():
    screen.clear() 
    bird.draw()

pgzrun.go()