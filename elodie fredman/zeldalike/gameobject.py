import pygame
import mysprite

class GameObject:
    # needs a pygame.Surface to draw
    _image: mysprite.MySprite

    def __init__(self):
        print('GameObject constructor')
    
    def update(self, frame_time: float):
        assert(False)

    def draw(self, screen: pygame.Surface):
        self._image.draw(screen=screen)
