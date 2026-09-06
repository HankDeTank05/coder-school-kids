import pygame
from common import *


def load_sprite(path) -> pygame.Surface:
    img_surf = pygame.image.load(path)
    return pygame.transform.scale(img_surf, (img_surf.get_width()*SCALE_FACTOR, img_surf.get_height()*SCALE_FACTOR))