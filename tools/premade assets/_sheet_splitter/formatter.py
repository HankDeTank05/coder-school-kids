# language imports
import os
import random
import sys

# package imports
from PIL import Image
import pygame

# program imports
from selector import select_color
import common

# colors to use
TRANSPARENT = (0, 0, 0, 0)
RED = (255, 0, 0, 255)
BLACK = (0, 0, 0, 255)
WHITE = (255, 255, 255, 255)

def get_random_unique_color(colors_to_avoid):
    # NOTE: we create it as a list so new values can be assigned to them
    random_color = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), 255]

    # make sure the replacement sheet background color is not found in the original spritesheet
    while random_color[0:3] in original_colors:
        for i in range(3):
            random_color[i] = random.randint(0, 255)

    # convert it to a tuple so no changes can be made
    random_color = tuple(random_color)

    return random_color

def replace_print(output):

    #cursor up one line
    sys.stdout.write('\x1b[1A')

    #delete last line
    sys.stdout.write('\x1b[2K')

    print(output)



current = os.path.dirname(os.path.abspath(__file__)) # get the current folder
if not os.path.isabs(current): # if the path of the current folder is not an absolute path...
    current = os.path.abspath(current) # ...make it absolute
print(current) # TODO: remove temp code
current = os.path.split(current)[0] # go up one folder
print(current) # TODO: remove temp code

# TODO: remove temp code below
# current = os.path.join(current, "platformer", "playable characters", "mario series", "mario", "2usa_sheet.png")
# current = os.path.join(current, "platformer", "playable characters", "samus", "og_sheet_cleaned.png")
# current = os.path.join(current, "platformer", "playable characters", "samus", "super_sheet_cleaned.png")
# current = os.path.join(current, "platformer", "playable characters", "mario series", "mario", "world_sheet_cleaned.png")
# current = os.path.join(current, "platformer", "playable characters", "mega man", "mm1_megaman_sheet.png")
current = os.path.join(current, "rpg", "deltarune", "kris_3_4.png")
# current = os.path.join(current, "rpg", "kris_1_2.png")
# current = os.path.join(current, "platformer", "playable characters", "mario series", "mario maker", "costumes.png")

print(current)
assert(os.path.exists(current) == True)
image = Image.open(current)
print(f"Format: {image.format}")
print(f"Size: {image.size}")
print(f"Mode: {image.mode}")
#image.show()
# TODO: remove temp code above

pixel_data = []

print("Select the sheet background color")
sheet_bg_color = select_color(current) # get the sheet background color by clicking on it
sheet_bg_color = (sheet_bg_color.r, sheet_bg_color.g, sheet_bg_color.b, sheet_bg_color.a) # convert from pygame color to RGBA 4-tuple

print("Select the sprite background color")
sprite_bg_color = select_color(current) # get the sprite background color by clicking on it
sprite_bg_color = (sprite_bg_color.r, sprite_bg_color.g, sprite_bg_color.b, sprite_bg_color.a) # convert from pygame color to RGBA 4-tuple

###########################################################
# get a list of unique colors in the original spritesheet #
###########################################################
print("Getting unique colors from original sheet...")
print()
original_colors = []
size = image.size[1]
for y in range(image.size[1]):
    for x in range(image.size[0]):
        current_pixel = image.getpixel([x, y])
        if len(current_pixel) == 3:
            current_pixel = (current_pixel[0], current_pixel[1], current_pixel[2], 255)
        if current_pixel not in original_colors:
            original_colors.append(current_pixel)
            # print(f"\t{current_pixel}")

    replace_print(f"{int(y/size*100)}%")
replace_print("100%")

# create a random opaque color to replace the sheet background color with
sheet_bg_replace = get_random_unique_color(original_colors)

print(f"Sheet background color {sheet_bg_color} will be replaced with {sheet_bg_replace}")
print(f"Sprite background color {sprite_bg_color} will be made transparent")
print()

# new (2D) array of pixels
new_pixels = []

