import pygame
import random

class Particle:
    _pos: pygame.math.Vector2
    _velo: pygame.math.Vector2
    _size: int
    _color: pygame.Color
    _lasting_time: float

    def __init__(self, pos: pygame.math.Vector2, velo: pygame.math.Vector2, size: int, color: pygame.Color, lasting_time: float):
        self._pos = pos
        self._velo = velo
        self._size = size
        self._color = color
        self._lasting_time = lasting_time

    def update(self, frame_time: float):
        self._pos += self._velo * frame_time
        self._lasting_time -= frame_time

    def draw(self, screen: pygame.Surface):
        pygame.draw.rect(screen, self._color, pygame.Rect(
            self._pos - pygame.math.Vector2(self._size, self._size) / 2,
            pygame.math.Vector2(self._size, self._size)
        ))

class ParticleManager:
    _parts: list[Particle]

    def __init__(self):
        self._parts = []

    def firework(self, pos: pygame.math.Vector2, color: pygame.Color, part_count: int, part_size: int):
        for pn in range(part_count):
            velo = pygame.math.Vector2(0,-1)
            velo.rotate_ip(random.randint(0, 360))
            new_part = Particle(pos, velo, part_size, color)
            self._parts.append(new_part)