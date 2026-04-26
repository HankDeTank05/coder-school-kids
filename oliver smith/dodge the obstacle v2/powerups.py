import pygame
import pygame.gfxdraw
import random
from constants import *
from movingobj import MovingObject
from enum import Enum

class PupType(Enum):
    Invincibility = 1
    HealthBoost = 2
    SlowDown = 3


class Powerup(MovingObject):

    def __init__(self, rect: pygame.Rect, color, type: PupType):
        super().__init__(rect, POWERUP_SPEED, color)
        self._type = type
        self._stop_range_top = 0.4
        self._stop_range_btm = 0.9
        rounded_stop_rangetop = round(self._stop_range_top * HEIGHT, None)
        rounded_stop_rangebtm = round(self._stop_range_btm * HEIGHT, None)
        self._stop_point = random.randint(
            rounded_stop_rangetop,
            rounded_stop_rangebtm
        )
        self._stopped_time = 25
        self._current_stop_time = 0
        self._set_start_pos()
        

    # game functions

    def update(self, frame_time):
        if self._rect.y < self._stop_point: #if the powerup is above the stopping point
            self._rect.move_ip(0, self._speed * frame_time) #keeps moving down
        else:
            self._current_stop_time += frame_time

    def draw(self, screen):
        pygame.draw.rect(screen, self._color, self._rect)

    # accessors
    
    def get_current_stop_time(self)-> float:
        return self._current_stop_time
    
    def get_stop_time(self) -> float:
        return self._stopped_time
    
    def get_rect(self) -> pygame.Rect:
        return self._rect

    def get_type(self) -> PupType:
        return self._type


class Invincibility(Powerup):

    def __init__(self):
        temp_rect = pygame.Rect(0, 0, INVINC_POWERUP_WIDTH, INVINC_POWERUP_HEIGHT)
        super().__init__(temp_rect, MIDNIGHT_BLUE, PupType.Invincibility)

class HealthPower(Powerup):

    def __init__(self):
        temp_rect = pygame.Rect(0,0, HEALTH_POWERUP_SIZE, HEALTH_POWERUP_SIZE)
        temp_rect_old_center = temp_rect.center
        super().__init__(temp_rect, CORAL_RED, PupType.HealthBoost)
        temp_rect_new_center = self._rect.center
        self._points = [pygame.math.Vector2(temp_rect_new_center)]
        self._points.append(self._points[-1] + pygame.math.Vector2(4, -6))
        self._points.append(self._points[-1] + pygame.math.Vector2(5, -2))
        self._points.append(self._points[-1] + pygame.math.Vector2(5, 2))
        self._points.append(self._points[-1] + pygame.math.Vector2(1, 6))
        self._points.append(self._points[-1] + pygame.math.Vector2(-15, 17))
        self._points.append(self._points[-1] + pygame.math.Vector2(-15, -17))
        self._points.append(self._points[-1] + pygame.math.Vector2(1, -6))
        self._points.append(self._points[-1] + pygame.math.Vector2(5, -2))
        self._points.append(self._points[-1] + pygame.math.Vector2(5, 2))
        self._points.append(self._points[-1] + pygame.math.Vector2(4, 6))

    def update(self, frame_time):
        old_rect_center = self._rect.center
        super().update(frame_time)
        new_rect_center = self._rect.center
        delta = pygame.math.Vector2(new_rect_center) - pygame.math.Vector2(old_rect_center)
        for point in self._points:
            point += delta



    def draw(self, screen):
        # pygame.draw.polygon(screen, self._color, self._points)
        # pygame.draw.aalines(screen, self._color, True, self._points)
        
        pygame.gfxdraw.filled_polygon(screen, self._points, self._color)
        pygame.gfxdraw.aapolygon(screen, self._points, self._color)
        pygame.display.flip()

        # draw bounding box
        pygame.draw.rect(screen, BLACK, self._rect, width=1)

class PowerupManager:

    def __init__(self):
        self._powers: list[Powerup] = []
        self._spawn_timer = 0
        

    def update(self, frame_time, player_hp, player_max_hp):
        if player_hp <= player_max_hp * POWERUP_SPAWN_HEALTH_AMT:
            self._spawn_timer += frame_time
            print(self._spawn_timer)
            # TODO: uncomment the following lines
            if self._spawn_timer >= POWERUP_SPAWN_DELAY:
                self._spawn_timer -= POWERUP_SPAWN_DELAY
                pwrup_choice = random.randint(1,2)
                if pwrup_choice == 1:
                    new_power = Invincibility()
                    self._powers.append(new_power)
                elif pwrup_choice == 2:
                    new_health_power = HealthPower()
                    self._powers.append(new_health_power)
        for power in self._powers:
            power.update(frame_time)

        


    def draw(self, screen):
        for power in self._powers:
            power.draw(screen)

    def get_pwrs(self):
        return self._powers
    
    def remove_pwrs(self, pwrs_indices: list[int]):
        pwrs_indices.sort(reverse=True)
        for pwr_index in pwrs_indices:
            self._powers.pop(pwr_index)