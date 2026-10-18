import pygame

class GameObject:
    # needs a position (so we know where to draw it)
    _pos: pygame.math.Vector2
    # needs a pygame.Surface to draw
    _image: pygame.Surface

    def __init__(self):
        print('GameObject constructor')
    
    def update(self, frame_time: float):
        print('GameObject update')

    def draw(self, screen: pygame.Surface):
        print('GameObject draw')
        screen.blit(self._image, self._pos)


class OompaLoompa(GameObject):

    def __init__(self):
        super().__init__()
        print('OompaLoompa constructor')
    
    def update(self, frame_time: float):
        print('OompaLoompa update')


ol = OompaLoompa()
ol.update(frame_time=0.0)
ol.draw(screen=pygame.Surface((1,1)))