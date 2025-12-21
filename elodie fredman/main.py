# language imports (stuff built into python)
import math
import random
import time
import os.path

# library imports (not built in stuff, but not my code)
import pygame
import pygame_textinput

# project imports (my code)
# none yet

#############
# CONSTANTS #
#############
WIDTH = 1700
HEIGHT = 950
MAX_RADIUS = None
if WIDTH > HEIGHT:
    MAX_RADIUS = HEIGHT / 2
else:
    MAX_RADIUS = WIDTH / 2
COLOR_RED = pygame.Color(255,0,0)
COLOR_GREEN = pygame.Color(0,255,0)
COLOR_BLUE = pygame.Color(0,50,205)
COLOR_YELLOW = pygame.Color(255,255,0)
COLOR_ORANGE = pygame.Color(255,110,0)
COLOR_BLACK = pygame.Color(0,0,0)
WIN_SCREEN_TIME = 5000

#######################
# GAME MATH FUNCTIONS #
#######################

def circle_overlap(x1, y1, r1, x2, y2, r2) -> bool:
    distance: float = math.hypot(x1 - x2, y1 - y2)
    overlap: bool = distance < r1 + r2
    return overlap

####################
# PLAYER FUNCTIONS #
####################

class Player:

    # constructor
    def __init__(self, player_color):
        self.x = 78
        self.y = 295
        self.color = player_color
        self.radius = 50
        self.speed = 500

    def update(self, frame_time):
        # Establishing the movement of the player
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.y -= self.speed * frame_time
        if keys[pygame.K_DOWN]:
            self.y += self.speed * frame_time
        if keys[pygame.K_RIGHT]:
            self.x += self.speed * frame_time
        if keys[pygame.K_LEFT]:
            self.x -= self.speed * frame_time

        # Keep player on screen
        self.x = max(self.radius, min(WIDTH - self.radius, self.x))
        self.y = max(self.radius, min(HEIGHT - self.radius, self.y))

    def draw(self):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)


##################
# FOOD FUNCTIONS #
##################

class Food:
    
    # constructor
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.color = color
        self.radius = radius

    def update(self, frame_time):
        pass
   
    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
    

#############################
# FOOD MANAGEMENT FUNCTIONS #
#############################

class FoodManager:

    def __init__(self):
        self.game_over = False
        self.foods = [
            Food(78,45,12,(45,27,255)),
            Food(250, 250,  20, (255, 225, 255)),
            Food(380, 129,  42, (0, 255, 0)),
            Food(703, 159,  89, (225, 171, 22)),
            Food(684, 547, 109, COLOR_BLACK),
        ]

    def update(self, frame_time, _player: Player):
        for food in self.foods:
            food.update(frame_time)

        # Draw food and check collisions
        for food in self.foods:
            #  Checks if cirlces overlap                                     If player circle is larger than food circle
            #  vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv     vvvvvvvvvvvvvvvvvvvv
            if circle_overlap(_player.x, _player.y, _player.radius, food.x, food.y, food.radius):
                if _player.radius >= food.radius:
                    eat_sound.play()
                    _player.radius += int(food.radius * 0.25)
                    self.foods.remove(food)
                    self.create_new()
                elif _player.radius < food.radius:
                    self.game_over = True

    def draw(self):
        for food in self.foods:
            food.draw()

    def create_new(self):
        while True:
            # STEP 0: generate new food
            new_radius = random.randint(10, 80)
            new_x = random.randint(new_radius, WIDTH - new_radius)
            new_y = random.randint(new_radius, HEIGHT - new_radius)
            new_color = (
                random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255)
            )
            overlap = False
            # STEP 1. check if the newly created food overlaps with ANY existing food
            for index in range(len(self.foods)):
                food = self.foods[index]
                overlap = circle_overlap(x1=food.x, y1=food.y, r1=food.radius, x2=new_x, y2=new_y, r2=new_radius)
                if overlap == True:
                    break
            
            # 1a. if it does, re-run the WHILE loop
            if overlap == True:
                continue

            # 1b. if it does not, exit the loop
            elif overlap == False:
                break
        new_food = Food(new_x, new_y, new_radius, new_color)
        self.foods.append(new_food)


