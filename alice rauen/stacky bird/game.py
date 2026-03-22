import pgzrun
import random

WIDTH=300
HEIGHT=500

COLOR_BLUE=(0,0,255)
COLOR_SKY_BLUE=(135,206,235)
COLOR_DODGER_BLUE=(30,144,255)
COLOR_BROWN=(139,69,19)

FLORE_HEIGHT=300
flore_rect=Rect(0,FLORE_HEIGHT,WIDTH,HEIGHT-FLORE_HEIGHT)
sky_rect=Rect(0,0,WIDTH,FLORE_HEIGHT)

BLOCK_SIZE=30
bird_rect=Rect(0, FLORE_HEIGHT-BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
block_list=[]

OBS_TIME=3
OBS_MAX_HEIGHT=9 #number of blocks tall
time_since_obs=0

def spawn_obs():
    obs_height=random.randint(1,OBS_MAX_HEIGHT)

def on_mouse_down():
    if bird_rect.y>0:
        new_rect=Rect(0, FLORE_HEIGHT-BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
        for block in block_list:
            block.y-=BLOCK_SIZE
        bird_rect.y-=BLOCK_SIZE
        block_list.append(new_rect)


def update(frame_time):
    time_since_obs+=frame_time
    if time_since_obs>=OBS_TIME:
        time_since_obs-=OBS_TIME


def draw():
    screen.clear()
    screen.draw.filled_rect(sky_rect,COLOR_SKY_BLUE)
    screen.draw.filled_rect(flore_rect, COLOR_BROWN)
    screen.draw.filled_rect(bird_rect, COLOR_BLUE)
    for block in block_list:
        screen.draw.rect(block,COLOR_DODGER_BLUE)

pgzrun.go()