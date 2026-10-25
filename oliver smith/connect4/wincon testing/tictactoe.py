import random

board = []
board_size = 5

for y in range(board_size):
    board.append([])
    for x in range(board_size):
        # board[y].append(random.choice(['x', 'o', None]))
        board[y].append(None)

# hvs = random.choice(['h','v', 'bs', 'fs', None])
hvs = 'bs'
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
    length = random.randint(2, board_size)
    max_sx = board_size - length
    max_sy = board_size - length
    sx = random.randint(0, max_sx)
    sy = random.randint(0, max_sy)
    for di in range(length):
        board[sy + di][sx + di] = 'w'
elif hvs == 'fs':
    for bi in range(board_size):
        board[bi][board_size-bi-1] = 'w'


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
        if board[i][i] != board[i+1][i+1]:
            return False
    return True

def bs_win_n(n=3) -> bool:
    # pick a start-x and start-y only from possible top-left-most marker spots
    for sy in range(len(board) - n + 1):
        for sx in range(len(board[sy]) - n + 1):
            if board[sy][sx] is None:
                continue # don't even attempt to check diagonally adjacent spaces, because there's no marker there
            consecutive = 1 # keep track of how many consecutive markers there are
            for di in range(1,n):
                if board[sy][sx] != board[sy + di][sx + di]:
                    break # if one marker in the diagonal isn't the same, don't bother checking the rest
                else:
                    consecutive += 1 # a consecutive marker was found, so increase the consecutive counter
            if consecutive >= n:
                return True # if the consecutive counter is equal to the specified win length (aka, n) then stop checking and report a win
    return False

def fs_win() -> bool:
    for i in range(len(board) - 1):
        if board[i][board_size-1-i] != board[i+1][(board_size-1-i)+1]:
            return False
    return True
            
def fs_win_n(n=3) -> bool:
    # pick a start-x and start-y only from possible top-right-most marker spots
    for sy in range(len(board) - n + 1):
        for sx in range(n - 1, len(board[sy])):
            if board[sy][sx] is None:
                continue # don't even attempt to check diagonally adjacent spaces, because there's no marker there
            consecutive = 1 # keep track of how many consecutive markers there are
            for di in range(1,n):
                if board[sy][sx] != board[sy + di][sx - di]:
                    break # if one marker in the diagonal isn't the same, don't bother checking the rest
                else:
                    consecutive += # a consecutive marker was found, so increase the consecutive counter
            if consecutive >= n:
                return True # if the consecutive counter is equal to the specified win length (aka, n) then stop checking and report a win
    return False


# print(f'horizontal win? {h_win()}')
print(f'horizontal win of n=3? {h_win_n(n=3)}')
# print(f'vertical win? {v_win()}')
print(f'vertical win of n=3? {v_win_n(n=3)}')
# print(f'backslash win? {bs_win()}')
print(f'backslash win of n=3? {bs_win_n(n=3)}')
print(f'forwardslash win? {fs_win()}')