##################
# GAME FUNCTIONS #
##################

def start():
    global game_state, menu_start_time, boxes, box_colors
    global player, food_man
    ################
    # Player Setup #
    ################
    player = Player()
    # box list
    box_width = 100
    box_height = 100
    boxes = [
        # pygame.Rect(WIDTH /2 - box_width /2, HEIGHT/2 - box_height/2, box_width, box_height), #red rect
        pygame.Rect(0, 0, box_width, box_height), #red rect
        pygame.Rect(0, 0, box_width,box_height), #green rect
        pygame.Rect(0, 0, box_width,box_height), #blue rect
        pygame.Rect(0,0, box_width, box_height), #yellow rect
        pygame.Rect(0,0, box_width, box_height) # orange rect
    ]
    box_colors = [
        COLOR_RED,
        COLOR_GREEN,
        COLOR_BLUE,
        COLOR_YELLOW,
        COLOR_ORANGE
    ]
    c = math.floor(len(boxes)/2)
    print(f"c = {c}")
    for box_index in range(len(boxes)):
        change_from_center = box_index - c
        print(f"change from center = {change_from_center}")
        boxes[box_index].center = pygame.math.Vector2(WIDTH/2 + change_from_center*box_width,HEIGHT/2)
    food_man = FoodManager()
    # Game State
    game_state = "menu"
    menu_start_time = pygame.time.get_ticks()  # Get start time of menu

# Initialize Pygame and Mixer
pygame.init()
pygame.mixer.init()

# Screen Setup

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Agario Clone')
clock = pygame.time.Clock()
running = True

# Load Sounds
eat_sound = pygame.mixer.Sound(os.path.join("elodie fredman", "eat.mp3"))
pygame.mixer.music.load(os.path.join("elodie fredman", "backgroundMusic.mp3"))
pygame.mixer.music.play(-1)

# Fonts
font = pygame.font.SysFont(None, 72)
small_font = pygame.font.SysFont(None, 48)

win_timer = -1

#start()

class Leaderboard:

    FILE_NAME = 'scores.txt'

    def __init__(self):
        self.scores = {}
        self.read_data()
        
    def write_data(self):
        with open(Leaderboard.FILE_NAME, 'w') as score_file:
            for (username,score) in zip(self.scores.keys(), self.scores.values()):
                score_file.write(f'{username},{score}\n')

    def read_data(self):
        with open(Leaderboard.FILE_NAME, 'r') as score_file:
            for line in score_file:
                #text_line = score_file.readline()
                values = line.split(sep=',')
                username = values[0]
                score = float(values[1])
                self.scores[username]=score

    def add_score(self, new_score_number, player_username):
        if player_username not in self.scores.keys() or self.scores[player_username] > new_score_number:
            self.scores[player_username] = new_score_number
            self.write_data()

    def draw(self):
        row = 0
        PADDING = 150
        SPACING = 50
        sorted_scores = sorted(self.scores.items(), key=lambda keyValue: (keyValue[1], keyValue[0]))
        for index in range(5):
            entry = sorted_scores[index]
            username = entry[0]
            score = entry[1]
            username_text = font.render(f'{index+1}. {username}', False, (0,0,0))
            username_text_rect = username_text.get_rect()
            username_text_rect.right = WIDTH / 2 - PADDING
            username_text_rect.top = row * SPACING
            screen.blit(username_text, username_text_rect)
            score_text = font.render(f'{round(score)} seconds to beat the game.', False, (0,0,0))
            score_text_rect = score_text.get_rect()
            score_text_rect.left = WIDTH / 2 + PADDING
            score_text_rect.top = row * SPACING
            screen.blit(score_text, score_text_rect)
            row += 1

class GameState:
    
    def __init__(self):
        pass

