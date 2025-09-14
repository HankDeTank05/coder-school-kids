# language imports (stuff built into python)
import math
import random

# library imports (not built in stuff, but not my code)
import pygame

# project imports (my code)
# none yet

#############
# CONSTANTS #
#############
WIDTH = 1580
HEIGHT = 900
COLOR_RED = pygame.Color(255,0,0)
COLOR_GREEN = pygame.Color(0,255,0)
COLOR_BLUE = pygame.Color(0,0,255)

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

def player_update(frame_time):
    global circle_x, circle_y
    # Establishing the movement of the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        circle_y -= speed * frame_time
    if keys[pygame.K_DOWN]:
        circle_y += speed * frame_time
    if keys[pygame.K_RIGHT]:
        circle_x += speed * frame_time
    if keys[pygame.K_LEFT]:
        circle_x -= speed * frame_time

    # Keep player on screen
    circle_x = max(circle_radius, min(WIDTH - circle_radius, circle_x))
    circle_y = max(circle_radius, min(HEIGHT - circle_radius, circle_y))

def player_draw():
    pygame.draw.circle(screen, circle_color, (int(circle_x), int(circle_y)), circle_radius)

##################
# FOOD FUNCTIONS #
##################

def food_update(food, frame_time):
    fx, fy, fr, color = food

def food_draw(food):
    fx, fy, fr, color = food
    pygame.draw.circle(screen, color, (int(fx), int(fy)), fr) # Puts food on screen / draws food

#############################
# FOOD MANAGEMENT FUNCTIONS #
#############################

def create_new_food():
    global foods
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
        for index in range(len(foods)):
            food = foods[index]
            fx = food[0]
            fy = food[1]
            fr = food[2]
            overlap = circle_overlap(x1=fx, y1=fy, r1=fr, x2=new_x, y2=new_y, r2=new_radius)
            if overlap == True:
                break
        
        # 1a. if it does, re-run the WHILE loop
        if overlap == True:
            continue

        # 1b. if it does not, exit the loop
        elif overlap == False:
            break
    foods.append([new_x, new_y, new_radius, new_color])

def food_update_all(frame_time):
    for food in foods:
        food_update(food=food, frame_time=frame_time)

def food_draw_all():
    for food in foods:
        food_draw(food=food)

##################
# GAME FUNCTIONS #
##################

def start():
    global circle_x, circle_y, circle_color, circle_radius, speed, foods, game_state, menu_start_time, boxes, box_colors
    ################
    # Player Setup #
    ################
    circle_x, circle_y = 78, 295
    circle_color = (245, 45, 67)
    circle_radius = 50
    speed = 500
    # box list
    box_width = 100
    box_height = 100
    boxes = [
        # pygame.Rect(WIDTH /2 - box_width /2, HEIGHT/2 - box_height/2, box_width, box_height), #red rect
        pygame.Rect(0, 0, box_width, box_height), #red rect
        pygame.Rect(0, 0, box_width,box_height),
        pygame.Rect(0, 0, box_width,box_height),
        pygame.Rect(0, 0, box_width, box_height)
    ]
    box_colors = [
        COLOR_RED,
        COLOR_GREEN,
        COLOR_BLUE,
        (255, 255, 0)
    ]
    c = math.floor(len(boxes)/2)
    print(f"c = {c}")
    for box_index in range(len(boxes)):
        change_from_center = box_index - c
        print(f"change from center = {change_from_center}")
        boxes[box_index].center = pygame.math.Vector2(WIDTH/2 + change_from_center*box_width,HEIGHT/2)
    # Food List
    foods = [
        [78, 45, 12, (45, 27, 232)],
        [250, 250, 20, (255, 225, 0)],
        [380, 129, 42, (0, 255, 0)],
        [703, 159, 89, (225, 171, 22)],
        [684, 547, 109, (0, 247, 255)],
    ]
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
eat_sound = pygame.mixer.Sound("eat.mp3")
pygame.mixer.music.load("backgroundMusic.mp3")
pygame.mixer.music.play(-1)

# Fonts
font = pygame.font.SysFont(None, 72)
small_font = pygame.font.SysFont(None, 48)

start()



#############
# Game Loop #
#############

while running:
    frame_time = clock.tick(60) / 1000  # 60 FPS
    screen.fill((89, 134, 203))  # Background color

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Auto switch from menu to playing after 3 seconds (3000 ms)
    if game_state == "menu":
        elapsed_time = pygame.time.get_ticks() - menu_start_time
        #if elapsed_time >= 3000:
            #game_state = "playing"

        #if game_state == "menu":
        title_text = font.render("Glitchy Ripoff Agario", True, (0, 0, 0))
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
                

    elif game_state == "playing":

        ########################
        # step 1: update stuff #
        ########################

        player_update(frame_time=frame_time)
        food_update_all(frame_time=frame_time)

        # Draw food and check collisions
        for food in foods:
            fx, fy, fr, box_color = food
            #  Checks if cirlces overlap                                     If player circle is larger than food circle
            #  vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv     vvvvvvvvvvvvvvvvvvvv
            if circle_overlap(circle_x, circle_y, circle_radius, fx, fy, fr):
                if circle_radius >= fr:
                    eat_sound.play()
                    circle_radius += int(fr * 0.25)
                    foods.remove(food)
                    create_new_food()
                elif circle_radius < fr:
                    start()

        ######################
        # step 2: draw stuff #
        ######################

        player_draw()
        food_draw_all()

    pygame.display.flip()

pygame.quit()