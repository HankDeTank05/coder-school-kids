# language imports
import os.path
import random

# package imports
from PIL import Image
import pygame

def open_image(abs_path: str) -> Image:
    assert(os.path.isabs(abs_path))
    assert(os.path.exists(abs_path))
    assert(os.path.isfile(abs_path))
    image = Image.open(abs_path)
    return image

def replace_color(pixels: list[list[tuple[int, int, int, int]]], original_color: tuple[int, int, int, int], replacement_color: tuple[int, int, int, int]) -> None:
    for y in range(len(pixels)):
        for x in range(len(pixels[y])):
            if pixels[y][x] == original_color:
                pixels[y][x] = replacement_color

def replace_color_adjacent(pixels: list[list[tuple[int, int, int, int]]], original_color: tuple[int, int, int, int], replacement_color: tuple[int, int, int, int], original_pos: tuple[int, int]) -> None:
    assert(pixels[original_pos[1]][original_pos[0]] == original_color)
    replaced = []
    queue = [original_pos]
    while len(queue) > 0:
        pos = queue.pop(0)
        x = pos[0]
        y = pos[1]
        pixels[y][x] = replacement_color
        replaced.append(pos)
        nbors = [ (x-1,y), (x+1,y), (x,y-1), (x,y+1) ]
        for nbor in nbors:
            nbor_x = nbor[0]
            nbor_y = nbor[1]
            if pixels[nbor_y][nbor_x] == original_color:
                queue.append(nbor)

def get_pixels(image: Image) -> list[list[tuple[int, int, int, int]]]:
    pixels: list[list[tuple]] = []
    width: int = image.size[0]
    height: int = image.size[1]
    for y in range(height):
        pixels.append([])
        for x in range(width):
            pixel = image.getpixel([x, y])
            assert(type(pixel) == tuple)
            if len(pixel) == 3:
                pixel = (pixel[0], pixel[1], pixel[2], 255)
            elif len(pixel) != 4:
                print(pixel)
            pixels[y].append(pixel)
    return pixels

def pixels_to_image(pixels: list[list[tuple[int, int, int, int]]]) -> Image.Image:
    pixels_1d = []
    for y in range(len(pixels)):
        for x in range(len(pixels[y])):
            # print(pixels[y][x])
            if type(pixels[y][x]) != tuple:
                print(type(pixels[y][x]))
            # assert(type(pixels[y][x]) == tuple)
            pixels_1d.append(pixels[y][x])
    # print(pixels_1d)
    image = Image.new("RGBA", (len(pixels[0]), len(pixels)))
    image.putdata(pixels_1d)
    return image

def select_color(image_path: str):
    assert(os.path.exists(image_path))
    assert(os.path.isabs(image_path))
    assert(os.path.isfile(image_path) == True)

    image = pygame.image.load(image_path)

    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((image.get_width(), image.get_height()))
    clock = pygame.time.Clock()
    running = True

    # left mouse button states
    m1_prev = False # current frame
    m1_curr = False # previous frame
    clicked_pos = None

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        ##########
        # UPDATE #
        ##########
        m1_curr = pygame.mouse.get_pressed()[0] # get the current state of the left mouse button
        if m1_curr == True and m1_prev == False:
            selected_color = image.get_at(pygame.mouse.get_pos())
            clicked_pos = pygame.mouse.get_pos()
            print(selected_color)
            running = False

        ########
        # DRAW #
        ########
        screen.blit(image, (0, 0))

        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

        # prep for next frame
        m1_prev = m1_curr

    pygame.quit()

    return pygame_color_to_tuple(selected_color), clicked_pos

def pygame_color_to_tuple(pg_color: pygame.color.Color) -> tuple[int, int, int, int]:
    return (pg_color.r, pg_color.g, pg_color.b, pg_color.a)

def type_rgba() -> tuple[int, int, int, int]:
    return (int(input("r: ")), int(input("g: ")), int(input("b: ")), int(input("a: ")))

def select_rects(image_path: str, rects: list[pygame.Rect]) -> list[pygame.Rect]:
    assert(os.path.exists(image_path))
    assert(os.path.isabs(image_path))
    assert(os.path.isfile(image_path) == True)

    image = pygame.image.load(image_path)

    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((image.get_width(), image.get_height()))
    clock = pygame.time.Clock()
    running = True

    # selection setup
    selected = []
    for rect in rects:
        selected.append(False)
    m1_curr = False
    m1_prev = False

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0,0,0,255))

        ##########
        # UPDATE #
        ##########
        m1_curr = pygame.mouse.get_pressed()[0]

        ########
        # DRAW #
        ########
        # screen.blit(image, rects[rect_i].topleft, rects[rect_i])
        screen.blit(image, (0, 0))
        for i in range(len(rects)):
            rect = rects[i]
            if rect.collidepoint(pygame.mouse.get_pos()):
                draw_color = (0, 0, 255)
                if m1_curr and not m1_prev:
                    selected[i] = not selected[i]
            elif selected[i]:
                draw_color = (0, 255, 0)
            else:
                draw_color = (255, 0, 0)
            pygame.draw.rect(screen, (0,0,0), rect, width=3)
            pygame.draw.rect(screen, draw_color, rect, width=1)

        #######################
        # PREP FOR NEXT FRAME #
        #######################
        m1_prev = m1_curr

        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

    pygame.quit()

def show_pixels(image_path: str, groups: list[list[tuple[int, int]]]) -> None:
    assert(os.path.exists(image_path))
    assert(os.path.isabs(image_path))
    assert(os.path.isfile(image_path) == True)

    image = pygame.image.load(image_path)

    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((image.get_width(), image.get_height()))
    clock = pygame.time.Clock()
    running = True

    colors = []
    for group_i in range(len(groups)):
        while True:
            color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            if color not in colors:
                colors.append(color)
                break
            else:
                continue
    assert(len(colors) == len(groups))

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        ##########
        # UPDATE #
        ##########

        ########
        # DRAW #
        ########
        screen.blit(image, (0, 0))
        for gi in range(len(groups)):
            group = groups[gi]
            for pixel in group:
                x = pixel[0]
                y = pixel[1]
                pygame.draw.rect(screen, colors[gi], pygame.Rect(x, y, 1, 1))

        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

    pygame.quit()