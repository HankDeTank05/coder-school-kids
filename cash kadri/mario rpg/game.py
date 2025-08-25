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
WHITE = (255, 255, 255)
BLUE = (0, 55, 255)
RED = (255, 0, 0)

#playar variables 
p1_pstn = pygame.math.Vector2(100,100)
p1_radius = 40
    
p1_leg_width = p1_radius / 2
p1_leg_height = 70

belly_pstn = p1_pstn + pygame.math.Vector2(0, 1.75 * p1_radius)

def draw_legs():
    #right leg 
    right_leg = pygame.Rect(p1_pstn.x + 5, p1_pstn.y + 101, p1_leg_width, p1_leg_height)
    pygame.draw.rect(SCREEN, RED, right_leg)
    left_leg = pygame.Rect(p1_pstn.x - 5 - p1_leg_width, p1_pstn.y + 101, p1_leg_width, p1_leg_height)
    pygame.draw.rect(SCREEN, RED, left_leg)

def draw_arms() :

    # TODO: come back and draw two arms
    punchyarm_right_points = []

    #blu 0
    punchyarm_right_points.append(pygame.math.Vector2(
        p1_pstn.x + 24, 
        p1_pstn.y + 63))
    
    #green 1
    punchyarm_right_points.append(pygame.math.Vector2(
        p1_pstn.x + 39,
        p1_pstn.y + 45))
    
    #yelloh 2
    punchyarm_right_points.append(pygame.math.Vector2(
        p1_pstn.x + 77,
        p1_pstn.y + 67))
    
    #REHD 3
    punchyarm_right_points.append(pygame.math.Vector2(
        p1_pstn.x + 83,
        p1_pstn.y + 41))
    
    #Oranj 4
    punchyarm_right_points.append(pygame.math.Vector2(
        p1_pstn.x + 91,
        p1_pstn.y + 63))
    
    # pirpull 5

    punchyarm_right_points.append(pygame.math.Vector2(
        p1_pstn.x + 77,
        p1_pstn.y + 77
    )) 

    # draws the red polygon as in the Right arm
    pygame.draw.polygon(SCREEN, RED, punchyarm_right_points)
    

    punchyarm_left = pygame.Rect(p1_pstn.x - 58, p1_pstn.y + 45, p1_leg_width, p1_leg_height)
    pygame.draw.rect(SCREEN, RED, punchyarm_left)

def draw_body() :
    # we are drooing the playa's bodi
    pygame.draw.circle(SCREEN, BLUE, belly_pstn, p1_radius)

def draw_head() :
    # we're drawing heads 
    pygame.draw.circle(SCREEN, PEACH_PUFF, p1_pstn, p1_radius) 

def draw_nose(face_pstn):
    nose_width = 16 
    nose_height = 21
    nose_points = []

    # 0 
    nose_points.append(pygame.math.Vector2(
        face_pstn.x, 
        face_pstn.y
    )) 

    # 1 
    nose_points.append(pygame.math.Vector2(
        face_pstn.x +7,
        face_pstn.y + 9
    ))

    # 2 
    nose_points.append(pygame.math.Vector2(
        face_pstn.x + 8,
        face_pstn.y + 18
    )) 

    # 3 
    nose_points.append(pygame.math.Vector2(
        face_pstn.x,
        face_pstn.y + nose_height 
    ))

    # 4 
    nose_points.append(pygame.math.Vector2(
        face_pstn.x - 8, 
        face_pstn.y + 18 
    ))

    # 5
    nose_points.append(pygame.math.Vector2(
        face_pstn.x - 7,
        face_pstn.y + 9 
    ))

    pygame.draw.polygon(SCREEN,RED, nose_points )

    left_nostril_points = []
    nostril_width = 8
    nostril_height = 5

    left_nostril_points.append(pygame.math.Vector2(
        nose_points[4].x,
        nose_points[4].y - 5
    ))

    # 1 
    left_nostril_points.append(pygame.math.Vector2(
        left_nostril_points[0].x + 8,
        left_nostril_points[0].y + 2.5
    ))

    left_nostril_points.append(pygame.math.Vector2(
        nose_points[4].x,
        nose_points[4].y
    ))

    pygame.draw.polygon(SCREEN, BLACK,  left_nostril_points)