#########################################################
# replace sheet background and sprite background colors #
#########################################################
for y in range(image.size[1]):
    new_pixels.append([])
    for x in range(image.size[0]):
        current_pixel = image.getpixel([x, y])
        color_vals = len(current_pixel)
        # print(f"{current_pixel}\t/\t{sprite_bg_color}")

        # replace the sheet background color with opaque red
        if (color_vals == 3 and current_pixel == sheet_bg_color[0:3]) or (color_vals == 4 and current_pixel == sheet_bg_color):
            new_pixels[y].append(sheet_bg_replace)

        # replace the sprite background color with the transparent color
        elif (color_vals == 3 and current_pixel == sprite_bg_color[0:3]) or (color_vals == 4 and current_pixel == sprite_bg_color):
            new_pixels[y].append(TRANSPARENT) # make sprite background color transparent

        # keep any other color the same
        else:
            if color_vals == 3:
                new_pixels[y].append((current_pixel[0], current_pixel[1], current_pixel[2], 255))
            else:
                new_pixels[y].append(current_pixel)

    replace_print(f"{int(y/size*100)}%")
replace_print("100%")

##########################################
# outline sprites with a new third color #
##########################################
sprite_outline_color = get_random_unique_color(original_colors)

print(f"Outlining sprites...")
print()

# list of pixels colored with sprite outline color
outline_pixels = []

size = len(new_pixels)
for y in range(len(new_pixels)):
    for x in range(len(new_pixels[y])):
        # if the current pixel is the sheet background color
        if new_pixels[y][x] == sheet_bg_replace:
            # and the neighboring pixel is either transparent or a sprite color
            is_left_edge = x == 0
            is_right_edge = x == len(new_pixels[y]) - 1
            is_top_edge = y == 0
            is_bottom_edge = y == len(new_pixels) - 1

            if not is_left_edge:
                nbor_pixel_l = new_pixels[y][x-1] # left
            else:
                nbor_pixel_l = None
            
            if not is_right_edge:
                nbor_pixel_r = new_pixels[y][x+1] # right
            else:
                nbor_pixel_r = None
            
            if not is_top_edge:
                nbor_pixel_a = new_pixels[y-1][x] # above
            else:
                nbor_pixel_a = None
            
            if not is_bottom_edge:
                nbor_pixel_b = new_pixels[y+1][x] # below
            else:
                nbor_pixel_b = None

            if not is_left_edge and not is_top_edge:
                nbor_pixel_la = new_pixels[y-1][x-1]
            else:
                nbor_pixel_la = None

            if not is_right_edge and not is_top_edge:
                nbor_pixel_ra = new_pixels[y-1][x+1]
            else:
                nbor_pixel_ra = None

            if not is_left_edge and not is_bottom_edge:
                nbor_pixel_lb = new_pixels[y+1][x-1]
            else:
                nbor_pixel_lb = None

            if not is_right_edge and not is_bottom_edge:
                nbor_pixel_rb = new_pixels[y+1][x+1]
            else:
                nbor_pixel_rb = None
            
            nbor_l_edge = nbor_pixel_l == TRANSPARENT or nbor_pixel_l in original_colors
            nbor_r_edge = nbor_pixel_r == TRANSPARENT or nbor_pixel_r in original_colors
            nbor_a_edge = nbor_pixel_a == TRANSPARENT or nbor_pixel_a in original_colors
            nbor_b_edge = nbor_pixel_b == TRANSPARENT or nbor_pixel_b in original_colors
            nbor_la_corner = nbor_pixel_la == TRANSPARENT or nbor_pixel_la in original_colors
            nbor_ra_corner = nbor_pixel_ra == TRANSPARENT or nbor_pixel_ra in original_colors
            nbor_lb_corner = nbor_pixel_lb == TRANSPARENT or nbor_pixel_lb in original_colors
            nbor_rb_corner = nbor_pixel_rb == TRANSPARENT or nbor_pixel_rb in original_colors

            if nbor_l_edge or nbor_r_edge or nbor_a_edge or nbor_b_edge or nbor_la_corner or nbor_ra_corner or nbor_lb_corner or nbor_rb_corner:
                new_pixels[y][x] = sprite_outline_color
                outline_pixels.append((x, y))

    replace_print(f"{int(y/size*100)}%")
