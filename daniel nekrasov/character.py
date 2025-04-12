import pygame

import common as c

import bullet

"""player functions"""



player_speed=500

player_pos = pygame.math.Vector2(5,720/2)
player_facing = pygame.math.Vector2(1,0)
size=50

prev_m1_state = False
prev_m2_state = False

def player_update(_dt):
    global player_pos
    global player_facing
    global prev_m1_state, prev_m2_state
    pos_delta=pygame.math.Vector2(0,0)
    #player_facing = pygame.math.Vector2(0,0)
    
    keys=pygame.key.get_pressed()
    mouse_buttons = pygame.mouse.get_pressed()
    # TODO: come back and figure out a way to prevent diagonal-movement key releases from reading as straightine directions sometimes
    if keys[pygame.K_w]:
        #move up
        pos_delta.y -= player_speed
    if keys[pygame.K_a]:
        #move left
        pos_delta.x -= player_speed
    if keys[pygame.K_s]:
        #move down
        pos_delta.y += player_speed
    if keys[pygame.K_d]:
        #move right
        pos_delta.x += player_speed

    # detemine state for left mouse button
    current_m1_state = mouse_buttons[0]
    current_m2_state = mouse_buttons[1]
    # TODO: come back and move the following lines of code if there are problems with aiming direction
    if prev_m1_state == False and current_m1_state == True:
        #shoot
        bullet.bullet_create(player_pos, player_facing)

    
    # fix diagonal movement so it isn't faster than straightline speed
    if pos_delta.x != 0 and pos_delta.y != 0:
        pos_delta.normalize_ip()
        pos_delta *= player_speed

    pos_delta *= _dt
    player_pos += pos_delta #move player
    # player_pos = player_pos + pos_delta

    # caluculate facing direction
    player_facing = pygame.mouse.get_pos() - player_pos
    player_facing.normalize_ip()

    # set prev states for next frame
    prev_m1_state = current_m1_state
    prev_m2_state = current_m2_state



def player_draw():
    pygame.draw.circle(c.screen, c.GREEN, player_pos, size)
    pygame.draw.line(c.screen, c.RED, player_pos, player_pos + player_facing * size)
