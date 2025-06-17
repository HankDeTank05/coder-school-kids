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
LIGHT_PURPLE = pygame.math.Vector3(177, 156, 217)
LIGHT_PURPLE_D = LIGHT_PURPLE * 0.9
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
        self.walk_speed = 500
        self.fast_goose = 1000

    # update the goose
    def update(self, _keys, _dt):
        # TODO make it a fast goose when shift key is pressed
        pos_delta = pygame.math.Vector2(0,0)
        current_speed = self.walk_speed
        if _keys[pygame.K_RSHIFT]:
            current_speed = self.fast_goose
        if _keys[pygame.K_RIGHT]:
            pos_delta.x += current_speed
        if _keys[pygame.K_LEFT]:
            pos_delta.x -= current_speed
        if _keys[pygame.K_UP]:
            pos_delta.y -= current_speed
        if _keys[pygame.K_DOWN]:
            pos_delta.y += current_speed

        if pos_delta.magnitude() > 0:
            pos_delta.normalize_ip()
            pos_delta *= current_speed
        
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
        self.points = {
            "front bottom-left": pygame.math.Vector2(0,0),
            "front bottom-right": pygame.math.Vector2(0,0),
            "front top-left": pygame.math.Vector2(0,0),
            "front top-right": pygame.math.Vector2(0,0),
            "inside top-left": pygame.math.Vector2(0,0),
            "inside top-right": pygame.math.Vector2(0,0),
            "left flappy top-est": pygame.math.Vector2(0,0),
            "left flappy bottom left-ish": pygame.math.Vector2(0,0),
            "right flappy top-est": pygame.math.Vector2(0,0),
            "right flappy bottom right": pygame.math.Vector2(0,0) 
        } 

    def update(self):
        #calculate points for box front face
        box_width = 80
        box_height = 50
        self.points["front bottom-left"] = pygame.math.Vector2(self.pos.x - box_width / 2,
                                                               self.pos.y)
        self.points["front bottom-right"] = pygame.math.Vector2(self.pos.x + box_width / 2,
                                                                self.pos.y)
        self.points["front top-left"] = pygame.math.Vector2(self.pos.x - box_width / 2,
                                                            self.pos.y - box_height)
        self.points["front top-right"] = pygame.math.Vector2(self.pos.x + box_width / 2,
                                                             self.pos.y - box_height)
        
        # Below is inside points all the time
        inside_height = 30
        
        self.points["inside top-left"] = pygame.math.Vector2(self.pos.x - box_width / 2,
                                                             self.pos.y - box_height - inside_height)
        self.points["inside top-right"] = pygame.math.Vector2(self.pos.x + box_width / 2,
                                                              self.pos.y - box_height - inside_height)

        if self.has_goose == True:
            """
            this is how the box should look

            left flappy/right flappy
              |        /
              v       v
                
              /|____|\ 
             |/| in |\|
             |/______\|
             | front  |
             |________|
            """
            pass  #calculate points for closed box
        elif self.has_goose == False:
            """
            this is how the box should look

            left flappy     right flappy
            |              /
            v             v

            |\          /|
            | \________/ |
            \ | inside | /
             \|________|/
              |  front |
              |________|
            """
            height_offset = 25
            flap_width = 0.40 * box_width
            
            self.points["left flappy bottom left-ish"] = pygame.math.Vector2(self.pos.x - box_width / 2 - flap_width,
                                                                             self.pos.y - box_height - height_offset)
            self.points["left flappy top-est"] = pygame.math.Vector2(self.pos.x - box_width / 2 - flap_width,
                                                                     self.pos.y - box_height - height_offset - inside_height)
    def draw(self, _surface):
        # yhis code is drawing the box front
        pygame.draw.polygon(_surface, LIGHT_PURPLE, [
            self.points["front bottom-left"],
            self.points["front bottom-right"],
            self.points["front top-right"],
            self.points["front top-left"]
        ])

        # Yhis is the drawing of the inside
        pygame.draw.polygon(_surface, NAVY, [
            self.points["inside top-left"],
            self.points["front top-left"],
            self.points["front top-right"],
            self.points["inside top-right"]
        ])

        #yhis is the drawing of the left flappy
        pygame.draw.polygon(_surface, LIGHT_PURPLE_D, [
            self.points["left flappy top-est"],
            self.points["left flappy bottom left-ish"],
            #seft.pie = dog +- cat = rabbit
            self.points["front top-left"],
            self.points["inside top-left"]
        ])


        if self.has_goose == True:
            pass
        elif self.has_goose == False:
            # TODO: GET RID OF THESE vv THESE ARE DUPLICATE VARIABLES
            box_width = 80
            box_height = 50
            # Drawing the inside of the box
            inside_height = 30
            ##########################################################################################################################################
            # TODO: draw the left flappy with the new system yayyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy
            height_offset = 25
            flap_width = 0.40 * box_width
            # left_flappy_points = [pygame.math.Vector2(self.points["inside top-left"]), #yhis is the topright corner of the left flappy
            #                       pygame.math.Vector2(self.points["front top-left"])] #yhis is the bottom right corner of the left flappy
            #yhis is the bottom left corner of the left flappy
            # left_flappy_points.append(
            #     pygame.math.Vector2(
            #         left_flappy_points[1].x - flap_width,
            #         left_flappy_points[1].y - height_offset))
            #yhis is the topleft corner of the left flappy
            # left_flappy_points.append(
            #     pygame.math.Vector2(
            #         left_flappy_points[2].x,
            #         left_flappy_points[2].y - inside_height))
            # pygame.draw.polygon(_surface, LIGHT_PURPLE_D, left_flappy_points)
            
            right_flappy_points = [pygame.math.Vector2(self.points["inside top-right"]), # yhis is the topleft corner of the right flappy
                                   pygame.math.Vector2(self.points["front top-right"] )] #yhis is the bottomleft corner of ye right flappy
            #yhis is ye bottom right corner of ye right flappy
            right_flappy_points.append(
                pygame.math.Vector2(
                    right_flappy_points[1].x + flap_width,
                    right_flappy_points[1].y - height_offset))
            #yhis is the topright corner of ye right flappy
            right_flappy_points.append(
                pygame.math.Vector2(
                    right_flappy_points[2].x,
                    right_flappy_points[2].y - inside_height))
            pygame.draw.polygon(_surface, LIGHT_PURPLE_D, right_flappy_points)

quacK = Goose(150, 150)
box = Box(100, 150)

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
    box.update() 
    # draw stuff
    quacK.draw(screen)
    box.draw(screen)
    
    pygame.display.flip()

    dt = clock.tick(60)/1000