class MenuState(GameState):

    def __init__(self):
        box_width = 100
        box_height = 100
        self.boxes = [
            # pygame.Rect(WIDTH /2 - box_width /2, HEIGHT/2 - box_height/2, box_width, box_height), #red rect
            pygame.Rect(0, 0, box_width, box_height), #red rect
            pygame.Rect(0, 0, box_width,box_height), #green rect
            pygame.Rect(0, 0, box_width,box_height), #blue rect
            pygame.Rect(0,0, box_width, box_height), #yellow rect
            pygame.Rect(0,0, box_width, box_height) # orange rect
        ]
        self.box_colors = [
            COLOR_RED,
            COLOR_GREEN,
            COLOR_BLUE,
            COLOR_YELLOW,
            COLOR_ORANGE
        ]
        c = math.floor(len(self.boxes)/2)
        print(f"c = {c}")
        for box_index in range(len(self.boxes)):
            change_from_center = box_index - c
            print(f"change from center = {change_from_center}")
            self.boxes[box_index].center = pygame.math.Vector2(WIDTH/2 + change_from_center*box_width,HEIGHT/2)

        self.box_clicked = False
        self.clicked_color = None
    
    def update(self, frame_time):
        for box_index in range(len(self.boxes)):
            box = self.boxes[box_index]
            box_color = self.box_colors[box_index]

            # what are the two conditions that tell us if the player has clicked the color box or not?
            # 1. does the player's mouse hover over the box?
            # 2. did the player click the box when the mouse was in the box?
            mouse_pos = pygame.mouse.get_pos()
            mouse_state = pygame.mouse.get_pressed()
            if box.collidepoint(mouse_pos) and mouse_state[0] == True:
                self.box_clicked = True
                self.clicked_color = box_color

    def draw(self):
        # these lines make the title 'Glitchy Ripoff Agario' appear on the screen
        title_text = font.render("Glitchy Ripoff Agario", False, COLOR_BLACK)
        screen.blit(title_text, ((WIDTH - title_text.get_width()) // 2, HEIGHT // 3))

        #these next lines go one by one to draw each of the boxes
        for box_index in range(len(self.boxes)):
            box = self.boxes[box_index]
            box_color = self.box_colors[box_index]
            pygame.draw.rect(screen, box_color, box)

    def get_next_state(self) -> GameState:
        if self.box_clicked == True:
            return PlayingState(self.clicked_color)
        else:
            return self

class PlayingState(GameState):

    def __init__(self, player_color):
        self.player = Player(player_color)
        self.food_man = FoodManager()
        self.score = 0
    
    def update(self, frame_time):
        self.player.update(frame_time=frame_time)
        self.food_man.update(frame_time=frame_time, _player=self.player)
        self.score += frame_time

    def draw(self):
        self.player.draw()
        self.food_man.draw()

    def get_next_state(self) -> GameState:
        # if the player wins...
        if self.player.radius >= MAX_RADIUS:
            # return a WinningState object
            return NameState(new_score=self.score)
        # elif the player loses...
        if  self.food_man.game_over == True:
            # return a MenuState object
            return MenuState()
        else:
            return self

class NameState(GameState):

    def __init__(self, new_score):
        self.text_input = pygame_textinput.TextInputVisualizer(font_object=font)
        self.username = None
        self.score = new_score
        self.rendered_text = None
        self.rendered_text_rect = None

    def update(self, frame_time):
        self.text_input.update(events)
        screen.blit(self.text_input.surface, (600, 0))
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                self.username = self.text_input.value
        self.rendered_text = font.render("What is your username?\nPlease don't use a comma!", True, (0,0,0))
        self.rendered_text_rect = self.rendered_text.get_rect()
        self.rendered_text_rect.topleft = (0,0)

    def draw(self):
        screen.blit(self.rendered_text, self.rendered_text_rect)

    def get_next_state(self):
        if self.username is None:
            return self
        else:
            return WinningState(self.score, self.username)

class WinningState(GameState):

    def __init__(self, new_score, new_username):
        self.win_text = font.render("You Win! Click on the blue box to start another game!", False, COLOR_BLACK)
        self.restart_win_menu_checker_thing_time = pygame.time.get_ticks() + WIN_SCREEN_TIME
        self.leaderboard = Leaderboard()
        self.leaderboard.add_score(new_score, new_username)
        self.button_rect = pygame.Rect(200, 127, 130, 119)
        self.box_clicked = False
        self.your_score = new_score
    
    def update(self, frame_time):
        mouse_pos = pygame.mouse.get_pos()
        mouse_state = pygame.mouse.get_pressed()
        if self.button_rect.collidepoint(mouse_pos) and mouse_state[0] == True:
            self.box_clicked = True

    def draw(self):
        screen.fill(COLOR_YELLOW)
        screen.blit(self.win_text, ((WIDTH - self.win_text.get_width()) // 2, HEIGHT // 3))
        your_score_text = font.render(f'"Your score is {round(self.your_score)}. "', False, COLOR_BLACK)
        your_score_text_rect = your_score_text.get_rect()
        your_score_text_rect.center = (WIDTH / 2, HEIGHT / 2)
        screen.blit(your_score_text, your_score_text_rect)
        self.leaderboard.draw()
        pygame.draw.rect(screen, COLOR_BLUE, self.button_rect)

    def get_next_state(self) -> GameState:
        if self.box_clicked == True:
            return MenuState()
        return self


current_state = MenuState()

#############
# Game Loop #
#############

while running:
    frame_time = clock.tick(60) / 1000  # 60 FPS
    screen.fill((89, 134, 203))  # Background color
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    ### PART 1: UPDATE ###
    current_state.update(frame_time)

    ### PART 2: DRAW ###
    current_state.draw()

    ### PART 3: PREP FOR NEXT FRAME ###
    current_state = current_state.get_next_state()
    
    """
    if win_timer != -1:
        if pygame.time.get_ticks() >= win_timer:
            start()

    # Auto switch from menu to playing after 3 seconds (3000 ms)

    ####################
    # GAME STATE: MENU #
    ####################
    if game_state == "menu":
        elapsed_time = pygame.time.get_ticks() - menu_start_time

        #if game_state == "menu":
        title_text = font.render("Glitchy Ripoff Agario", True , (0, 0, 0))
        #prompt_text = small_font.render("Get Ready...3...2...1!", True, (0, 0, 0))
        screen.blit(title_text, ((WIDTH - title_text.get_width()) // 2, HEIGHT // 3))
        #screen.blit(prompt_text, ((WIDTH - prompt_text.get_width()) // 2, HEIGHT // 2))

        mouse_pos = pygame.mouse.get_pos()
        mouse_state = pygame.mouse.get_pressed()
        for box_index in range(len(boxes)):
            box = boxes[box_index]
            box_color = box_colors[box_index]
            pygame.draw.rect(screen, box_color, box)

            # what are the two conditions that tell us if the player has clicked the color box or not?
            # 1. does the player's mouse hover over the box?
            # 2. did the player click the box when the mouse was in the box?

            if box.collidepoint(mouse_pos) and mouse_state[0] == True:
                circle_color = box_color
                game_state = "playing"



    #######################
    # GAME STATE: PLAYING #
    #######################
    elif game_state == "playing":
        ########################
        # step 1: update stuff #
        ########################

        player.update(frame_time=frame_time)
        food_man.update(frame_time=frame_time, _player = player)

        ######################
        # step 2: draw stuff #
        ######################

        player.draw()
        food_man.draw()

        ###################
        # step 3: winning #
        ###################
   
        if player.radius >= MAX_RADIUS:
            game_state = "winning"
            win_timer = pygame.time.get_ticks() + 3000




    #######################
    # GAME STATE: WINNING #
    #######################
    elif game_state == "winning":
        screen.fill(COLOR_YELLOW)
        win_text = font.render("You Win! Another game will begin shortly!", True, (0, 0, 0))
        screen.blit(win_text, ((WIDTH - win_text.get_width()) // 2, HEIGHT // 3))
    """
   
    pygame.display.flip()

pygame.quit()