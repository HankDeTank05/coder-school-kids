import pygame
import fighter
import stage
import gamemath as gm

pygame.init()
SCREEN_WIDTH=1280
SCREEN_HEIGHT=720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True
dt=0


player1=fighter.Fighter("red",1, screen)
player2=fighter.Fighter("blue",2, screen)
stage=stage.Platform(100, 600, 1080, 100, "brown")
        

def clear_screen():
    screen.fill("white")

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # clear screen
    clear_screen()

    #check collisions
    stage_collision_p1=gm.intersect_circle_rect(player1.pos.x, player1.pos.y, player1.radius, stage.x, stage.y, stage.width, stage.height)
    stage_collision_p2=gm.intersect_circle_rect(player2.pos.x, player2.pos.y, player2.radius, stage.x, stage.y, stage.width, stage.height)
    screen_collision_p1=gm.intersect_circle_rect(player1.pos.x, player1.pos.y, player1.radius, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
    screen_collision_p2=gm.intersect_circle_rect(player2.pos.x, player2.pos.y, player1.radius, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)

    if stage_collision_p1==True:
        player1.on_collision_stage(stage.y)
    if stage_collision_p2==True:
        player2.on_collision_stage(stage.y)

    if screen_collision_p1==False:
        player1.respawn()
    if screen_collision_p2==False:
        player2.respawn()

    #update
    player1.update(dt)
    player2.update(dt)
    stage.update(dt)
        
    #draw
    player1.draw(screen)
    player2.draw(screen)
    stage.draw(screen)
    
    pygame.display.flip()

    dt=clock.tick(60)/1000

pygame.quit()
