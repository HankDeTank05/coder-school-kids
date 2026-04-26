import pgzrun
import random

WIDTH=300
HEIGHT=500

COLOR_BLUE=(0,0,255)
COLOR_SKY_BLUE=(135,206,235)
COLOR_DODGER_BLUE=(30,144,255)
COLOR_BROWN=(139,69,19)
COLOR_PURPLE = (155, 142, 199)

# for me

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
    obs_height = random.randint(1, OBS_MAX_BLOCKS)
    print(obs_height)
    obs_width = obs_height
    obs_rect=Rect(270, FLORE_HEIGHT-BLOCK_SIZE*obs_height, BLOCK_SIZE, BLOCK_SIZE*obs_height)
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
    remove_indices = []
    for block_index in range(len(block_list)-1, -1, -1):
        block = block_list[block_index]
        something_below = False
        for obs in obs_list:
            if block.colliderect(obs):
                block.right=obs.left
                if block.right<0:
                    remove_indices.append(block_index)

    # remove offscreen blocks
    for remove_index in remove_indices:
        block_list.pop(remove_index)

    if len(block_list)>0 and block_list[-1].y <FLORE_HEIGHT-BLOCK_SIZE:
        block_list[-1].y+=1
        obs_bellow=False
        for obs in obs_list:
            if block_list[-1].colliderect(obs):
                obs_bellow=True
        if obs_bellow:
            block_list[-1].y-=1
        else:
            for block_index in range(len(block_list)-1):
                block=block_list[block_index]
                block.y+=1
            bird_rect.y+=1
    elif len(block_list)==0 and bird_rect.y<FLORE_HEIGHT-BLOCK_SIZE:
        bird_rect.y+=1



                                         

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