replace_print("100%")

print("Generating pixel groups...")
print()

'''
rects = []

rect_x0 = None
rect_y0 = None
rect_x1 = None
rect_y1 = None
# 1. generate groups of adjacent sprite outline pixels
# 2. get the min and the max (top-left corner, and bottom-right corner)
# 3. ^^that's the rectangle^^
for y in range(len(new_pixels)):
    for x in range(len(new_pixels[y])):
        # if the current pixel is the sprite outline color
        if new_pixels[y][x] == sprite_outline_color:
            # check if the point is inside an already created rectangle
            new_point = True
            for rect in rects:
                if rect.collidepoint(x, y):
                    new_point = False
                    break
            # if the point is not already inside another bounding rectangle
            if new_point:
                print(f"source pixel: {(x, y)}")
                min_x = x
                max_x = x
                min_y = y
                max_y = y
                adjacent = [(x, y)]
                current_x = x
                current_y = y
                while True:
                    nbor_pos = (current_x-1, current_y)
                    if current_x > 0 and new_pixels[current_y][current_x-1] == sprite_outline_color and nbor_pos not in adjacent:
                        # print("adjacent pixel left")
                        adjacent.append(nbor_pos)
                        current_x = nbor_pos[0]
                        current_y = nbor_pos[1]
                        continue

                    nbor_pos = (current_x+1, current_y)
                    if current_x < len(new_pixels[current_y])-1 and new_pixels[current_y][current_x+1] == sprite_outline_color and nbor_pos not in adjacent:
                        # print("adjacent pixel right")
                        adjacent.append(nbor_pos)
                        current_x = nbor_pos[0]
                        current_y = nbor_pos[1]
                        continue

                    nbor_pos = (current_x, current_y-1)
                    if current_y > 0 and new_pixels[current_y-1][current_x] == sprite_outline_color and nbor_pos not in adjacent:
                        # print("adjacent pixel above")
                        adjacent.append(nbor_pos)
                        current_x = nbor_pos[0]
                        current_y = nbor_pos[1]
                        continue

                    nbor_pos = (current_x, current_y+1)
                    if current_y < len(new_pixels)-1 and new_pixels[current_y+1][current_x] == sprite_outline_color and nbor_pos not in adjacent:
                        # print("adjacent pixel below")
                        adjacent.append(nbor_pos)
                        current_x = nbor_pos[0]
                        current_y = nbor_pos[1]
                        continue

                    break
                print(f"adjacent pixel group: {adjacent}")
                for px in adjacent:
                    min_x = min(min_x, px[0])
                    max_x = max(max_x, px[0])
                    min_y = min(min_y, px[1])
                    max_y = max(max_y, px[1])
                rects.append(pygame.Rect(min_x, min_y, max_x - min_x, max_y - min_y))

    # replace_print(f"{y/size*100}%")
# replace_print("100%")

# for rect in rects:
#     print(rect)

common.show_rects(current, rects)
'''

###############################################################
# flood fill pixels until the sprite outline color is reached #
###############################################################
checked = []
checked_count = 0
groups = []
total_pixels = len(new_pixels) * len(new_pixels[0])

pixel_data = []
for y in range(len(new_pixels)):
    pixel_data.append([])
    for x in range(len(new_pixels[y])):
        pixel_data[y].append({
            "checked": False,
            "in stack": False
        })
    assert(len(pixel_data[y]) == len(new_pixels[y]))
assert(len(pixel_data) == len(new_pixels))

