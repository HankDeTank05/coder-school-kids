# language imports (these are built in to python)
import random
import time

# library imports (this is stuff that's not ours, but not built in to python)
import pygame

# project imports (this is our stuff we created)
import common as c
import player as p
import obstacle as o

pygame.init()
pygame.font.init()

# create colors


font = pygame.font.SysFont(None, 48)

#Create screen
#width, height = random.randint(100, 250), random.randint(150, 300)

clock = pygame.time.Clock()

# Create player variables
#player_size = random.randint(5, 50)
# player_size = 50
# player_x = c.WIDTH // 2 - player_size // 2
# player_y = c.HEIGHT - player_size - 10
# player_speed = 350
# right_edge = c.WIDTH - player_size + 1
# bottom_edge = c.HEIGHT - player_size + 0
# player_rect = None
player = p.Player()

game_not_started = True
time_has_failed = 0

#add more power ups examples:
#(smaller player, smaller obstacle/faster,obstacle bigger,)
# groups (big/tracking/norm) (/big/fast) (tracking small fast) (tracking small norm)
# groups extension (big/fast) (small/fast) (small norm) (big norm) (tracking normal fast) (norm fast) (slow norm) (slow tracking norm)

# Creating powerup variables
power_up_speed = 300
power_up_color = (c.BLUE)
shield_timer = 0
slow_down_timer = 0
power_ups = []

# Obstacle
obstacle_width = 20
obstacle_height = 30
obstacle_speed = 500
obstacles = []
obstacle_spawn_timer = 0
obstacle_spawn_delay = 0.5
obstacle_x = random.randint(0, c.WIDTH - obstacle_width)
obstacle_y = -obstacle_height
obstacle_spawn_delay = 0.5
cheating = False
postCheat = False


# def player_update():
#     global player_x
#     global player_y

#     # move the player
#     keys = pygame.key.get_pressed()
#     move_x = 0
#     move_y = 0
#     if keys[pygame.K_UP]:
#         move_y -= 1
#     if keys[pygame.K_DOWN]:
#         move_y += 1
#     if keys[pygame.K_LEFT]:
#         move_x -= 1
#     if keys[pygame.K_RIGHT]:
#         move_x += 1
#     player_move = pygame.math.Vector2(move_x, move_y)
#     # correct diagonal movement
#     if player_move.length() > 0:
#         player_move = player_move.normalize() * player_speed * frame_time

#     # Moving player left/right
#     player_x += player_move.x
#     player_y += player_move.y

#     # Keeps player in the screen

#     # If player is partialy or totaly off screen on the left
#     if player_x < 0:
#         player_x = 0

#     # If player is partialy or totaly off screen on the right
#     elif player_x > right_edge:
#         player_x = right_edge

#     # If player is partialy or totaly off screen on the bottom
#     if player_y > bottom_edge:
#         player_y = bottom_edge


# def player_draw():
#     global player_rect
#     player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
#     pygame.draw.rect(c.SCREEN, c.BLUE, player_rect)


def obstacle_update():
    pass


def obstacle_draw(obstacle):
    obstacle['rect'] = pygame.Rect(obstacle['x'], obstacle['y'],
                                   obstacle['width'], obstacle['height'])
    if obstacle['type'] == 2:
        pygame.draw.rect(c.SCREEN, c.ORANGE, obstacle['rect'])
    else:
        pygame.draw.rect(c.SCREEN, c.RED, obstacle['rect'])


