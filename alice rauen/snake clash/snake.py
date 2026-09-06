import pygame
from common import *

# SNAKE STUFF
segments=22
seg_size = 48 # size of the square

speed=6
seg_list=[]
mouth_rect=None

moves=[]

colors=[]
head_color = SNAKE_HEAD_COLOR
tail_color = SNAKE_TAIL_COLOR
for i in range(segments):
    seg_list.append(pygame.Rect(0,0,seg_size,seg_size))
    moves.append(pygame.math.Vector2(0,0))
    colors.append(head_color.lerp(tail_color, i/segments))

def update_snake() -> None:
    # move the snake
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

        # check for collision with food    

def draw_snake() -> None:
    global mouth_rect
    # draw the segments
    for i in range(len(seg_list)-1, -1, -1):
        # pygame.draw.rect(screen, colors[i], player[i])
        pygame.draw.circle(screen, colors[i],seg_list[i].center,seg_list[i].width/2)

    # draw the face
    face_center = pygame.math.Vector2(seg_list[0].center)
    pygame.draw.circle(screen, SNAKE_FACE_COLOR, face_center+pygame.math.Vector2(12,-12),5)
    pygame.draw.circle(screen, SNAKE_FACE_COLOR, face_center+pygame.math.Vector2(-12,-12),5)
    mouth_rect=pygame.draw.arc(screen, SNAKE_FACE_COLOR, seg_list[0].scale_by(0.65),225*(3.14/180),315*(3.14/180),width=2)




class Segment:
    _pos: pygame.math.Vector2
    _color: pygame.Color

    def __init__(self, start_paws, color):
        self._pos=start_paws
        self._color=color

    def draw(self,screen,radius):
        pygame.draw.circle(screen,self._color,self._pos,radius)


class Snake:
    _speed: int
    _seg_size: int
    _seg_list: list

    def __init__(self):
        self._speed=6
        self._seg_size=30
        self._seg_list=[]
        for i in range(22):
            new_seg=Segment(pygame.math.Vector2(15, 15), head_color.lerp(tail_color, i/segments))
            self._seg_list.append(new_seg)

    def update(self):
        pass

    def draw (self,screen):
        # drawing the segments
        for i in range(len(self._seg_list)-1,-1,-1):
            seg=self._seg_list[i]
            seg.draw(screen,self._seg_size)

        # drawing the face that henry ruined
        face_center = self._seg_list[0]
        pygame.draw.circle(screen, SNAKE_FACE_COLOR, face_center+pygame.math.Vector2(12,-12),5)
        pygame.draw.circle(screen, SNAKE_FACE_COLOR, face_center+pygame.math.Vector2(-12,-12),5)
        # mouth_rect=pygame.draw.arc(screen, SNAKE_FACE_COLOR, seg_list[0].scale_by(0.65),225*(3.14/180),315*(3.14/180),width=2)