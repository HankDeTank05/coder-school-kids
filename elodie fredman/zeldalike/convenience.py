import pygame
from common import *


def load_sprite(path) -> pygame.Surface:
    return pygame.transform.scale(pygame.image.load(path), (TILE_WIDTH_PX, TILE_HEIGHT_PX))