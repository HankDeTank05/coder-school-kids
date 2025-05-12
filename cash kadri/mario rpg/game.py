import pygame
pygame.init() # will make this work

#create the screen
WIDTH = 1280
HEIGHT = 800
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

# colors (if you need more, go to this website: https://html-color.codes/)

PEACH_PUFF = (255, 218, 185)
DARK_SEA_GREEN = (143, 188, 143)
BLACK = (0,0,0)
WHITE = (255,255,255)

#playar variables 
p1_pstn = pygame.math.Vector2(100,100)
p1_size = 40

p1_stat_hp = 12
p1_stat_attack = 12
p1_stat_defense = 12


p1_punch_damage = 6 
p1_bonk_damage = 4 
p1_bop_damage = 8

#player functions 
def draw_player():
    # draw player 

    # we're drawing heads 
    pygame.draw.circle(SCREEN, PEACH_PUFF, p1_pstn, p1_size)

    #draw left eyebrow
    eyebrow_left_x = -30
    eyebow_top_y = -10
    eyebrow_width = 29
    eyebrow_height = 10
    left_eyebrow = pygame.Rect(p1_pstn.x + eyebrow_left_x, p1_pstn.y + eyebow_top_y, eyebrow_width, eyebrow_height)
    pygame.draw.rect(SCREEN, BLACK,  left_eyebrow)

    #draw right eyebrow
    right_eyebrow = []

    # 0 - blue
    right_eyebrow.append(pygame.math.Vector2(
        p1_pstn.x,
        p1_pstn.y - 2)) 
    
    # 1 - purple
    right_eyebrow.append(pygame.math.Vector2(
        right_eyebrow[0].x + eyebrow_width/4,
        p1_pstn.y-17))

    # 2 - red
    right_eyebrow.append(pygame.math.Vector2(
        right_eyebrow[0].x + eyebrow_width/2,
        p1_pstn.y - 19)) 
    
    # 3 - ORANGE
    right_eyebrow.append(pygame.math.Vector2(
        right_eyebrow[0].x + eyebrow_width/4*3,
        p1_pstn.y-17))

    # 4 - green
    right_eyebrow.append(pygame.math.Vector2(
        right_eyebrow[0].x + eyebrow_width,
        p1_pstn.y - 2)) 
    
    # 5 - CYAN
    right_eyebrow.append(pygame.math.Vector2(
        right_eyebrow[3].x,
        right_eyebrow[4].y))

    # 6 - yellow
    right_eyebrow.append(pygame.math.Vector2(
        right_eyebrow[0].x + eyebrow_width/2,
        p1_pstn.y - 10))
    
    # 7 GRAY
    right_eyebrow.append(pygame.math.Vector2(
        right_eyebrow[1].x,
        right_eyebrow[0].y))

    pygame.draw.polygon(SCREEN, BLACK, right_eyebrow)

    #draw da eyes 
    eyeball_size = 7 
    pupil_size = 3
    eye_left=pygame.math.Vector2(
        p1_pstn.x-p1_size/3,
        p1_pstn.y+4
    )
    pygame.draw.circle(SCREEN, BLACK, eye_left, eyeball_size) #draw left eyeball
    pygame.draw.circle(SCREEN, WHITE, eye_left, pupil_size) # draw left pupil 
    eye_right=pygame.math.Vector2(
        p1_pstn.x+p1_size/3 ,
        p1_pstn.y+4
    )
    pygame.draw.circle(SCREEN, BLACK, eye_right, eyeball_size) # draw right eyeball
    pygame.draw.circle(SCREEN, WHITE, eye_right, pupil_size)  # draw right pupil

    # draw the SMILE
    mouth_points = []

    mouth_width = 23
    mouth_down = 12

    # 0 - blue 
    mouth_points.append(pygame.math.Vector2(
        p1_pstn.x-mouth_width,
        p1_pstn.y+mouth_down
    ))

    # 4 - orange
    mouth_points.append(pygame.math.Vector2(
        p1_pstn.x+mouth_width,
        p1_pstn.y+mouth_down
    ))

    # 6 - pink
    mouth_points.append(pygame.math.Vector2(
        p1_pstn.x,
        p1_pstn.y+0.75*p1_size
    ))

    pygame.draw.polygon(SCREEN, WHITE, mouth_points)

#mr. enemy variables 
enemy_pstn = pygame.math.Vector2(200, 100)
enemy_size = pygame.math.Vector2(80,80)

enemy_stat_hp = 9
enemy_stat_attack = 9
enemy_stat_defense = 9

enemy_chomp_damage = 3
enemy_tailSwat_damage = 5
enemy_clawSlash_damage = 7

# enemy functions
def draw_enemy():
    # draw enemy 
    pygame.draw.rect(SCREEN, DARK_SEA_GREEN, pygame.Rect(enemy_pstn, enemy_size))
    # TODO : draw enemy next time 

#main game loop
while running:
    #closes the gam when we hit the x button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # update makes the code work

    # draw helps you make things appear 
    draw_player()
    draw_enemy()

    pygame.display.flip()
    clock.tick()


pygame.quit()