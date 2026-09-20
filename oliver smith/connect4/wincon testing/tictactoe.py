import random

board = []
board_size = 4

for y in range(board_size):
    board.append([])
    for x in range(board_size):
        board[y].append(random.choice(['x', 'o', None]))

is_win = random.choice([0, 1]) == 1
if is_win:
    hv = random.choice(['h','v'])
    i = random.randint(0, board_size - 1)
    if hv == 'h':
        for x in range(board_size):
            board[i][x] = 'w'
    elif hv == 'v':
        for y in range(board_size):
            board[y][i] = 'w'

for y in range(len(board)):
    print('[', end='\t')
    for x in range(len(board[y])):
        print(board[y][x], end='\t')
    print(']')

# check for a win across an entire row
def h_win() -> bool:
    for y in range(len(board)):
        # check for a win in row #y
        win = True
        for x in range(len(board[y]) - 1):
            # check if the cell at (x,y) is different from the cell to its right [aka, (x+1,y)]
            if board[y][x] != board[y][x+1] or board[y][x] is None:
                win = False
        # if we've found a win, stop checking and just report a win
        if win:
            return win
    return False

# check for a win with only 3 in a row
def h_win3() -> bool:
    for y in range(len(board)):
        for x in range(len(board[y]) - board_size):
            if board[y][x] is not None:
                marker = board[y][x]
                win = True
                for xm in range(1,3):
                    if board[y][x + xm] != marker:
                        win = False
                        break
                if win:
                    return win
    return False

# check for a win along an entire column
def v_win() -> bool:
    for x in range(len(board[0])):
        # check for a win in column #x
        win = True
        for y in range(len(board) - 1):
            # check if the cell at (x,y) is different from the cell below it [aka, (x,y+1)]
            if board[y][x] != board[y+1][x]:
                win = False
        # if we've found a win, stop checking and just report a win
        if win:
            return win
    return False

def bs_win() -> bool:
    pass

def fs_win() -> bool:
    pass

print(f'horizontal win? {h_win()}')
print(f'horizontal win of 3? {h_win3()}')
print(f'vertical win? {v_win()}')
# print(f'backslash win? {bs_win()}')
# print(f'forwardslash win? {fs_win()}')