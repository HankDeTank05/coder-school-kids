# Example file showing a basic pygame "game loop"
import random

import pygame

# pygame setup
WIDTH=1280
HEIGHT=720
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

# SNAKE STUFF
segments=22
seg_size = 48 # size of the square

speed=6
seg_list=[]

moves=[]

colors=[]
head_color = pygame.Color('skyblue1')
tail_color = pygame.Color('black')
for i in range(segments):
    seg_list.append(pygame.Rect(0,0,seg_size,seg_size))
    moves.append(pygame.math.Vector2(0,0))
    colors.append(head_color.lerp(tail_color, i/segments))

def update_snake():
    keys=pygame.key.get_pressed()
    new_move=pygame.math.Vector2(0,0)
    if keys[pygame.K_UP]:
        new_move.y-=speed
    if keys[pygame.K_DOWN]:
        new_move.y+=speed
    if keys[pygame.K_LEFT]:
        new_move.x-=speed
    if keys[pygame.K_RIGHT]:
        new_move.x+=speed

    if new_move.length_squared()>0:
        new_move.normalize_ip()
        moves.insert(0,new_move)
        old_move=moves.pop()

        # player[0].move_ip(move.x,move.y) 
        for i in range(len(seg_list)):
            move=moves[i]*speed
            segment=seg_list[i]
            segment.move_ip(move.x,move.y)

            if segment.left<0:
                segment.left=0
            if segment.top<0:
                segment.top=0
            if segment.bottom>=HEIGHT:
                segment.bottom=HEIGHT-1
            if segment.right>=WIDTH:
                segment.right=WIDTH-1    

def draw_snake():
    # draw the segments
    for i in range(len(seg_list)-1, -1, -1):
        # pygame.draw.rect(screen, colors[i], player[i])
        pygame.draw.circle(screen,colors[i],seg_list[i].center,seg_list[i].width/2)

    # draw the face
    face_center = pygame.math.Vector2(seg_list[0].center)
    pygame.draw.circle(screen,'cyan4', face_center+pygame.math.Vector2(12,-12),5)
    pygame.draw.circle(screen,'cyan4', face_center+pygame.math.Vector2(-12,-12),5)
    pygame.draw.arc(screen,'cyan4',seg_list[0].scale_by(0.65),225*(3.14/180),315*(3.14/180),width=2)

# FOOD STUFF

food=[]
food_size=10 # radius of the circle

def spawn_food():
    x=random.randint(0,WIDTH-1)
    y=random.randint(0,HEIGHT-1)
    food.append(pygame.math.Vector2(x,y))

def draw_food():
    for center in food:
        pygame.draw.circle(screen, "mistyrose2", center, food_size)


spawn_food()

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # UPDATE THE GAME

    update_snake()

    # DRAW THE GAME

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("skyblue")

    draw_snake()
    draw_food()


    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()