for y in range(len(new_pixels)):
    for x in range(len(new_pixels[y])):
        if pixel_data[y][x]["checked"] == False and new_pixels[y][x] != sheet_bg_replace:
            queue = [(x, y)]
            group = []
            while len(queue) > 0:
                pixel = queue.pop(0)
                x = pixel[0]
                y = pixel[1]
                pixel_data[y][x]["in stack"] = False
                if new_pixels[y][x] != sprite_outline_color and pixel not in group:
                    group.append(pixel)
                    assert(pixel not in checked)
                    assert(pixel_data[y][x]["checked"] == False)
                    nbors = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
                    for nbor in nbors:
                        nbor_x = nbor[0]
                        nbor_y = nbor[1]
                        x_in_range = 0 <= nbor_x < len(new_pixels[0])
                        y_in_range = 0 <= nbor_y < len(new_pixels)
                        if x_in_range and y_in_range:
                            # nbor_unchecked = nbor not in checked
                            nbor_unchecked_new = pixel_data[nbor_y][nbor_x]["checked"] == False
                            # assert(nbor_unchecked_new == nbor_unchecked, f"{nbor_unchecked_new} != {nbor_unchecked}")
                            # nbor_unstacked = nbor not in stack
                            nbor_unstacked_new = pixel_data[nbor_y][nbor_x]["in stack"] == False
                            # assert(nbor_unstacked == nbor not in stack, f"{nbor_unstacked_new} != {nbor_unstacked}")
                            if nbor_unchecked_new and nbor_unstacked_new:
                                if new_pixels[nbor_y][nbor_x] != sprite_outline_color:
                                    queue.append(nbor)
                                    pixel_data[nbor_y][nbor_x]["in stack"] = True
                # checked.append(pixel)
                checked_count += 1
                pixel_data[y][x]["checked"] = True
                replace_print(f"group_i={len(groups)} / group={len(group)} / queue={len(queue)} / checked={checked_count} / total={total_pixels} / {int((checked_count / total_pixels) * 100)}%")
                # replace_print(f"{int((checked_count / total_pixels) * 100)}%")
            if len(group) > 0:
                groups.append(group)

new_pixels_1d = []
for y in range(len(new_pixels)):
    for x in range(len(new_pixels[y])):
        new_pixels_1d.append(new_pixels[y][x])

print("showing pixels...")
common.show_pixels(current, groups)

###############################################
# form a bounding rectangle around each group #
###############################################
print("Generating rectangles...")
rects = []
for group in groups:
    min_x = group[0][0]
    max_x = min_x
    min_y = group[0][1]
    max_y = min_y
    for pixel in group:
        x = pixel[0]
        y = pixel[1]
        if x < min_x:
            min_x = x
        elif x > max_x:
            max_x = x
        if y < min_y:
            min_y = y
        elif y > max_y:
            max_y = y
    rects.append(pygame.Rect(min_x, min_y, max_x - min_x + 1, max_y - min_y + 1))

assert(len(rects) == len(groups))
print("Showing rects...")
common.select_rects(current, rects)

sprite_folder = os.path.join(os.path.split(current)[0], os.path.split(current)[1].split(".")[0])
if not os.path.exists(sprite_folder):
    print(f"{sprite_folder} does not exist. Creating it now...")
    os.mkdir(sprite_folder)
    print("Done!")

sprite_n = 0
for rect in rects:
    sprite = Image.new(mode="RGBA", size=rect.size)
    sprite_pixels = []
    for y in range(rect.top, rect.bottom):
        for x in range(rect.left, rect.right):
            color = new_pixels[y][x]
            if color == TRANSPARENT or color in original_colors:
                sprite_pixels.append(new_pixels[y][x])
            else:
                sprite_pixels.append(TRANSPARENT)
    # print(f"pixels = {len(sprite_pixels)}")
    sprite.putdata(sprite_pixels)
    # print("The following sprite is about to be saved...")
    # sprite.show()
    sprite_path = os.path.join(sprite_folder, f"{sprite_n}.png")
    print(f"Saving {sprite_path}...")
    sprite.save(sprite_path)
    print("Done!")
    sprite_n += 1
    # choice = input("Proceed with saving this sprite?")
    # if "y" in choice.lower():
    #     sprite.save(sprite_path)
    # elif "n" in choice.lower():
    #     print("The sprite will not be saved")
    # else:
    #     assert(False)

modded_image = Image.new("RGBA", image.size)
modded_image.putdata(new_pixels_1d)
modded_image.show()
