wall = "#"
space = "-"

cell_size = 10
maze_size = cell_size * 2 + 1

maze = []

for y in range(maze_size):
    maze.append([]) # add an empty row to the maze

    # populate the row with wall characters
    for x in range(maze_size):
        maze[y].append(wall)
    
    # print the completed row
    print(maze[y])

# print(maze)


def maze_gen_recursive():
    # 1. Choose a starting cells
    # 2. Mark the current cell as visited
    # 3. While the current cell has any unvisited neighbor cells
        # 3.1 Choose one of the unvisited neighbors
        # 3.2 Remove the wall between the current cell and the chosen cell
        # 3.3 Invoke the routine recursivly for the chosen cell
    pass