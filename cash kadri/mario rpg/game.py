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

    #we draw eyebrows
    eyebrow_left_x = -30
    eyebow_top_y = -10
    eybrow_width = 29
    eyebrow_height = 10
    left_eyebrow = pygame.Rect(p1_pstn.x + eyebrow_left_x, p1_pstn.y + eyebow_top_y, eybrow_width, eyebrow_height)
    pygame.draw.rect(SCREEN, BLACK,  left_eyebrow)

    point_list = []
    point_list.append(pygame.math.Vector2(p1_pstn.x,p1_pstn.y-5))
    point_list.append(point_list[0].x+7,point_list[0].y-7)
    #TODO come back add 3rd point
    pygame.draw.polygon(SCREEN,BLACK,)

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