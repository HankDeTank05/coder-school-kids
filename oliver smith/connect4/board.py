import pygame
from pieces import Pieces
from constants import *


class Board:


    def __init__(self, column_count, row_count, x, y):
        self._column_ct = column_count
        self._row_ct = row_count
        self._click_zones = []
        for row in range(self._row_ct):
            self._click_zones.append([])
            for col in range(self._column_ct):
                zone = pygame.Rect(
                    self.grid_to_px(pygame.math.Vector2(col, row)) - pygame.math.Vector2(CIRCLE_RADIUS, CIRCLE_RADIUS),
                    pygame.math.Vector2(CIRCLE_RADIUS, CIRCLE_RADIUS) * 2
                )
                self._click_zones[row].append(zone)
        self._hover_zone = pygame.math.Vector2(-1, -1)
        self._clicked_zone = pygame.math.Vector2(-1, -1)
        self._chips = []
        for row in range(self._row_ct):
            self._chips.append([])
            for col in range(self._column_ct):
                self._chips[row].append(None)

    def update(self, frame_time):
        self._hover_zone = pygame.math.Vector2(-1, -1)
        self._clicked_zone = pygame.math.Vector2(-1, -1)
        mx, my = pygame.mouse.get_pos()
        for row in range(self._row_ct):
            for col in range(self._column_ct):
                if self._click_zones[row][col].collidepoint(mx, my):
                    self._hover_zone = pygame.math.Vector2(col, row)
                    if pygame.mouse.get_pressed()[0]:
                        self._clicked_zone = pygame.math.Vector2(col, row)
                        self._chips[row][col] = 1

    def draw(self, screen):
        circ_radius = 75
        for row in range(self._row_ct):
            for col in range(self._column_ct):
                circ_center = self.grid_to_px(pygame.math.Vector2(col, row))
                circ_color = COLOR_WHITE
                if col == self._clicked_zone.x and row == self._clicked_zone.y:
                    circ_color = COLOR_CYAN
                elif self._chips[row][col] is not None:
                    circ_color = COLOR_RED
                pygame.draw.circle(screen, circ_color, circ_center, circ_radius)

                rect_line_width = 1
                if col == self._hover_zone.x and row == self._hover_zone.y:
                    rect_line_width = 3
                pygame.draw.rect(screen, COLOR_RED, self._click_zones[row][col], width=rect_line_width)

    def grid_to_px(self, grid_pos: pygame.math.Vector2) -> pygame.math.Vector2:
        return pygame.math.Vector2(
            (CIRCLE_RADIUS + X_EDGE_SPACING) + grid_pos.x * (CIRCLE_RADIUS * 2 + X_CIRCLE_SPACING),
            (CIRCLE_RADIUS + Y_EDGE_SPACING) + grid_pos.y * (CIRCLE_RADIUS * 2 + Y_CIRCLE_SPACING),
        )