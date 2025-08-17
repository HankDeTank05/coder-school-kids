# language imports (stuff built into python)
import math
import random

# library imports (not built in stuff, but not my code)
import pygame

# project imports (my code)
import gamemath

# Initialize Pygame and Mixer
pygame.init()
pygame.mixer.init()

# Screen Setup
WIDTH, HEIGHT = 1240, 600
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

# Game State
game_state = "menu"
menu_start_time = pygame.time.get_ticks()  # Get start time of menu

# Player Setup
circle_x, circle_y = 78, 295
circle_radius = 32
speed = 100

# Food List
foods = [
    [78, 45, 12, (45, 27, 232)],
    [250, 250, 20, (255, 225, 0)],
    [380, 129, 42, (0, 255, 0)],
    [703, 159, 89, (225, 171, 22)],
    [684, 547, 109, (0, 247, 255)],
]

def create_new_food():
    new_radius = random.randint(10, 80)
    new_x = random.randint(new_radius, WIDTH - new_radius)
    new_y = random.randint(new_radius, HEIGHT - new_radius)
    new_color = (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255)
    )
    while True:
        #1. check if the newly created food overlaps with ANY existing food
        #2a. if it does, re-generate a new food, and re-run the loop
        #2b. if it does not, exit the loop
        pass
    foods.append([new_x, new_y, new_radius, new_color])

# Game Loop
while running:
    frame_time = clock.tick(60) / 1000  # 60 FPS
    screen.fill((89, 134, 203))  # Background color

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Auto switch from menu to playing after 3 seconds (3000 ms)
    if game_state == "menu":
        elapsed_time = pygame.time.get_ticks() - menu_start_time
        if elapsed_time >= 3000:
            game_state = "playing"

    #if game_state == "menu":
        title_text = font.render("Glitchy Ripoff Agario", True, (0, 0, 0))
        prompt_text = small_font.render("Get Ready...3...2...1!", True, (0, 0, 0))
        screen.blit(title_text, ((WIDTH - title_text.get_width()) // 2, HEIGHT // 3))
        screen.blit(prompt_text, ((WIDTH - prompt_text.get_width()) // 2, HEIGHT // 2))

    elif game_state == "playing":
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

        # Draw food and check collisions
        for food in foods:
            fx, fy, fr, color = food
            pygame.draw.circle(screen, color, (int(fx), int(fy)), fr) # Puts food on screen / draws food
            #  Checks if cirlces overlap                                                If player circle is larger than food circle
            #  vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv     vvvvvvvvvvvvvvvvvvvv
            if gamemath.circle_overlap(circle_x, circle_y, circle_radius,fx, fy,fr) and circle_radius >= fr:
                eat_sound.play()
                circle_radius += int(fr * 0.5)
                foods.remove(food)
                create_new_food()

        # Draw player
        pygame.draw.circle(screen, (245, 45, 67), (int(circle_x), int(circle_y)), circle_radius)

    pygame.display.flip()

pygame.quit()