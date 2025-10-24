wall = "#"
space = "-"

def char_to_cell(char_i: int) -> int:
    assert(char_i % 2 == 1)
    return (char_i - 1) // 2

def cell_to_char(cell_i: int) -> int:
    return cell_i * 2 + 1

cell_size = 10
maze_size = cell_to_char(cell_size)

maze = []

for y in range(maze_size):
    maze.append([]) # add an empty row to the maze

    # populate the row with wall characters
    for x in range(maze_size):
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
def maze_gen_recursive(x: int, y: int):
    # assert() has to be true or it crashes
    assert(x % 2 == 1) # checking if x is odd (will crash if not)
    assert(y % 2 == 1) # checking if y is odd (will crash if not)
    # 2. Mark the current cell as visited

    # 3. While the current cell has any unvisited neighbor cells
        # 3.1 Choose one of the unvisited neighbors
        # 3.2 Remove the wall between the current cell and the chosen cell
        # 3.3 Invoke the routine recursivly for the chosen cell
    pass