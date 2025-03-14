import pygame
import copy

pygame.init()
WIDTH=1280
HEIGHT=720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True
dt=0

WHITE=(255,255,255)
GRAY=(128,128,128)
BLACK=(0,0,0)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)

player_speed=500

player_pos = pygame.math.Vector2(5,720/2)
player_facing = pygame.math.Vector2(1,0)
size=50

"""player functions"""

def player_update(_dt):
    global player_pos
    global player_facing
    pos_delta=pygame.math.Vector2(0,0)
    #player_facing = pygame.math.Vector2(0,0)
    
    keys=pygame.key.get_pressed()
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
    if keys[pygame.K_SPACE]:
        bullet_create(player_pos, player_facing)

    if pos_delta.length_squared() > 0:
        player_facing = copy.deepcopy(pos_delta)
        player_facing.normalize_ip()

    if pos_delta.x != 0 and pos_delta.y != 0:
        pos_delta.normalize_ip()
        pos_delta *= player_speed

    pos_delta *= _dt
    player_pos = player_pos + pos_delta

def player_draw():
    pygame.draw.circle(screen, GREEN, player_pos, size)
    pygame.draw.line(screen, RED, player_pos, player_pos + player_facing * size)

"""bullet functions"""

bullet_speed = 200
bullet_radius = 20
bullet_pos = []
bullet_dir = []

def bullet_create(_pos, _dir):
    global bullet_pos,bullet_dir
    bullet_pos.append(_pos)
    bullet_dir.append(_dir)

def bullet_update(_dt):
    pass

def bullet_draw():
    pass


#main game loop
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    # step 1: update stuff
    player_update(dt)

    # step 2: draw stuff
    player_draw()

    pygame.display.flip()

    dt=clock.tick(60)/1000

pygame.quit()
