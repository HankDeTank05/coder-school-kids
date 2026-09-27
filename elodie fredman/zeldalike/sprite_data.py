from mysprite import MySprite
import os
import pygame
from common import *

# this is where MySprite objects are stored
# scroll down to see functions
my_sprite_data: dict[str, MySprite] = {
    'walk up 0': MySprite(
        path=os.path.join('elodie fredman', 'zeldalike', 'assets', 'sprites', 'link', 'walk_up_0.png'),
        hurtbox=pygame.Rect(2*SCALE_FACTOR, 0*SCALE_FACTOR, 12.5*SCALE_FACTOR, 16*SCALE_FACTOR)
    ),
    'walk up 1': MySprite(
        path=os.path.join('elodie fredman', 'zeldalike', 'assets', 'sprites', 'link', 'walk_up_1.png'),
        hurtbox=pygame.Rect(2*SCALE_FACTOR, 0*SCALE_FACTOR, 12.5*SCALE_FACTOR, 16*SCALE_FACTOR)
    ),
    'walk down 0': MySprite(
        path=os.path.join('elodie fredman', 'zeldalike', 'assets', 'sprites', 'link', 'walk_down_0.png'),
        hurtbox=pygame.Rect(2*SCALE_FACTOR, 0*SCALE_FACTOR, 13.5*SCALE_FACTOR, 16*SCALE_FACTOR)
    ),
    'walk down 1': MySprite(
        path=os.path.join('elodie fredman', 'zeldalike', 'assets', 'sprites', 'link', 'walk_down_1.png'),
        hurtbox=pygame.Rect(2*SCALE_FACTOR, 0*SCALE_FACTOR, 12.5*SCALE_FACTOR, 16*SCALE_FACTOR)
    ),
    'walk right 0': MySprite(
        path=os.path.join('elodie fredman', 'zeldalike', 'assets', 'sprites', 'link', 'walk_right_0.png'),
        hurtbox=pygame.Rect(1*SCALE_FACTOR, 0*SCALE_FACTOR, 13*SCALE_FACTOR, 16*SCALE_FACTOR)
    ),
    'walk right 1': MySprite(
        path=os.path.join('elodie fredman', 'zeldalike', 'assets', 'sprites', 'link', 'walk_right_1.png'),
        hurtbox=pygame.Rect(0*SCALE_FACTOR, 0*SCALE_FACTOR, 13*SCALE_FACTOR, 16*SCALE_FACTOR)
    ),
    'walk left 0': MySprite(
        path=os.path.join('elodie fredman', 'zeldalike', 'assets', 'sprites', 'link', 'walk_right_0.png'),
        hurtbox=pygame.Rect(0*SCALE_FACTOR, 0*SCALE_FACTOR, 16*SCALE_FACTOR, 16*SCALE_FACTOR),
        flip_h=True
    ),
    'walk left 1': MySprite(
        path=os.path.join('elodie fredman', 'zeldalike', 'assets', 'sprites', 'link', 'walk_right_1.png'),
        hurtbox=pygame.Rect(0*SCALE_FACTOR, 0*SCALE_FACTOR, 16*SCALE_FACTOR, 16*SCALE_FACTOR),
        flip_h=True
    ),
    'sword up 0': MySprite(
        path=os.path.join('elodie fredman', 'zeldalike', 'assets', 'sprites', 'link', 'sword_up_0.png'),
        hitbox=pygame.Rect(0*SCALE_FACTOR, 0*SCALE_FACTOR, 16*SCALE_FACTOR, 16*SCALE_FACTOR),
        hurtbox=pygame.Rect(0*SCALE_FACTOR, 0*SCALE_FACTOR, 16*SCALE_FACTOR, 16*SCALE_FACTOR)
    ),
    'sword up 1': MySprite(
        path=os.path.join('elodie fredman', 'zeldalike', 'assets', 'sprites', 'link', 'sword_up_1.png'),
        hitbox=pygame.Rect(0*SCALE_FACTOR, 0*SCALE_FACTOR, 16*SCALE_FACTOR, 16*SCALE_FACTOR),
        hurtbox=pygame.Rect(0*SCALE_FACTOR, 0*SCALE_FACTOR, 16*SCALE_FACTOR, 16*SCALE_FACTOR)
    ),
    'sword up 2': MySprite(
        path=os.path.join('elodie fredman', 'zeldalike', 'assets', 'sprites', 'link', 'sword_up_2.png'),
        hitbox=pygame.Rect(0*SCALE_FACTOR, 0*SCALE_FACTOR, 16*SCALE_FACTOR, 16*SCALE_FACTOR),
        hurtbox=pygame.Rect(0*SCALE_FACTOR, 0*SCALE_FACTOR, 16*SCALE_FACTOR, 16*SCALE_FACTOR)
    ),
    'sword up 3': MySprite(
        path=os.path.join('elodie fredman', 'zeldalike', 'assets', 'sprites', 'link', 'sword_up_3.png'),
        hitbox=pygame.Rect(0*SCALE_FACTOR, 0*SCALE_FACTOR, 16*SCALE_FACTOR, 16*SCALE_FACTOR),
        hurtbox=pygame.Rect(0*SCALE_FACTOR, 0*SCALE_FACTOR, 16*SCALE_FACTOR, 16*SCALE_FACTOR)
    ),
    'sword down 0': MySprite(
        path=os.path.join('elodie fredman', 'zeldalike', 'assets', 'sprites', 'link', 'sword_down_0.png'),
        hitbox=pygame.Rect(0*SCALE_FACTOR, 0*SCALE_FACTOR, 16*SCALE_FACTOR, 16*SCALE_FACTOR),
        hurtbox=pygame.Rect(0*SCALE_FACTOR, 0*SCALE_FACTOR, 16*SCALE_FACTOR, 16*SCALE_FACTOR)
    ),
    'sword down 1': MySprite(
        path=os.path.join('elodie fredman', 'zeldalike', 'assets', 'sprites', 'link', 'sword_down_1.png'),
        hitbox=pygame.Rect(0*SCALE_FACTOR, 0*SCALE_FACTOR, 16*SCALE_FACTOR, 16*SCALE_FACTOR),
        hurtbox=pygame.Rect(0*SCALE_FACTOR, 0*SCALE_FACTOR, 16*SCALE_FACTOR, 16*SCALE_FACTOR)
    ),
    'sword down 2': MySprite(
        path=os.path.join('elodie fredman', 'zeldalike', 'assets', 'sprites', 'link', 'sword_down_2.png'),
        hitbox=pygame.Rect(0*SCALE_FACTOR, 0*SCALE_FACTOR, 16*SCALE_FACTOR, 16*SCALE_FACTOR),
        hurtbox=pygame.Rect(0*SCALE_FACTOR, 0*SCALE_FACTOR, 16*SCALE_FACTOR, 16*SCALE_FACTOR)
    ),
    'sword down 3': MySprite(
        path=os.path.join('elodie fredman', 'zeldalike', 'assets', 'sprites', 'link', 'sword_down_3.png'),
        hitbox=pygame.Rect(0*SCALE_FACTOR, 0*SCALE_FACTOR, 16*SCALE_FACTOR, 16*SCALE_FACTOR),
        hurtbox=pygame.Rect(0*SCALE_FACTOR, 0*SCALE_FACTOR, 16*SCALE_FACTOR, 16*SCALE_FACTOR)
    ),
    'sword right 0': MySprite(
        path=os.path.join('elodie fredman', 'zeldalike', 'assets', 'sprites', 'link', 'sword_right_0.png'),
        hitbox=pygame.Rect(0*SCALE_FACTOR, 0*SCALE_FACTOR, 16*SCALE_FACTOR, 16*SCALE_FACTOR),
        hurtbox=pygame.Rect(0*SCALE_FACTOR, 0*SCALE_FACTOR, 16*SCALE_FACTOR, 16*SCALE_FACTOR)
    ),
    'sword right 1': MySprite(
        path=os.path.join('elodie fredman', 'zeldalike', 'assets', 'sprites', 'link', 'sword_right_1.png'),
        hitbox=pygame.Rect(0*SCALE_FACTOR, 0*SCALE_FACTOR, 16*SCALE_FACTOR, 16*SCALE_FACTOR),
        hurtbox=pygame.Rect(0*SCALE_FACTOR, 0*SCALE_FACTOR, 16*SCALE_FACTOR, 16*SCALE_FACTOR)
    ),
    'sword right 2': MySprite(
        path=os.path.join('elodie fredman', 'zeldalike', 'assets', 'sprites', 'link', 'sword_right_2.png'),
        hitbox=pygame.Rect(0*SCALE_FACTOR, 0*SCALE_FACTOR, 16*SCALE_FACTOR, 16*SCALE_FACTOR),
        hurtbox=pygame.Rect(0*SCALE_FACTOR, 0*SCALE_FACTOR, 16*SCALE_FACTOR, 16*SCALE_FACTOR)
    ),
    'sword right 3': MySprite(
        path=os.path.join('elodie fredman', 'zeldalike', 'assets', 'sprites', 'link', 'sword_right_3.png'),
        hitbox=pygame.Rect(0*SCALE_FACTOR, 0*SCALE_FACTOR, 16*SCALE_FACTOR, 16*SCALE_FACTOR),
        hurtbox=pygame.Rect(0*SCALE_FACTOR, 0*SCALE_FACTOR, 16*SCALE_FACTOR, 16*SCALE_FACTOR)
    ),
    'sword left 0': MySprite(
        path=os.path.join('elodie fredman', 'zeldalike', 'assets', 'sprites', 'link', 'sword_right_0.png'),
        hitbox=pygame.Rect(0*SCALE_FACTOR, 0*SCALE_FACTOR, 16*SCALE_FACTOR, 16*SCALE_FACTOR),
        hurtbox=pygame.Rect(0*SCALE_FACTOR, 0*SCALE_FACTOR, 16*SCALE_FACTOR, 16*SCALE_FACTOR),
        flip_h=True
    ),
    'sword left 1': MySprite(
        path=os.path.join('elodie fredman', 'zeldalike', 'assets', 'sprites', 'link', 'sword_right_1.png'),
        hitbox=pygame.Rect(0*SCALE_FACTOR, 0*SCALE_FACTOR, 16*SCALE_FACTOR, 16*SCALE_FACTOR),
        hurtbox=pygame.Rect(0*SCALE_FACTOR, 0*SCALE_FACTOR, 16*SCALE_FACTOR, 16*SCALE_FACTOR),
        flip_h=True
    ),
    'sword left 2': MySprite(
        path=os.path.join('elodie fredman', 'zeldalike', 'assets', 'sprites', 'link', 'sword_right_2.png'),
        hitbox=pygame.Rect(0*SCALE_FACTOR, 0*SCALE_FACTOR, 16*SCALE_FACTOR, 16*SCALE_FACTOR),
        hurtbox=pygame.Rect(0*SCALE_FACTOR, 0*SCALE_FACTOR, 16*SCALE_FACTOR, 16*SCALE_FACTOR),
        flip_h=True
    ),
    'sword left 3': MySprite(
        path=os.path.join('elodie fredman', 'zeldalike', 'assets', 'sprites', 'link', 'sword_right_3.png'),
        hitbox=pygame.Rect(0*SCALE_FACTOR, 0*SCALE_FACTOR, 16*SCALE_FACTOR, 16*SCALE_FACTOR),
        hurtbox=pygame.Rect(0*SCALE_FACTOR, 0*SCALE_FACTOR, 16*SCALE_FACTOR, 16*SCALE_FACTOR),
        flip_h=True
    ),
}

def load_my_sprite(key: str) -> MySprite:
    assert(key in my_sprite_data.keys())
    return my_sprite_data[key]

