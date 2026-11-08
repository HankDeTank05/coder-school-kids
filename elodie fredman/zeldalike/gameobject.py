import pygame
import mysprite

class GameObject:
    # needs a pygame.Surface to draw
    _image: mysprite.MySprite
    _pos: pygame.math.Vector2

    def __init__(self):
        print('GameObject constructor')

    @property
    def pos(self) -> pygame.math.Vector2:
        return self._pos

    @pos.setter
    def pos(self, new_pos: pygame.math.Vector2) -> None:
        self._pos = new_pos

    @property
    def x(self) -> float:
        return self.pos.x

    @x.setter
    def x(self, new_x: float) -> None:
        self.pos.x = new_x

    @property
    def y(self) -> float:
        return self.pos.y

    @y.setter
    def y(self, new_y: float) -> None:
        self.pos.y = new_y

    # gameobject functions
    
    def update(self, frame_time: float):
        assert(False)

    def draw(self, screen: pygame.Surface):
        self._image.draw(screen=screen, draw_pos=self._pos)
