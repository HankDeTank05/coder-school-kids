import pygame
from constants import *


class Board:
    _column_ct: int # how many columns there are on the board
    _row_ct: int # how many rows there are on the board
    _chips: list[list[None | int]]
    _colors: list[pygame.Color]
    _player_ct: int
    _current_turn: int


    def __init__(self, column_count: int, row_count: int, player_count: int):
        self._column_ct = column_count
        self._row_ct = row_count

        self._chips = []
        for row in range(self._row_ct):
            self._chips.append([])
            for col in range(self._column_ct):
                self._chips[row].append(None)

        self._colors = [
            COLOR_RED,
            COLOR_YELLOW,
            COLOR_GREEN,
            COLOR_MIDNIGHT_BLUE,
            COLOR_GOLDENROD,
            COLOR_CORAL_RED,
            COLOR_TEAL,
            COLOR_ORANGE,
            COLOR_CYAN,
            COLOR_BLACK
        ]

        self._player_ct = player_count
        assert(1 < self._player_ct <= len(self._colors))

        self._current_turn = 0
        
        self._mouse_zones = []
        for row in range(self._row_ct):
            self._mouse_zones.append([])
            for col in range(self._column_ct):
                zone = pygame.Rect(
                    self.grid_to_px(pygame.math.Vector2(col, row)) - pygame.math.Vector2(CIRCLE_RADIUS, CIRCLE_RADIUS),
                    pygame.math.Vector2(CIRCLE_RADIUS, CIRCLE_RADIUS) * 2
                )
                self._mouse_zones[row].append(zone)
        self._hover_zone = pygame.math.Vector2(-1, -1)
        self._clicked_zone = pygame.math.Vector2(-1, -1)

    def update(self, frame_time, mx: int, my: int, m1_released: bool):
        self._hover_zone = pygame.math.Vector2(-1, -1)
        self._clicked_zone = pygame.math.Vector2(-1, -1)

        for row in range(self._row_ct):
            for col in range(self._column_ct):
                # if hovering over current mouse zone...
                if self._mouse_zones[row][col].collidepoint(mx, my):
                    # ...set the hover zone to the current click zone
                    self._hover_zone = pygame.math.Vector2(col, row)
                    # if left click was released ...
                    if m1_released:
                        # ...set the clicked zone as current mouse zone...
                        self._clicked_zone = pygame.math.Vector2(col, row)
                        #...and put a chip there
                        self.place_chip(col, row)

    def draw(self, screen):
        for row in range(self._row_ct):
            for col in range(self._column_ct):
                circ_center = self.grid_to_px(pygame.math.Vector2(col, row))
                circ_color = COLOR_WHITE
                if col == self._clicked_zone.x and row == self._clicked_zone.y:
                    circ_color = COLOR_CYAN
                elif self._chips[row][col] is not None:
                    circ_color = self._colors[self._chips[row][col]]
                pygame.draw.circle(screen, circ_color, circ_center, CIRCLE_RADIUS)

                rect_line_width = 1
                if col == self._hover_zone.x and row == self._hover_zone.y:
                    rect_line_width = 3
                pygame.draw.rect(screen, COLOR_RED, self._mouse_zones[row][col], width=rect_line_width)

    '''Given the x,y grid pos returns x,y pixel coords of center of grid space'''
    def grid_to_px(self, grid_pos: pygame.math.Vector2) -> pygame.math.Vector2:
        return pygame.math.Vector2(
            (CIRCLE_RADIUS + X_EDGE_SPACING) + grid_pos.x * (CIRCLE_RADIUS * 2 + X_CIRCLE_SPACING),
            (CIRCLE_RADIUS + Y_EDGE_SPACING) + grid_pos.y * (CIRCLE_RADIUS * 2 + Y_CIRCLE_SPACING),
        )

    def place_chip(self, chip_grid_x: int, chip_grid_y: int):
        assert(0 <= chip_grid_x < self._column_ct)
        assert(0 <= chip_grid_y < self._row_ct)
        self._chips[chip_grid_y][chip_grid_x] = self._current_turn
        self._turn_rotation()

    def _turn_rotation(self)-> None:
        self._current_turn += 1
        if self._current_turn >= self._player_ct:
            self._current_turn = 0