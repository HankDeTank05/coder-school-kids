import pygame


pygame.font.init()
TEXT_FONT = pygame.font.Font(size=32)

WIDTH=1280
HEIGHT=720
SCREEN_RECT=pygame.Rect(0, 0, WIDTH, HEIGHT)

BACKGROUND_COLOR = pygame.Color('skyblue')

SNAKE_HEAD_COLOR = pygame.Color('orchid4')
SNAKE_TAIL_COLOR = pygame.Color('slateblue1')
SNAKE_FACE_COLOR = pygame.Color('orchid')

FOOD_COLORS = [
    pygame.Color('mistyrose2'),
    pygame.Color('salmon1'),
    pygame.Color("chocolate"),
    pygame.Color('plum'),
    pygame.Color('peachpuff'),
    pygame.Color('aliceblue'),
    pygame.Color('honeydew'),
    pygame.Color('lime'),
    pygame.Color('olive'),
    pygame.Color('orange'),
    pygame.Color('tomato'),
    pygame.Color('mediumpurple'),
    pygame.Color('gold')
]

LENGTH_TO_WIN = 1000
STARTING_FOOD_COUNT_MAX = LENGTH_TO_WIN * 5
STARTING_FOOD_COUNT_MIN = LENGTH_TO_WIN
CPU_SNAKE_STARTING_LENGTH = 50

PROGRESS_BAR_WIDTH=13