import pygame
import random
from constants import *

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

    def update(self, frame_time: float):
        remove_indices: list[int] = []
        for part_i in range(len(self._parts)):
            part: Particle = self._parts[part_i]
            part.update(frame_time)
            #  check if the particle was offscreen                                                 or   if it is too old
            #  vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv    vvvvvvvvvvvvvvvvvvvvvvv
            if part._pos.x < 0 or part._pos.x >= WIDTH or part._pos.y < 0 or part._pos.y >= HEIGHT or part._lasting_time <= 0:
                remove_indices.append(part_i)
        # TODO: remove particles from self._parts using indices in remove_indices
        remove_indices.sort(reverse=True)
        for part_index in remove_indices:
            self._parts.pop(part_index)


    def draw(self, screen: pygame.Surface):
        for part in self._parts:
            part.draw(screen)
            

    def firework(self, pos: pygame.math.Vector2, color: pygame.Color, part_count: int, part_size: int, life_time: float, speed: int):
        for pn in range(part_count):
            velo = pygame.math.Vector2(0,-speed)
            velo.rotate_ip(random.randint(0, 360))
            variance = random.randint(1, speed)
            velo.scale_to_length(variance)
            # life_time *= variance / speed
            new_part = Particle(pos, velo, part_size, color, life_time * (variance / speed))
            self._parts.append(new_part)

    def burst(self, pos: pygame.math.Vector2, colors: list[pygame.Color], part_count: int, part_size: int, life_time: float, speed: int, dir: float, spread: float):
        assert(speed > 0)
        for pn in range(part_count):
            velo = pygame.math.Vector2(0,-speed)
            velo.rotate_ip(dir)
            velo.rotate_ip(random.randint(-spread // 2, spread // 2))
            variance = random.uniform(.2 * speed, speed)
            velo.scale_to_length(variance)
            color = random.choice(colors)
            new_part = Particle(pos, velo, part_size, color, life_time * (variance / speed))
            self._parts.append(new_part)