import pygame
import random
from constants import *
from copy import deepcopy

class Particle:
    _pos: pygame.math.Vector2
    _velo: pygame.math.Vector2
    _size: int
    _color: pygame.Color

    def __init__(self, pos: pygame.math.Vector2, velo: pygame.math.Vector2, size: int, color: pygame.Color):
        self._pos = pos
        self._velo = velo
        self._size = size
        self._color = color

    def update(self, frame_time: float):
        assert(False)

    def draw(self, screen: pygame.Surface):
        pygame.draw.rect(screen, self._color, pygame.Rect(
            self._pos - pygame.math.Vector2(self._size, self._size) / 2,
            pygame.math.Vector2(self._size, self._size)
        ))

class LifetimeParticle(Particle):
    _lasting_time: float
    
    def __init__(self, pos: pygame.math.Vector2, velo: pygame.math.Vector2, size: int, color: pygame.Color, lasting_time: float):
        super().__init__(pos, velo, size, color)
        self._lasting_time = lasting_time

    def update(self, frame_time: float) -> None:
        self._pos += self._velo * frame_time
        self._lasting_time -= frame_time

class MagPartState:
    pass

class MagneticParticle(Particle):
    _state: MagPartState
    _intial_velo: pygame.math.Vector2
    _target_pos: pygame.math.Vector2
    _first_time: float
    _mag_time: float

    MAX_TIME_FIRST: float = 3.0
    MAX_TIME_MAG: float = 3.0

    def __init__(self, pos: pygame.math.Vector2, velo: pygame.math.Vector2, size: int, color: pygame.Color, target_pos: pygame.math.Vector2):
        super().__init__(pos, velo, size, color)
        self._state = FirstMoveState()
        self._intial_velo = velo
        self._target_pos = target_pos
        self._first_time = 0
        self._mag_time = 0

    def update(self, frame_time: float) -> None:
        self._state.update(self, frame_time)
        self._state = self._state.get_next_state(self)

    def update_target(self, new_target_pos: pygame.math.Vector2) -> None:
        self._target_pos = new_target_pos


class MagPartState:


    def update(self, part: MagneticParticle, frame_time: float) -> None:
        assert(False)

    def get_next_state(self, part: MagneticParticle) -> MagPartState:
        assert(False)

class FirstMoveState(MagPartState):


    def update(self, part: MagneticParticle, frame_time: float) -> None:
        part._pos += part._velo * frame_time #move the particle
        part._first_time += frame_time #increase the timer
        #making a percent to slow down the particle gradually over time
        time_pcent_inv = 1 - (part._first_time / MagneticParticle.MAX_TIME_FIRST)
        part._velo = time_pcent_inv * part._intial_velo


    def get_next_state(self, part: MagneticParticle) -> MagPartState:
        if part._first_time >= MagneticParticle.MAX_TIME_FIRST:
            return MagnetState()
        else:
            return self


class MagnetState(MagPartState):


    def update(self, part: MagneticParticle, frame_time: float) -> None:
        part._mag_time += frame_time #increase the timer
        #calculate the velo
        dist_to_target = part._target_pos - part._pos
        time_pcent = part._mag_time / MagneticParticle.MAX_TIME_MAG
        print(f'dist to target: {dist_to_target.magnitude()}\ttime_pcent: {time_pcent}')
        part._velo = time_pcent * dist_to_target
        part._pos += part._velo * frame_time #move the particle


    def get_next_state(self, part: MagneticParticle) -> MagPartState:
        return self
    

class ParticleManager:
    _parts: list[Particle]

    def __init__(self):
        self._parts = []

    def update(self, frame_time: float, player_pos: pygame.math.Vector2):
        remove_indices: list[int] = []
        for part_i in range(len(self._parts)):
            part: Particle = self._parts[part_i]
            part.update(frame_time)
            if type(part) is MagneticParticle:
                part.update_target(player_pos)
            #  check if the particle was offscreen                                                 or   if it is too old
            #  vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv    vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
            if part._pos.x < 0 or part._pos.x >= WIDTH or part._pos.y < 0 or part._pos.y >= HEIGHT or (type(part) is LifetimeParticle and part._lasting_time <= 0) or (type(part) is MagneticParticle and part._mag_time >= MagneticParticle.MAX_TIME_MAG):
                remove_indices.append(part_i)
        # TODO: remove particles from self._parts using indices in remove_indices
        remove_indices.sort(reverse=True)
        for part_index in remove_indices:
            self._parts.pop(part_index)


    def draw(self, screen: pygame.Surface):
        for part in self._parts:
            part.draw(screen)
            

    def firework(self, pos: pygame.math.Vector2, colors: list[pygame.Color], part_count: int, part_size: int, life_time: float, speed: int):
        for pn in range(part_count):
            velo = pygame.math.Vector2(0,-speed)
            velo.rotate_ip(random.randint(0, 360))
            self._burst_helper(pos, colors, part_size, life_time, speed, 360, velo)
            # variance = random.randint(1, speed)
            # velo.scale_to_length(variance)
            # new_part = Particle(pos, velo, part_size, color, life_time * (variance / speed))
            # self._parts.append(new_part)

    def magnetic_firework(self, pos: pygame.math.Vector2, colors: list[pygame.Color], part_count: int, part_size: int, speed: int, target_pos: pygame.math.Vector2):
        for pn in range(part_count):
            velo = pygame.math.Vector2(0,-speed)
            velo.rotate_ip(random.randint(0, 360))
            self._magnetic_burst_helper(pos, colors, part_size, speed, 360, velo, target_pos)

    def burst(self, pos: pygame.math.Vector2, colors: list[pygame.Color], part_count: int, part_size: int, life_time: float, speed: int, dir: float, spread: float):
        assert(speed > 0)
        for pn in range(part_count):
            velo = pygame.math.Vector2(0,-speed)
            velo.rotate_ip(dir)
            self._burst_helper(pos, colors, part_size, life_time, speed, spread, velo)

    def burst(self, pos: pygame.math.Vector2, colors: list[pygame.Color], part_count: int, part_size: int, life_time: float, speed: int, dirv: pygame.math.Vector2, spread: float):
        assert(speed > 0)
        for pn in range(part_count):
            velo = deepcopy(dirv)
            self._burst_helper(pos, colors, part_size, life_time, speed, spread, velo)

    def _burst_helper(self, pos: pygame.math.Vector2, colors: list[pygame.Color], part_size: int, life_time: float, speed: int, spread: float, velo: pygame.math.Vector2):
        velo.rotate_ip(random.randint(-spread // 2, spread // 2))
        variance = random.uniform(.2 * speed, speed)
        velo.scale_to_length(variance)
        color = random.choice(colors)
        new_part = LifetimeParticle(pos, velo, part_size, color, life_time * (variance / speed))
        self._parts.append(new_part)

    def _magnetic_burst_helper(self, pos: pygame.math.Vector2, colors: list[pygame.Color], part_size: int, speed: int, spread: float, velo: pygame.math.Vector2, target_pos: pygame.math.Vector2):
        velo.rotate_ip(random.randint(-spread // 2, spread // 2))
        variance = random.uniform(.2 * speed, speed)
        velo.scale_to_length(variance)
        color = random.choice(colors)
        new_part = MagneticParticle(pos, velo, part_size, color, target_pos)
        self._parts.append(new_part)