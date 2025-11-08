import random

wall = "#"
space = " "

def char_to_cell(char_i: int) -> int:
    assert(char_i % 2 == 1)
    return (char_i - 1) // 2

def cell_to_char(cell_i: int) -> int:
    return cell_i * 2 + 1

cell_size = 10
char_size = cell_to_char(cell_size)

maze = []

for y in range(char_size):
    maze.append([]) # add an empty row to the maze

    # populate the row with wall characters
    for x in range(char_size):
        if x%2 == 1 and y%2 == 1:
            maze[y].append(space)
        else:
            maze[y].append(wall)
        print(maze[y][x], end=" ")
    
    print()

visited_data = []

for y in range(cell_size):
    visited_data.append([]) # add an empty row to the visited data grid

    # populate the row with "false" (which means it's not visited)
    for x in range(cell_size):
        visited_data[y].append(False)
        print(visited_data[y][x], end=" ")

    print()

# 1. Choose a starting cell
def maze_gen_recursive(char_x: int, char_y: int):
    # assert() has to be true or it crashes
    assert(char_x % 2 == 1) # checking if x is odd (will crash if not)
    assert(char_y % 2 == 1) # checking if y is odd (will crash if not)
    # 2. Mark the current cell as visited
    visited_data[char_to_cell(char_y)][char_to_cell(char_x)] = True

    unvisited_nbors = []

    if char_x != 1: # check if we are not in the west most edge
        #check west neighbor
        if visited_data[char_to_cell(char_y)][char_to_cell(char_x - 2)] == False:
            unvisited_nbors.append((char_x - 2, char_y))
    if char_x != char_size - 2: # check if we are not in the east most edge
        #check east neigbor
        if visited_data[char_to_cell(char_y)][char_to_cell(char_x + 2)] == False:
            unvisited_nbors.append((char_x + 2, char_y))

    if char_y != 1: # check if we are not in the north most edge
        #check north neighbor
        if visited_data[char_to_cell(char_y - 2)][char_to_cell(char_x)] == False:
            unvisited_nbors.append((char_x, char_y - 2))
    if char_y != char_size - 2: # check if we are not in the south most edge
        #check south neighbor
        if visited_data[char_to_cell(char_y + 2)][char_to_cell(char_x)] == False:
            unvisited_nbors.append((char_x, char_y + 2))

    # 3. While the current cell has any unvisited neighbor cells
    if len(unvisited_nbors) >= 1:
        # 3.1 Choose one of the unvisited neighbors
        random_unvisited_nbor = random.choice(unvisited_nbors)
        nbor_x = random_unvisited_nbor[0]
        nbor_y = random_unvisited_nbor[1]

        # 3.2 Remove the wall between the current cell and the chosen cell
        wall_x = (char_x + nbor_x) // 2
        wall_y = (char_y + nbor_y) // 2
        assert(maze[wall_y][wall_x] == wall)
        maze[wall_y][wall_x] = space

        # 3.3 Invoke the routine recursivly for the chosen cell
        maze_gen_recursive(nbor_x, nbor_y)

maze_gen_recursive(1,1)

for row in maze:
    for cell in row:
        print(cell, end=" ")
    print()