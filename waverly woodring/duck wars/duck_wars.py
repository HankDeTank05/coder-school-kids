import pygame, sys
from pygame.locals import QUIT

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Hello World!')

duck = pygame.image.load("placeholder_duck.png")
duck.convert_alpha()

while True:
    DISPLAYSURF.blit(duck, (0, 0))
    pygame.Surface.blit(DISPLAYSURF, duck, (0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.update()
