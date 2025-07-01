import pygame
import constants as const
import gamemath as gm
import copy

class Fighter:

    P1_SPAWN_POS=pygame.math.Vector2(427, 600)
    P2_SPAWN_POS=pygame.math.Vector2(853, 600)

    # constructor
    def __init__(self, color: str, control: int, screen):
        self.pos: pygame.math.Vector2 = pygame.math.Vector2(screen.get_width() / 2, screen.get_height() / 2)
        self.pos_delta = pygame.math.Vector2(0,0)
        self.radius=40
        self.color=color
        self.speed=50
        self.max_speed=300
        self.max_fall_speed=5000
        self.on_stage=False
        self.deceleration=0.75
        self.max_jumps=2
        self.jumps=self.max_jumps
        self.jump_strength=1500
        self.jump_held=False
        #do things differently depending on player 
        if control==1:
            self.strategy=ControlStrategy(pygame.K_w, pygame.K_a, pygame.K_d)
            self.spawn=Fighter.P1_SPAWN_POS
        elif control==2:
            self.strategy=ControlStrategy(pygame.K_UP, pygame.K_LEFT, pygame.K_RIGHT)
            self.spawn=Fighter.P2_SPAWN_POS

    def on_collision_stage(self, platform_height):
        self.on_stage=True
        self.pos.y=platform_height-self.radius #apperance of standing on top of platform
        self.jumps=self.max_jumps

    def respawn(self):
        self.pos=copy.deepcopy(self.spawn)

    def update(self, _dt):
        self.moving=False
        self.jumping=False
        
        #read for input
        self.strategy.ProcessInputs(self)

        #prevent player from moving too fast left/right
        self.pos_delta.x=gm.clamp(-self.max_speed, self.max_speed, self.pos_delta.x)
        #prevent player from moving too fast up/down
        self.pos_delta.y=gm.clamp(-self.max_fall_speed, self.max_fall_speed, self.pos_delta.y)

        #slow when not moving
        if not self.moving:
            self.pos_delta.x*=self.deceleration
        
        if self.on_stage==False:
            #apply gravity to player
            self.pos_delta.y+=const.GRAVITY
        elif self.on_stage and not self.jumping:
            self.pos_delta.y=0

        #movement
        self.pos+=self.pos_delta*_dt

        #prep for next frame
        self.on_stage=False
            

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.pos, self.radius)

class ControlStrategy:

    def __init__(self, up, left, right):
        self.up=up
        self.left=left
        self.right=right 

    def ProcessInputs(self, _fighter):
        keys=pygame.key.get_pressed()
        if keys[self.up] and not _fighter.jump_held and _fighter.jumps>0:
            _fighter.pos_delta.y=-_fighter.jump_strength
            _fighter.jumping=True
            _fighter.jumps-=1
            _fighter.jump_held=True
        elif not keys[self.up]:
            _fighter.jump_held=False
        if keys[self.left]:
            _fighter.pos_delta.x-=_fighter.speed
            _fighter.moving=True
        if keys[self.right]:
            _fighter.pos_delta.x+=_fighter.speed
            _fighter.moving=True
