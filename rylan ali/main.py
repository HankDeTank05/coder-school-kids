
import sys
import pygame
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Set up the clock for managing the frame rate
fps = 60
fpsClock = pygame.time.Clock()

# Set up the window
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("maze_game")

# Main game loop
class Player:
    def __init__(self,x,y,width,height):
        self.box = pygame.Surface((width , height))
        self.rect = self.box.get_rect()
        self.rect.x = x
        self.rect.y =y 
        self.box.fill((254, 186, 23))

    def update_player(self):

        dx = 0
        dy = 0
        speed = 5
        key = pygame.key.get_pressed()
        if key[pygame.K_w]:
            dy -= speed
        if key[pygame.K_s]:
            dy += speed
        if key[pygame.K_d]:
            dx += speed
        if key[pygame.K_a]:
            dx -= speed


        if self.rect.top < 0 :
            self.rect.top = 0
            dy = 0
        if self.rect.bottom > height :
            self.rect.bottom = height
            dy = 0
        if self.rect.right > width :
            self.rect.right = width
            dx = 0
        if self.rect.left < 0 :
            self.rect.left = 0
            dx = 0





        self.rect.x +=dx 
        self.rect.y +=dy 


        screen.blit(self.box,self.rect)












player = Player(150,400, 20,20)



while True:
    screen.fill((245, 100, 169)) # Fill the screen with black
    player.update_player()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

# Update and draw code goes here

    pygame.display.flip() # Update the display
    fpsClock.tick(fps) # Maintain the frame rate







































