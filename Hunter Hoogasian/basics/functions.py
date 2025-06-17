# define a function called say_hello
# parameters: none
# return value: none
def say_hello() -> None:
    print("Hello")

# We call functions by typing their name followed by parentheses
say_hello()

x_pos: int = 247
y_pos: int = 771

# Define a funcation called print_coords
# Parameters: 
# - x = the X component of the coord 
# - y = the Y compenent of the coord
# return value: none
def print_coords(x: int | float, y: int | float) -> None: 
    print(f"({x}, {y})")

print_coords(x_pos, y_pos)
print_coords(.1, .2)
print_coords(1, 2.2)

# what does return do?
# 
def combine(first_name: str, last_name: str) -> str:
    combination: str = f"{first_name} {last_name}"
    print(combination)
    return combination

full_name = combine("Bob", "Spoke")
print(full_name)

# what's happening here? (in order)
# 1. Concatenate BOB and B
# 2. Combine function does it's thing (and returns a string)
# 3. print function does its thing (the value retured by the combine function is printed)
print(combine("BOB" + "B", "BOB"))

# what's happening here? (in order)
# 1. say_hello function does its thing (Prints the word "Hello")
# 2. Print function does its thing (The value that is returned by the say_hello function is printed)
print(say_hello())

