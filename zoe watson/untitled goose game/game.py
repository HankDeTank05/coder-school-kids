#animal crossing DED leaf

import sys
import pygame
from pygame.locals import *

pygame.init()

WIDTH = 1280 
HEIGHT = 720

# create the surface we're going to draw on
screen = pygame.display.set_mode((WIDTH, HEIGHT))
dt = 0

# define some colors
# NOTE: if you want more, this website has a lot of colors to pick from: https://html-color.codes/
ORANGE = (255, 153, 51)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (128, 128, 128)
BROWN = (153, 76, 0)
GREEN = (141, 182, 0)
LIGHT_PURPLE = (177, 156, 217)
NAVY = (0, 33, 71)
GRASS_COLOR = (116,195,101)
# set the game to run at 60fps
clock = pygame.time.Clock()

class Goose:

    """
    abilities
    - honk
    - flap
    - duck (not the animal, the action)
    - grab/move
    - run/dash
    - peck
    - (other context-sensitive interactions)
    """

    # constructor function (creates a goose object)
    def __init__(self, _x, _y):
        self.pos = pygame.math.Vector2(_x, _y)
        self.speed = 1000

    # update the goose
    def update(self, _keys, _dt):
        pos_delta = pygame.math.Vector2(0,0)
        if _keys[pygame.K_RIGHT]:
            pos_delta.x += self.speed
        if _keys[pygame.K_LEFT]:
            pos_delta.x -= self.speed
        if _keys[pygame.K_UP]:
            pos_delta.y -= self.speed
        if _keys[pygame.K_DOWN]:
            pos_delta.y += self.speed

        if pos_delta.magnitude() > 0:
            pos_delta.normalize_ip()
            pos_delta *= self.speed
        
        pos_delta *= _dt
        self.pos += pos_delta

        #checks if you're off screen left
        if self.pos.x < 0:
            self.pos.x += WIDTH
        
        #checks if you're off screen right
        elif self.pos.x >= WIDTH: 
            self.pos.x -= WIDTH

        # TODO: come back next time and make the goose do vertical loop-around

        #checks if you're off the screen on the top 
        if self.pos.y < 0:
            self.pos.y += HEIGHT

        elif self.pos.y >= HEIGHT:
            self.pos.y -= HEIGHT

    # draw the goose
    def draw(self, _surface):
        body_color = GREY
        leg_color = BROWN
        beak_color = ORANGE
        eye_color = BLACK
        
        #below is the drawing of legs
        left_leg_end = self.pos + pygame.math.Vector2(0, -25)
        pygame.draw.line(_surface, leg_color, self.pos, left_leg_end)
        right_leg_start = self.pos + pygame.math.Vector2(15,0)
        right_leg_end = right_leg_start + pygame.math.Vector2(0,-35)
        pygame.draw.line(_surface, leg_color, right_leg_start, right_leg_end)

        #below is the drawing of the body
        body_center = left_leg_end + pygame.math.Vector2(0,-10)
        body_radius =  15
        pygame.draw.circle(_surface, body_color, body_center, body_radius)

        # flappy wings
        left_wing = pygame.Rect(body_center.x - 5, body_center.y - 35, 7, 25)
        pygame.draw.rect(_surface, body_color, left_wing)
        right_wing = pygame.Rect(body_center.x + 10, body_center.y - 10, 30, 7)
        pygame.draw.rect(_surface, body_color, right_wing)

        #below is the drawing of neck
        neck_start = body_center + pygame.math.Vector2(-7,-7)
        neck_end = neck_start + pygame.math.Vector2(-10,-30)
        pygame.draw.line(_surface, body_color, neck_start, neck_end)

        #head (circle) on top of neck
        head_radius = 10
        head_center = neck_end + pygame.math.Vector2(0,-head_radius)
        pygame.draw.circle(_surface, body_color, head_center, head_radius)

        # beak... quacK
        beak_width = 11
        rect_x = head_center.x - beak_width - 10
        rect_y = head_center.y 
        beak_height = 4
        beak_rect = pygame.Rect(rect_x, rect_y, beak_width, beak_height)
        pygame.draw.rect(_surface, beak_color, beak_rect)

        #eyes... *blink blink*
        eye_radius = 4
        r_eye_center = head_center + pygame.math.Vector2(0,-4)
        pygame.draw.circle(_surface, eye_color, r_eye_center, eye_radius)

class Object:

    def __init__(self, _x, _y):
        self.pos = pygame.math.Vector2(_x, _y)

class Box(Object):

    # constructor
    def __init__(self, _x, _y):
        super().__init__(_x, _y)
        self.has_goose = False

    def draw(self, _surface):
        """
        this is how the box should look
        |\          /|
        | \________/ |
        \ | inside | /
         \|________|/
          |        |
          |________|
        """
        box_width = 80
        box_height = 50
        box_front = pygame.Rect(self.pos.x - box_width/2, #box front X positiom
                                self.pos.y - box_height, #box front Y positiom
                                box_width, 
                                box_height)
        pygame.draw.rect(_surface, LIGHT_PURPLE, box_front)

        if self.has_goose == True:
            pass
        elif self.has_goose == False:
            # TODO: come back next time and finish drawing the rest of the (open) box
            inside_height = 30
            box_inside = pygame.Rect(self.pos.x - box_width/2,
                                     self.pos.y - box_height - inside_height, 
                                     box_width, 
                                     inside_height)
            pygame.draw.rect(_surface, NAVY, box_inside)

quacK = Goose(150, 150)
box = Box(100, 100)

# MAIN GAME LOOP
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(GRASS_COLOR)

    # update stuff
    keys = pygame.key.get_pressed()
    quacK.update(keys, dt)

    # draw stuff
    quacK.draw(screen)
    box.draw(screen)
    
    pygame.display.flip()

    dt = clock.tick(60)/1000
