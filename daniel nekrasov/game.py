import pygame

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

pos=pygame.math.Vector2(5,720/2)
facing=pygame.math.Vector2(1,0)
size=50

def player_update(_dt):
    global pos
    global facing
    pos_delta=pygame.math.Vector2(0,0)
    facing = pygame.math.Vector2(0,0)
    
    keys=pygame.key.get_pressed()
    if keys[pygame.K_w]:
        #move up
        pos_delta.y-=player_speed
        #look up
        facing.y -= 1
    if keys[pygame.K_a]:
        #move left
        pos_delta.x-=player_speed
        #look left
        facing.x -= 1
    if keys[pygame.K_s]:
        #move down
        pos_delta.y+=player_speed
        #look down
        facing.y += 1
    if keys[pygame.K_d]:
        #move right
        pos_delta.x+=player_speed
        #look down
        facing.x += 1

    if pos_delta.x != 0 and pos_delta.y != 0:
        pos_delta.normalize_ip()
        pos_delta *= player_speed
        facing.normalize_ip()


    pos_delta*=_dt
    pos+=pos_delta

def player_draw():
    pygame.draw.circle(screen, GREEN, pos, size)
    pygame.draw.line(screen, RED, pos, pos + facing * size)


#main game loop
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    player_update(dt)
    
    player_draw()

    pygame.display.flip()

    dt=clock.tick(60)/1000

pygame.quit()