def draw_face(face_pstn):
    #draw left eyebrow
    eyebrow_left_x = -30
    eyebow_top_y = -10
    eyebrow_width = 29
    eyebrow_height = 10
    pygame.draw.circle(SCREEN, RED, face_pstn, 1)
    left_eyebrow = pygame.Rect(face_pstn.x + eyebrow_left_x, face_pstn.y + eyebow_top_y, eyebrow_width, eyebrow_height)
    pygame.draw.rect(SCREEN, BLACK,  left_eyebrow)

    #draw right eyebrow
    right_eyebrow = []

    # 0 - blue
    right_eyebrow.append(pygame.math.Vector2(
        face_pstn.x,
        face_pstn.y - 2)) 
    
    # 1 - purple
    right_eyebrow.append(pygame.math.Vector2(
        right_eyebrow[0].x + eyebrow_width/4,
        face_pstn.y-17))

    # 2 - red
    right_eyebrow.append(pygame.math.Vector2(
        right_eyebrow[0].x + eyebrow_width/2,
        face_pstn.y - 19)) 
    
    # 3 - ORANGE
    right_eyebrow.append(pygame.math.Vector2(
        right_eyebrow[0].x + eyebrow_width/4*3,
        face_pstn.y-17))

    # 4 - green
    right_eyebrow.append(pygame.math.Vector2(
        right_eyebrow[0].x + eyebrow_width,
        face_pstn.y - 2)) 
    
    # 5 - CYAN
    right_eyebrow.append(pygame.math.Vector2(
        right_eyebrow[3].x,
        right_eyebrow[4].y))

    # 6 - yellow
    right_eyebrow.append(pygame.math.Vector2(
        right_eyebrow[0].x + eyebrow_width/2,
        face_pstn.y - 10))
    
    # 7 GRAY
    right_eyebrow.append(pygame.math.Vector2(
        right_eyebrow[1].x,
        right_eyebrow[0].y))

    pygame.draw.polygon(SCREEN, BLACK, right_eyebrow)

    #draw da eyes 
    eyeball_size = 7 
    pupil_size = 3
    eye_left=pygame.math.Vector2(
        face_pstn.x-p1_radius/3,
        face_pstn.y+4
    )
    pygame.draw.circle(SCREEN, BLACK, eye_left, eyeball_size) #draw left eyeball
    pygame.draw.circle(SCREEN, WHITE, eye_left, pupil_size) # draw left pupil 
    eye_right=pygame.math.Vector2(
        face_pstn.x+p1_radius/3 ,
        face_pstn.y+4
    )
    pygame.draw.circle(SCREEN, BLACK, eye_right, eyeball_size) # draw right eyeball
    pygame.draw.circle(SCREEN, WHITE, eye_right, pupil_size)  # draw right pupil

    #draw da knowse
    draw_nose(face_pstn)


    # draw the SMILE
    mouth_points = []

    mouth_width = 23
    mouth_down = 12

    # 0 - blue 
    mouth_points.append(pygame.math.Vector2(
        face_pstn.x - mouth_width,
        face_pstn.y + mouth_down
    ))

    # point 1 and yellow
    mouth_points.append(pygame.math.Vector2(
        face_pstn.x - 0.5 * mouth_width, 
        face_pstn.y + 0.35 * p1_radius
    ))

    #2 reddy
    mouth_points.append(pygame.math.Vector2(
        face_pstn.x,
        face_pstn.y + 0.5 * p1_radius
    ))# 0.5 = 1 half 

    #point 3 and green 
    mouth_points.append(pygame.math.Vector2(
        face_pstn.x + 0.5 * mouth_width,
        face_pstn.y + 0.35 * p1_radius
    ))

    # 4 - orange
    mouth_points.append(pygame.math.Vector2(
        face_pstn.x + mouth_width,
        face_pstn.y + mouth_down
    ))

    # the 5 and purple
    mouth_points.append(pygame.math.Vector2(
        face_pstn.x + 0.5 * mouth_width,
        face_pstn.y + 0.65 * p1_radius 
    ))

    # 6 - pink
    mouth_points.append(pygame.math.Vector2(
        face_pstn.x,
        face_pstn.y + 0.75 * p1_radius
    ))#0.75 = 3 quarters

    #point 7 and teel
    mouth_points.append(pygame.math.Vector2(
        face_pstn.x - 0.5 * mouth_width,
        face_pstn.y + 0.65 * p1_radius
    )) #0.7 = 7/10 or 70% (remember THIS)

    pygame.draw.polygon(SCREEN, WHITE, mouth_points)

#player functions 
def draw_player():
    # draw player  

    draw_legs()

    draw_arms() 
    
    draw_body() 

    draw_face(belly_pstn)

    draw_head()

    draw_face(p1_pstn)



p1_stat_hp = 12
p1_stat_attack = 12
p1_stat_defense = 12


p1_punch_damage = 6 
p1_bonk_damage = 4 
p1_bop_damage = 8




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