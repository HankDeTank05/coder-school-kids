import random

board = []
board_size = 4

for y in range(board_size):
    board.append([])
    for x in range(board_size):
        board[y].append(random.choice(['x', 'o', None]))

hvs = random.choice(['h','v', 'bs', 'fs', None])
i = random.randint(0, board_size - 1)
if hvs is None:
    pass
elif hvs == 'h':
    for x in range(board_size):
        board[i][x] = 'w'
elif hvs == 'v':
    for y in range(board_size):
        board[y][i] = 'w'
elif hvs == 'bs':
    for bi in range(board_size):
        board[bi][bi] = 'w'
elif hvs == 'fs':
    for bi in range(board_size):
        board[bi][board_size-bi] = 'w'

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
def h_win_n(n=3) -> bool:
    for y in range(len(board)):
        # check for a win in row #y
        for x in range(len(board[y]) - n + 1):
            # Don't check for win if there is no marker
            if board[y][x] is not None:
                marker = board[y][x] # checking which team placed chip at x,y
                win = True
                # check if the there are n-1 consecutive of the same marker to the right
                for xm in range(1,n):
                    if board[y][x + xm] != marker:
                        win = False
                        break
                # if there is a win stop checking and tell the system someone won
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

def v_win_n(n=3) -> bool:
    for x in range(len(board[0])):
        # check for a win in column #x
        for y in range(len(board) - n + 1):
            # dont check for win if there is no marker
            if board[y][x] is not None:
                marker = board[y][x]
                win = True
                # check if the there are n-1 consecutive of the same marker below
                for ym in range(1,n):
                    if board[y + ym][x] != marker:
                        win = False
                        break
                # if there is a win stop checking and tell the system someone won
                if win:
                    return win
    return False

def bs_win() -> bool:
    for i in range(len(board) - 1):
        if  board[i][i] != board[i+1][i+1]:
            return False
    return True

def fs_win() -> bool:
    for i in range(len(board) - 1):
        if board[i][3-i] != board[i+1][3 - (i+1)]:
            return False
    return True
            

# print(f'horizontal win? {h_win()}')
print(f'horizontal win of n=3? {h_win_n()}')
# print(f'vertical win? {v_win()}')
print(f'vertical win of n=3? {v_win_n()}')
print(f'backslash win? {bs_win()}')
print(f'forwardslash win? {fs_win()}')