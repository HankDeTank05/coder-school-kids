import pygame
import common as c
import bullet as b
import time_manager as tm

class Player:

    #constructor
    def __init__(self, color, speed, bullet_man, time_man):
        self._pos = pygame.math.Vector2(5, 720/2) #starting pos
        self._color = color
        self.speed = speed
        self.dir = pygame.math.Vector2(1,0) #starting dir
        self.current_m1_state = False
        self.current_m2_state = False
        self.prev_m1_state = False
        self.prev_m2_state = False
        self.current_space_state = False
        self.prev_space_state = False
        self._health = c.PLAYER_BASE_HEALTH
        self.bullet_man = bullet_man # player HAS ACCESS to bullet manager. it DOES NOT OWN it
        self.time_man = time_man
        self.max_slomo_time = 10.6
        self.slomo_time = self.max_slomo_time

        #constants
        self.SIZE = 50
        self.BOUNDS_MIN_X = 0 + self.SIZE
        self.BOUNDS_MAX_X = c.SCREEN_WIDTH - self.SIZE
        self.BOUNDS_MIN_Y = 0 + self.SIZE
        self.BOUNDS_MAX_Y = c.SCREEN_HEIGHT - self.SIZE
        
    def update(self, dt):

        pos_delta=pygame.math.Vector2(0,0)
        #player_facing = pygame.math.Vector2(0,0)
        
        ##############
        # READ INPUT #
        ##############

        keys=pygame.key.get_pressed()
        # TODO: come back and figure out a way to prevent diagonal-movement key releases from reading as straightine directions sometimes
        if keys[pygame.K_w]:
            #move up
            pos_delta.y -= self.speed
        if keys[pygame.K_a]:
            #move left
            pos_delta.x -= self.speed
        if keys[pygame.K_s]:
            #move down
            pos_delta.y += self.speed
        if keys[pygame.K_d]:
            #move right
            pos_delta.x += self.speed
        if keys[pygame.K_SPACE]:
            # determine state for space bar
            self.current_space_state = True
        else :
            self.current_space_state = False

        mouse_buttons = pygame.mouse.get_pressed()
        # detemine state for both mouse buttons
        self.current_m1_state = mouse_buttons[0]
        self.current_m2_state = mouse_buttons[1]
        # TODO: come back and move the following lines of code if there are problems with aiming direction

        #################
        # PROCESS INPUT #
        #################

        #shoot
        if self.prev_m1_state == False and self.current_m1_state == True:
            self.bullet_man.add_bullet(self._pos, self.dir)
            #bullet.bullet_create(self.pos, self.dir)

        #toggle slowmo
        if self.prev_space_state == False and self.current_space_state == True:
            if self.time_man.get_timescale() == 1:
                self.time_man.set_timescale(0.01)
            elif self.time_man.get_timescale() < 1:
                self.time_man.set_timescale(1)
        
        # fix diagonal movement so it isn't faster than straightline speed
        if pos_delta.x != 0 and pos_delta.y != 0:
            pos_delta.normalize_ip()
            pos_delta *= self.speed

        pos_delta *= dt
        self._pos += pos_delta #move player
        # player_pos = player_pos + pos_delta

        ###############################################
        # prevents the player from walking off screen #
        ###############################################

        if self._pos.x < self.BOUNDS_MIN_X: #if player is left of min x
            #move player right until the player is not out of bounds 
            self._pos.x = self.BOUNDS_MIN_X
        elif self._pos.x > self.BOUNDS_MAX_X:#if player is right of max.x
            #move player left
            self._pos.x = self.BOUNDS_MAX_X

        if self._pos.y < self.BOUNDS_MIN_Y: #if player is above of min y
            #move player down
            self._pos.y = self.BOUNDS_MIN_Y
        elif self._pos.y > self.BOUNDS_MAX_Y: # if player is under of max y
            #move player up
            self._pos.y = self.BOUNDS_MAX_Y

        # caluculate facing direction
        if not pygame.mouse.get_pos() == self._pos:
            self.dir = pygame.mouse.get_pos() - self._pos
            self.dir.normalize_ip()

        ##################################
        # set prev states for next frame #
        ##################################
        
        self.prev_m1_state = self.current_m1_state
        self.prev_m2_state = self.current_m2_state
        self.prev_space_state = self.current_space_state

    def draw(self):
        pygame.draw.circle(c.screen, self._color, self._pos, self.SIZE) # draw player
        #get rid of the line under me (eventually)
        pygame.draw.line(c.screen, c.RED, self._pos, self._pos + self.dir * self.SIZE) # draw aim line

'''
player_speed=500

player_pos = pygame.math.Vector2(5,720/2)
player_facing = pygame.math.Vector2(1,0)
SIZE = 50

BOUNDS_MIN_X = 0 + SIZE
BOUNDS_MAX_X = c.SCREEN_WIDTH - SIZE
BOUNDS_MIN_Y = 0 + SIZE
BOUNDS_MAX_Y = c.SCREEN_HEIGHT - SIZE

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

    # prevents the player from walking off screen
    if player_pos.x < BOUNDS_MIN_X: #if player is left of min x
        #move player right until the player is not out of bounds 
        player_pos.x = BOUNDS_MIN_X
    elif player_pos.x > BOUNDS_MAX_X:#if player is right of max.x
        #move player left
        player_pos.x = BOUNDS_MAX_X

    if player_pos.y < BOUNDS_MIN_Y: #if player is above of min y
        #move player down
        player_pos.y = BOUNDS_MIN_Y
    elif player_pos.y > BOUNDS_MAX_Y: # if player is under of max y
        #move player up
        player_pos.y = BOUNDS_MAX_Y

    # caluculate facing direction
    player_facing = pygame.mouse.get_pos() - player_pos
    player_facing.normalize_ip()

    # set prev states for next frame
    prev_m1_state = current_m1_state
    prev_m2_state = current_m2_state

def player_draw():
    pygame.draw.circle(c.screen, c.GREEN, player_pos, SIZE)
    pygame.draw.line(c.screen, c.RED, player_pos, player_pos + player_facing * SIZE)
'''