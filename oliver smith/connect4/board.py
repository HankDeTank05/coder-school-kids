import pygame
from constants import *


class Board:
    _column_ct: int # how many columns there are on the board
    _row_ct: int # how many rows there are on the board
    _chips: list[list[None | int]]
    _colors: list[pygame.Color]
    _color_names: list[str]
    _player_ct: int
    _current_turn: int
    _win_value: int | None


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
            COLOR_BLUE,
            COLOR_GOLDENROD,
            COLOR_CORAL_RED,
            COLOR_ORANGE,
            COLOR_CYAN,
            COLOR_BLACK
        ]
        self._color_names = [
            'Red',
            'Yellow',
            'Green',
            'Blue',
            'Gold',
            'Coral',
            'Orange',
            'Cyan',
            'Black'
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
        self._win_value = self.check_for_win()
        self._hover_zone = pygame.math.Vector2(-1, -1)
        self._clicked_zone = pygame.math.Vector2(-1, -1)
        if self._win_value is None:

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
        else:
            pass

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
        if self._win_value is not None:
            text_surf = FONT.render(f'{self._color_names[self._win_value]} team wins'.upper(), False, COLOR_BLACK)
            text_rect = text_surf.get_rect()
            text_rect.center = (WIDTH // 2, HEIGHT // 2)
            pygame.draw.rect(screen, COLOR_WHITE, text_rect)
            screen.blit(text_surf, text_rect)

    def grid_to_px(self, grid_pos: pygame.math.Vector2) -> pygame.math.Vector2:
        '''Given the x,y grid pos returns x,y pixel coords of center of grid space'''
        return pygame.math.Vector2(
            (CIRCLE_RADIUS + X_EDGE_SPACING) + grid_pos.x * (CIRCLE_RADIUS * 2 + X_CIRCLE_SPACING),
            (CIRCLE_RADIUS + Y_EDGE_SPACING) + grid_pos.y * (CIRCLE_RADIUS * 2 + Y_CIRCLE_SPACING),
        )

    def place_chip(self, placed_grid_x: int, placed_grid_y: int):
        assert(0 <= placed_grid_x < self._column_ct)
        assert(0 <= placed_grid_y < self._row_ct)
        '''
        if a piece has been placed at (x,y)...
        then increase the y coord until...
            the piece hits the bottom row coord on the board (ROW_COUNT - 1)
                                    current_grid_y == self._row_ct - 1
        '''
        current_grid_x = placed_grid_x
        current_grid_y = placed_grid_y
        while current_grid_y < self._row_ct - 1 and self._chips[current_grid_y + 1][current_grid_x] is None:
            current_grid_y += 1
        self._chips[current_grid_y][current_grid_x] = self._current_turn
        # self._chips[placed_grid_y][placed_grid_x] = self._current_turn
        self._turn_rotation()

    def _turn_rotation(self)-> None:
        self._current_turn += 1
        if self._current_turn >= self._player_ct:
            self._current_turn = 0

    def check_for_win(self) -> int | None:
        win_value = self._check_horizontal_win()
        if win_value is not None:
            return win_value
        win_value = self._check_vertical_win()
        if win_value is not None:
            return win_value
        win_value = self._check_bslash_win()
        if win_value is not None:
            return win_value
        win_value = self._check_fslash_win()
        return win_value
        

    def _check_horizontal_win(self) -> int | None:
        '''checks for a horizontal win. returns either None, or the number of the team a win has been detected for'''
        for y in range(len(self._chips)):
            # check for a win in row #y
            for x in range(len(self._chips[y]) - MIN_WIN_LENGTH + 1):
                # don't check for win if there is no marker
                if self._chips[y][x] is not None:
                    chip = self._chips[y][x] # checking which team placed chip at x,y
                    win = True
                    # check if there are MIN_WIN_LENGTH-1 consecutive of the same chip to the right
                    for dx in range(1, MIN_WIN_LENGTH):
                        if self._chips[y][x + dx] != chip:
                            win = False
                            break
                    # if there is a win, stop checking and tell the system someone won
                    if win:
                        return chip
        return None

    def _check_vertical_win(self) -> int | None:
        '''checks for a vertical win. returns either None, or the number of the team a win has been detected for'''
        for x in range(len(self._chips[0])):
            # check for a win in column #x
            for y in range(len(self._chips) - MIN_WIN_LENGTH + 1):
                # don't check for win if there is no chip
                if self._chips[y][x] is not None:
                    chip = self._chips[y][x]
                    win = True
                    # check if there are MIN_WIN_LENGTH-1 consecutive of the same marker below
                    for dy in range(1, MIN_WIN_LENGTH):
                        if self._chips[y + dy][x] != chip:
                            win = False
                            break
                    # if there is a win, stop checking and tell the system someone won
                    if win:
                        return chip
        return None

    def _check_bslash_win(self) -> int | None:
        '''checks for a diagonal backslash win. returns either None, or the number of the team a win has been detected for'''
        # pick a start-x and start-y only from possible top-left-most chip spots
        for sy in range(len(self._chips) - MIN_WIN_LENGTH + 1):
            for sx in range(len(self._chips[sy]) - MIN_WIN_LENGTH + 1):
                if self._chips[sy][sx] is None:
                    continue # don't even attempt to check diagonally adjacent spaces, because there's no marker there
                chip = self._chips[sy][sx]
                consecutive = 1 # keep track of how many consecutive chips there are
                for di in range(1, MIN_WIN_LENGTH):
                    if self._chips[sy][sx] != self._chips[sy + di][sx + di]:
                        break # if one chip in the diagonal isn't the same, don't bother checking the rest
                    else:
                        consecutive += 1 # a consecutive chip was found, so increase the consecutive counter
                if consecutive >= MIN_WIN_LENGTH:
                    return chip # if the consecutive counter is equal to the specified win length (aka, MIN_WIN_LENGTH) then stop checking and report a win
        return None

    def _check_fslash_win(self) -> int | None:
        '''checks for a diagonal forward-slash win. returns either None, or the number of the team a win has been detected for'''
        # pick a start-x and start-y only from possible top-right-most marker spots
        for sy in range(len(self._chips) - MIN_WIN_LENGTH + 1):
            for sx in range(MIN_WIN_LENGTH - 1,len(self._chips[sy])):
                if self._chips[sy][sx] is None:
                    continue # don't even attempt to check diagonally adjacent spaces, because there's no marker there
                chip = self._chips[sy][sx]
                consecutive = 1 # keep track of how many consecutive markers there are
                for di in range(1,MIN_WIN_LENGTH):
                    if self._chips[sy][sx] != self._chips[sy + di][sx - di]:
                        break # if one marker in the diagonal isn't the same, don't bother checking the rest
                    else:
                        consecutive += 1 # a consecutive marker was found, so increase the consecutive counter
                if consecutive >= MIN_WIN_LENGTH:
                    return chip # if the consecutive counter is equal to the specified win length (aka, MIN_WIN_LENGTH) then stop checking and report a win
        return None

    # TODO: check for \backslash\ wins

    # TODO: check for /fwdslash/ wins