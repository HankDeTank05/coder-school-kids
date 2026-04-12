import pgzrun
import random

WIDTH=300
HEIGHT=500

COLOR_BLUE=(0,0,255)
COLOR_SKY_BLUE=(135,206,235)
COLOR_DODGER_BLUE=(30,144,255)
COLOR_BROWN=(139,69,19)
COLOR_PURPLE = (155, 142, 199)



FLORE_HEIGHT=300
flore_rect=Rect(0,FLORE_HEIGHT,WIDTH,HEIGHT-FLORE_HEIGHT)
sky_rect=Rect(0,0,WIDTH,FLORE_HEIGHT)

BLOCK_SIZE=30
bird_rect=Rect(0, FLORE_HEIGHT-BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
block_list=[]

OBS_TIME=3
OBS_MAX_BLOCKS = 9 #number of blocks tall
time_since_obs = 0
obs_list=[]

def spawn_obs():
    obs_height = random.randint(1,OBS_MAX_BLOCKS)
    obs_width = obs_height
    obs_rect=Rect(270, FLORE_HEIGHT-BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
    return obs_rect


def on_mouse_down():
    if bird_rect.y>0:
        new_rect=Rect(0, FLORE_HEIGHT-BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
        for block in block_list:
            block.y-=BLOCK_SIZE
        bird_rect.y-=BLOCK_SIZE
        block_list.append(new_rect)


def update(frame_time):
    global time_since_obs 
    time_since_obs += frame_time
    if time_since_obs>=OBS_TIME:
        time_since_obs-=OBS_TIME
        obs_list.append(spawn_obs())

    # move obstacles
    for obs in obs_list:
        obs.x-=1

    # check for collision
    highest_pushed_block_index = len(block_list)
    for block_index in range(len(block_list)):
        block = block_list[block_index]
        for obs in obs_list:
            if block.colliderect(obs):
                block.right=obs.left
                highest_pushed_block_index = min(block_index, highest_pushed_block_index)


    # drop the block stack if there's nothing under it
    for block_index in range(len(block_list)):
        pass



def draw():
    screen.clear()
    screen.draw.filled_rect(sky_rect,COLOR_SKY_BLUE)
    screen.draw.filled_rect(flore_rect, COLOR_BROWN)
    screen.draw.filled_rect(bird_rect, COLOR_BLUE)
    #screen.draw.filled_rect(spawn_obs(),COLOR_PURPLE)
    for obs in obs_list:
        screen.draw.filled_rect(obs,COLOR_PURPLE)

    for block in block_list:
        screen.draw.rect(block,COLOR_DODGER_BLUE)



pgzrun.go()