while game_not_started:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if keys[pygame.K_RSHIFT]:
        game_not_started = False
        print("Yay")
    c.SCREEN.fill(c.GREEN)
    text = font.render("Press shift on the right to begin", True, c.YELLOW)
    text_rect = text.get_rect(center=(c.WIDTH // 2, c.HEIGHT // 2))
    c.SCREEN.blit(text, text_rect)
    pygame.display.flip()

lives = 7

running = True
game_over = False
# main game loop
start_time = time.time()
while running:
    frame_time = clock.tick(60) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    shield_timer -= frame_time
    slow_down_timer -= frame_time
    time_has_failed += frame_time
    #print(time_has_failed)
    text = font.render(str(lives), True, c.RED)
    text_rect = text.get_rect(center=(40, 40))
    c.SCREEN.blit(text, text_rect)

    ##################
    # part 1: update #
    ##################

    player.update(frame_time)

    # Speeds up obstacles, player and powerups
    if time.time() > start_time + 10:
        obstacle_speed += 20
        player.change_speed(10)
        power_up_speed += 5
        start_time = time.time()

    obstacle_spawn_timer += frame_time
    # if its time to spawn a new obstacle...
    if obstacle_spawn_timer >= obstacle_spawn_delay:
        obstacle_spawn_timer = 0  # restart timer

        explodey = False
        obstacle_type = random.choice([
            "small", "normal", "normal", "normal", "normal", "normal",
            "normal", "normal", "normal", "normal", "normal", "normal",
            "normal", "normal", "normal", "normal", "normal", "normal",
            "normal", "big"
        ])
        #obstacle_type="small"

        #small_obstacle = random.choice([True,False,False,False,False,False,False,False,False,False,False,False,False,False,False])
        if obstacle_type == "small":
            obstacle_width = 15.98769876987
            obstacle_height = 21.98769876987
            obstacle_speed = 550
            if random.randint(0, 100) < 20:
                explodey = True
        elif obstacle_type == "normal":
            obstacle_height = 30
            obstacle_width = 20
            obstacle_speed = 500
        elif obstacle_type == "big":
            obstacle_width = 30.12341234123
            obstacle_height = 40.12341234123
            obstacle_speed = 450
        # new_obstacle_object = o.Obstacle(obstacle_width, obstacle_height, obstacle_speed, explodey)

        new_obstacle = {
            # making sure the obstacle could hit the player by spawning within the horizontal boudaries
            'x': random.randint(0, 480),
            'y': -obstacle_height,
            'width': obstacle_width,
            'height': obstacle_height,
            'type': 1,
            'speed': obstacle_speed,
            'explodes': explodey
        }
        new_obstacle['rect'] = pygame.Rect(new_obstacle['x'],
                                           new_obstacle['y'], obstacle_width,
                                           obstacle_height)
        if time_has_failed >= 20:
            random.randint(1, 80)
            if random.randint(1, 80) >= 70:
                new_obstacle['speed'] = int(obstacle_speed * 1.4)

        if time_has_failed >= 30:
            random.randint(1, 80)
            if random.randint(1, 80) >= 60:
                new_obstacle['type'] = 2
        if lives <= 2:
            random.randint(1, 80)
            if random.randint(1, 80) >= 70:
                better_obstacle = {
                    'x': random.randint(0, 480),
                    'y': -obstacle_height,
                    'width': obstacle_width,
                    'height': obstacle_height,
                    'type': random.randint(1, 2)
                }

                power_ups.append(better_obstacle)
                print("Get the not red/orange obstacle")

        obstacles.append(new_obstacle)
        # obstacles.append(new_obstacle_object)

    for obstacle in obstacles:
        if slow_down_timer > 0:
            # move the obstacles slowly if they got a powerup
            obstacle['y'] += obstacle['speed'] * frame_time / 4
            obstacle_spawn_delay = 2
        else:
            # move the obstacles normal speed if no powerup
            obstacle['y'] += obstacle['speed'] * frame_time
        if obstacle['y'] > c.HEIGHT:
            if obstacle["type"] == 3 or obstacle["type"] == 4:
                new_obstacle = {
                    # making sure the obstacle could hit the player by spawning within the horizontal boudaries
                    'x': obstacle["x"],
                    'y': 0,
                    'width': obstacle["width"],
                    'height': obstacle["height"],
                    'type': 1,
                    'speed': obstacle["speed"],
                    'explodes': False
                }
                obstacles.append(new_obstacle)
            obstacles.remove(obstacle)
            obstacle_spawn_delay = 0.5

        if obstacle['type'] == 2:  #power up
            obstacle_x_speed = 200
            if slow_down_timer >= 1:
                obstacle_x_speed = 200 / 4
            if obstacle['x'] > player.get_pos().x:
                obstacle['x'] -= obstacle_x_speed * frame_time
            if obstacle['x'] < player.get_pos().x:
                obstacle['x'] += obstacle_x_speed * frame_time
        if obstacle['type'] == 3:
            obstacle['x'] -= 100 * frame_time
        if obstacle['type'] == 4:
            obstacle['x'] += 100 * frame_time
        if obstacle['type'] == 4:
            obstacle['x']
        if obstacle['explodes'] and obstacle['y'] > 50:  #and obstacle['y']<500:
            print("boom!")

            for x in range(2):
                new_obstacle = {
                    'x': obstacle['x'] - 50,
                    'y': obstacle['y'],
                    'width': 30.12341234123,
                    'height': 40.12341234123,
                    'type': 3,  #drifting left
                    'speed': obstacle["speed"],
                    'explodes': False
                }
                obstacles.append(new_obstacle)

            for x in range(2):
                new_obstacle = {
                    'x': obstacle['x'] - 30,
                    'y': obstacle['y'],
                    'width': 30.12341234123,
                    'height': 40.12341234123,
                    'type': 4,  #drifting right
                    'speed': obstacle["speed"],
                    'explodes': False
                }
                obstacles.append(new_obstacle)
            print("removing")
            if obstacle in obstacles:
                obstacles.remove(obstacle)

    ################
    # part 2: draw #
    ################

    for power_up in power_ups:
        power_up['y'] += power_up_speed * frame_time
        if power_up['y'] > c.HEIGHT:
            power_ups.remove(power_up)

    # Start drawing
    c.SCREEN.fill(c.WHITE)
    if player.get_pos().y < 0:
        if not cheating:
            cheatTime = time.time()
            cheating = True
            postCheat = False
        else:
            if time.time() > cheatTime + 5:
                player.set_y(300)
                cheating = False
                postCheat = True
                postCheatTime = time.time()

        text = font.render("YOU'RE A BAD PERSON ", True, c.RED)
        text_rect = text.get_rect(center=(c.WIDTH // 2, c.HEIGHT // 2))
        c.SCREEN.blit(text, text_rect)

        text2 = font.render("CHEATER!!!!!!! ", True, c.RED)
        text_rect = text2.get_rect(center=(c.WIDTH // 2, c.HEIGHT // 2 + 40))
        c.SCREEN.blit(text2, text_rect)

    if postCheat:
        if time.time() < postCheatTime + 2:
            text = font.render("THIS IS PAYBACK", True, c.RED)
            text_rect = text.get_rect(center=(c.WIDTH // 2, c.HEIGHT // 2 - 40))
            c.SCREEN.blit(text, text_rect)
        else:
            postCheat = False

    # Drawing the player
    player.draw()

    for obstacle in obstacles[:]:
        obstacle_draw(obstacle)

        if player._rect.colliderect(obstacle['rect']):
            print("Collision detected!")
            if shield_timer > 0:
                obstacles.remove(obstacle)
            else:
                obstacles.remove(obstacle)
                lives -= 1

    for power_up in power_ups:
        power_up_rect = pygame.Rect(power_up['x'], power_up['y'],
                                    power_up['width'], power_up['height'])
        if power_up['type'] == 1:
            pygame.draw.rect(c.SCREEN, c.BLUE, power_up_rect)
        else:
            pygame.draw.rect(c.SCREEN, c.YELLOW, power_up_rect)

        if player._rect.colliderect(power_up_rect):
            if power_up['type'] == 1:
                shield_timer = 5
            else:
                slow_down_timer = 7
            power_ups.remove(power_up)

    if shield_timer > 0:
        text = font.render(str(round(shield_timer)), True, c.RED)
        text_rect = text.get_rect(center=(c.WIDTH // 2, 20))
        c.SCREEN.blit(text, text_rect)

    if slow_down_timer > 0:
        text = font.render(str(round(slow_down_timer)), True, c.RED)
        text_rect = text.get_rect(center=(c.WIDTH // 2, 60))
        c.SCREEN.blit(text, text_rect)

    if lives <= 0:
        running = False
        c.SCREEN.fill(c.BLACK)
        text = font.render("GAME OVER", True, c.RED)
        text_rect = text.get_rect(center=(c.WIDTH // 2, c.HEIGHT // 2))
        c.SCREEN.blit(text, text_rect)

    pygame.display.flip()
time.sleep(5)

pygame.quit()
