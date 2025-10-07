# language imports (these are built in to python)
import random
import copy

# library imports (this is stuff that's not ours, but not built in to python)
import pygame

# project imports (this is our stuff we created)


pygame.init()
pygame.font.init()

##################
# GAME CONSTANTS #
##################

# screen constants
WIDTH = 500
HEIGHT = 600
FPS = 60
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodge the Obstacle")

# COLORS
WHITE = (255, 255, 255)
RED = (200, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
GREEN = (0, 240, 225)
YELLOW = (255, 255, 0)
ORANGE = (255, 100, 0)

# player stuff
PLAYER_MAX_HEALTH = 700

# obstacle stuff
OBS_FAST_CHANCE = 8
OBSTACLE_DMG_SMALL = 75
OBSTACLE_DMG_NORMAL = 100
OBSTACLE_DMG_BIG = 150
OBSTACLE_WIDTH = 20
OBSTACLE_HEIGHT = 30
OBSTACLE_SPEED_SMALL = 650
OBSTACLE_SPEED_NORMAL = 500
OBSTACLE_SPEED_BIG = 400
OBSTACLE_SPAWN_DELAY = 0.5
OBSTACLE_SIZE_SMALL = "small"
OBSTACLE_SIZE_NORMAL = "normal"
OBSTACLE_SIZE_BIG = "big"
OBSTACLE_SMALL_WIDTH = 14
OBSTACLE_SMALL_HEIGHT = 20
OBSTACLE_NORMAL_WIDTH = 20
OBSTACLE_NORMAL_HEIGHT = 30
OBSTACLE_BIG_WIDTH = 30
OBSTACLE_BIG_HEIGHT = 40
OBSTACLE_SPAWN_CHANCE = [
    OBSTACLE_SIZE_SMALL,
    OBSTACLE_SIZE_SMALL,
    OBSTACLE_SIZE_SMALL,
    OBSTACLE_SIZE_NORMAL,
    OBSTACLE_SIZE_NORMAL, 
    OBSTACLE_SIZE_NORMAL, 
    OBSTACLE_SIZE_NORMAL, 
    OBSTACLE_SIZE_NORMAL, 
    OBSTACLE_SIZE_NORMAL, 
    OBSTACLE_SIZE_NORMAL, 
    OBSTACLE_SIZE_NORMAL, 
    OBSTACLE_SIZE_NORMAL, 
    OBSTACLE_SIZE_NORMAL, 
    OBSTACLE_SIZE_NORMAL, 
    OBSTACLE_SIZE_NORMAL, 
    OBSTACLE_SIZE_NORMAL, 
    OBSTACLE_SIZE_NORMAL, 
    OBSTACLE_SIZE_BIG, 
    OBSTACLE_SIZE_BIG,
    OBSTACLE_SIZE_BIG
]

# HUD stuff
HEALTH_BAR_WIDTH = WIDTH
HEALTH_BAR_HEIGHT = 10

################
# GAME CLASSES #
################

class Obstacle:

    # constructor
    def __init__(self):
        self._rect: pygame.Rect = None
        self._speed = None
        self._dmg = None
        self._is_fast = random.randint(1, 100) < OBS_FAST_CHANCE
        # assert(self._rect != None) # if you got an error on this line the variable size_name doesn't have a value of "small", "normal", or "big"


    # game functions

    def update(self, frame_time):
        self._rect.move_ip(0, self._speed * frame_time)

    def draw(self):
        pygame.draw.rect(SCREEN, RED, self._rect)

    # accessors

    def get_rect(self) -> pygame.Rect:
        return self._rect

    def get_dmg(self) -> int:
        return self._dmg

    # mutators

    def _set_start_pos(self):
        x = random.randint(0, WIDTH - self._rect.width)
        y = -self._rect.height
        self._rect.update(x, y, self._rect.width, self._rect.height)

class SmallObstacle(Obstacle):

    def __init__(self):
        super().__init__()
        self._rect = pygame.Rect(0, 0, OBSTACLE_SMALL_WIDTH, OBSTACLE_SMALL_HEIGHT)
        self._speed = OBSTACLE_SPEED_SMALL
        self._dmg = OBSTACLE_DMG_SMALL
        self._set_start_pos()

class NormalObstacle(Obstacle):
    
    def __init__(self):
        super().__init__()
        self._rect = pygame.Rect(0, 0, OBSTACLE_NORMAL_WIDTH, OBSTACLE_NORMAL_HEIGHT)
        self._speed = OBSTACLE_SPEED_NORMAL
        self._dmg = OBSTACLE_DMG_NORMAL
        self._set_start_pos()

class BigObstacle(Obstacle):
    
    def __init__(self):
        super().__init__()
        self._rect = pygame.Rect(0, 0, OBSTACLE_BIG_WIDTH, OBSTACLE_BIG_HEIGHT)
        self._speed = OBSTACLE_SPEED_BIG
        self._dmg = OBSTACLE_DMG_BIG
        self._set_start_pos()

class ObstacleManager:

    # constructor
    def __init__(self):
        self._obses: list[Obstacle] = []
        self._spawn_timer = 0

    # game functions

    # update all the obstacles
    def update(self, frame_time):
        self._spawn_timer += frame_time
        if self._spawn_timer >= OBSTACLE_SPAWN_DELAY:
            self._spawn_timer -= OBSTACLE_SPAWN_DELAY
            size_name = random.choice(OBSTACLE_SPAWN_CHANCE)
            if size_name == OBSTACLE_SIZE_SMALL:
                new_obs = SmallObstacle()
            elif size_name == OBSTACLE_SIZE_NORMAL:
                new_obs = NormalObstacle()
            elif size_name == OBSTACLE_SIZE_BIG:
                new_obs = BigObstacle()
            else:
                assert(False) # crashes the game if size_name doesn't have a value listed above
                # (is there a problem with OBSTACLE_SPAWN_CHANCE or the if/elif sequence above?)
            self._obses.append(new_obs)
        for obs in self._obses:
            obs.update(frame_time)

    # draw all the obstacles
    def draw(self):
        for obs in self._obses:
            obs.draw()

    # accessors

    def get_obses(self) -> list[Obstacle]:
        return copy.deepcopy(self._obses)
    
    # mutators

    def remove_obses(self, obses_indices: list[int]):
        obses_indices.sort(reverse=True)
        for obs_index in obses_indices:
            self._obses.pop(obs_index)

class Player:

    # constructor
    def __init__(self):
        size = pygame.math.Vector2(50, 50)
        pos = pygame.math.Vector2(WIDTH // 2 - size.x // 2,
                                       HEIGHT - size.y - 10)
        self._speed: int | float = 350
        self._rect: pygame.Rect = pygame.Rect(pos, size)
        self._max_hp = PLAYER_MAX_HEALTH
        self._hp = self._max_hp

    # Game functions

    def update(self, frame_time):

        ###################
        # move the player #
        ###################

        keys = pygame.key.get_pressed()
        move_x = 0
        move_y = 0
        if keys[pygame.K_UP]:
            move_y -= 1
        if keys[pygame.K_DOWN]:
            move_y += 1
        if keys[pygame.K_LEFT]:
            move_x -= 1
        if keys[pygame.K_RIGHT]:
            move_x += 1
        player_move = pygame.math.Vector2(move_x, move_y)
        # correct diagonal movement
        if player_move.length() > 0:
            player_move = player_move.normalize() * self._speed * frame_time

        # move the rectangle
        self._rect.move_ip(player_move)

        ##############################
        # Keeps player in the screen #
        ##############################
        right_bound = WIDTH - 1
        bottom_bound = HEIGHT - HEALTH_BAR_HEIGHT

        # If player is partialy or totaly off screen on the left
        if self._rect.left < 0:
            self._rect.left = 0

        # If player is partialy or totaly off screen on the right
        elif self._rect.right > right_bound:
            self._rect.right = right_bound

        # If player is partialy or totaly off screen on the bottom
        if self._rect.bottom > bottom_bound:
            self._rect.bottom = bottom_bound

    def draw(self):
        pygame.draw.rect(SCREEN, BLUE, self._rect)

    # accessors

    def get_pos(self) -> pygame.math.Vector2:
        return pygame.math.Vector2(self._rect.topleft)
    
    def get_hp(self) -> int:
        return self._hp

    def get_rect(self) -> pygame.Rect:
        return self._rect

    # mutators

    def set_pos(self, new_pos: pygame.math.Vector2):
        self._rect.update(new_pos, self._rect.size)

    def set_x(self, new_x: int | float):
        self.set_pos(pygame.math.Vector2(new_x, self._rect.y))

    def set_y(self, new_y: int | float):
        self.set_pos(pygame.math.Vector2(self._rect.x, new_y))

    def set_speed(self, new_speed: int | float):
        self._speed = new_speed

    def change_speed(self, speed_change: int | float):
        self._speed += speed_change

    def take_damage(self, damage: int):
        self._hp -= damage

class Hud:

    # constructor
    def __init__(self):
        self._max_health_bar_width = HEALTH_BAR_WIDTH
        self._health_pcent = 1

    # game functions

    def update(self, frame_time):
        self._health_pcent = player.get_hp() / PLAYER_MAX_HEALTH

    def draw(self):
        # draw the background rectangle
        bg_rect = pygame.Rect((0, 0), (HEALTH_BAR_WIDTH, HEALTH_BAR_HEIGHT))
        bg_rect.midbottom = pygame.math.Vector2(WIDTH/2, HEIGHT-1)
        pygame.draw.rect(SCREEN, BLACK, bg_rect)
        # draw the current health rectangle
        hp_rect = pygame.Rect(bg_rect.topleft, (self._health_pcent * HEALTH_BAR_WIDTH, HEALTH_BAR_HEIGHT))
        pygame.draw.rect(SCREEN, RED, hp_rect)

font = pygame.font.SysFont(None, 48)

clock = pygame.time.Clock()

# Create player variables
player = Player()

# obstacle manager
obs_man = ObstacleManager()

# create the hud
hud = Hud()

frame_time = 0
running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    SCREEN.fill(WHITE)

    ##################
    # PART 1: UPDATE #
    ##################

    player.update(frame_time)
    obs_man.update(frame_time)
    hud.update(frame_time)

    # do collision
    collided_indices = []
    obses_list = obs_man.get_obses()
    for obs_index in range(len(obses_list)):
        obstacle = obses_list[obs_index]
        player_rect = player.get_rect()
        obs_rect = obstacle.get_rect()
        if player_rect.colliderect(obs_rect):
            player.take_damage(obstacle.get_dmg())
            collided_indices.append(obs_index)
    obs_man.remove_obses(collided_indices)

    ################
    # PART 2: DRAW #
    ################

    player.draw()
    obs_man.draw()
    hud.draw()

    # flip() the display to put your work on screen
    pygame.display.flip()

    frame_time = clock.tick(FPS) / 1000  # limits FPS to 60

pygame.quit()