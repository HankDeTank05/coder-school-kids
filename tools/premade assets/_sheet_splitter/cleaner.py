# language imports
import os.path

# package imports
from PIL import Image

# project imports
import common

current = os.getcwd() # get the current folder
if not os.path.isabs(current): # if the path of the current folder is not an absolute path...
    current = os.path.abspath(current) # ...make it absolute
print(current) # TODO: remove temp code
current = os.path.split(current)[0] # go up one folder
print(current) # TODO: remove temp code

# current = os.path.join(current, "platformer", "playable characters", "mario series", "mario", "world_sheet.png")
current = os.path.join(current, "platformer", "playable characters", "samus", "og_sheet.png")
print(current)

image = common.open_image(current)
going = True

pixels = common.get_pixels(image)

new_image = None
new_filename = os.path.split(current)[1]
new_filename = new_filename.split(".")[0] + "_cleaned." + new_filename.split(".")[1]
new_image_path = os.path.split(current)[0] + new_filename
print(f"the cleaned image will be saved at the following path:\n{new_image_path}")

while going:
    print("What color should be replaced?")
    # original = common.type_rgba()
    original, original_pos = common.select_color(current)
    
    print("What color should it be replaced with?")
    # replacement = common.type_rgba()
    replacement, replacement_pos = common.select_color(current)

    response = input("replace adjacent only?")
    if "y" in response.lower():
        print(f"Replacing adjacent {original} with {replacement}...")
        common.replace_color_adjacent(pixels, original, replacement, original_pos)
    elif "n" in response.lower():
        print(f"Replacing {original} with {replacement}...")
        common.replace_color(pixels, original, replacement)
    else:
        assert(False)
    print("Done!")

    new_image = common.pixels_to_image(pixels)
    new_image.save(new_image_path)
    current = new_image_path

    response = input("Keep going? ")
    if "y" in response.lower():
        going = True
    elif "n" in response.lower():
        going = False
    else:
        assert(False)

new_image.show()

'''
colors to be replaced
(88, 168, 240, 255)
(0, 84, 84, 255)
(0, 52, 52, 255)
(0, 66, 66, 255)
(0, 20, 20, 255)

(0, 148, 148, 255)
'''
