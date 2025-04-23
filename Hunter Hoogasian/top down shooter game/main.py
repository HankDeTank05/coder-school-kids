import pygame, sys
from pygame.locals import QUIT

# constants - A varieble that shold never change
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 300
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

pygame.init()
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Hello World!')
clock = pygame.time.Clock()
delta_time = 0

#Player varibles
player_speed = 85
player_pos = pygame.math.Vector2(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
player_size = 50
player_pos_delta = pygame.math.Vector2(0,0)
player_aim_dir = pygame.math.Vector2(0,0)

#Bullet variebles
bullet_width = 5
bullet_height = 5
bullet_rect = pygame.Rect(0, 0, bullet_width, bullet_height)
bullet_pos_delta = pygame.math.Vector2(0, 0)

#Main game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    #Without screen fill, the computer wants to move the circle around with out overwriteing the previously rendered frames of the circle.
    SCREEN.fill( (0,0,0) )

    ##########
    # update #
    ##########
    
    player_pos_delta = pygame.math.Vector2(0,0) #Reset pos delta to 0 every frame, in other words no acceleration or deceleration
    keys = pygame.key.get_pressed() #Get the state of the keys on this frame
    #Read input for moving/walking 
    if keys[pygame.K_w] == True:
        player_pos_delta += pygame.math.Vector2(0, -player_speed)
    if keys[pygame.K_s] == True:
        player_pos_delta += pygame.math.Vector2(0, player_speed)
    if keys[pygame.K_a] == True:
        player_pos_delta += pygame.math.Vector2(-player_speed, 0)
    if keys[pygame.K_d] == True:
        player_pos_delta += pygame.math.Vector2(player_speed, 0)

    if player_pos_delta.x != 0 and player_pos_delta.y != 0:
        # fix diagonal movement distance
        # normalize (divide vector by its length)
        player_pos_delta.normalize_ip()
        player_pos_delta *= player_speed

    #Read input for mouse cursor postion to aim
    # aim_dir = pygame.math.Vector2(0,0)
    #This is a vector pointing from the player to the mouse
    player_aim_dir = pygame.mouse.get_pos() - player_pos

    # As long as the vector legnth is not 0...
    if player_aim_dir.length_squared() != 0:
        player_aim_dir.normalize_ip() #...normalize
        
    # Read input for firing
    buttons = pygame.mouse.get_pressed()
    if buttons[0] == True:
        #Fire the bullet
        bullet_rect.move_ip(player_pos.x, player_pos.y) # TODO: Set the postion of the bullet
        bullet_pos_delta = player_aim_dir
    
    # this makes the movement look smooth
    player_pos_delta *= delta_time # this is a short hand for pos_delta = pos_delta * delta_time
    # This makes the circle move
    player_pos += player_pos_delta # player_pos = player_pos + player_pos_delta

    #This makes the movement look smooth
    #bullet_pos_delta *= delta_time
    #make the bulet move
    bullet_rect.move_ip(bullet_pos_delta.x * delta_time, bullet_pos_delta.y * delta_time)        
    
    ########
    # draw #
    ########

    #First, it is drawing the circle, with a blue color.
    pygame.draw.circle(SCREEN, BLUE, player_pos, player_size)
    #Drawing a line for the aim direcetion
    pygame.draw.line(SCREEN, RED, player_pos, player_pos + player_aim_dir * player_size)

    #Bullet drawing sequence
    pygame.draw.rect(SCREEN, GREEN, bullet_rect)

    #Makes the drawings visible on the screen
    pygame.display.update()
    
    delta_time = clock.tick(60)/1000