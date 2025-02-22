marker1="x" #marker player 1 will use
marker2="o" #marker player 2 will use
empty="*"

my_turn=marker1 #player whos turn it is
game_over=False #if someone wins or its a tie this will be true

grid=[empty,empty,empty,empty,empty,empty,empty,empty,empty]

def print_grid(_grid):
    #shows grid
    print(f"{_grid[0]} | {_grid[1]} | {_grid[2]}")
    print("---------")
    print(f"{_grid[3]} | {_grid[4]} | {_grid[5]}")
    print("---------")
    print(f"{_grid[6]} | {_grid[7]} | {_grid[8]}")

def take_your_turn(_marker1,_marker2,_my_turn,_grid):
    while True:
        #asks where you want to place the marker and waits for response
        choice=input("where would you like to place your marker? ")
        index=int(choice) #converts choice from string to int
        #make sure index is in an acceptable range
        assert 0<=index
        assert index<=8
        # (in other words) if the chosen spot is empty
        if _grid[index]!=_marker1 and _grid[index]!=_marker2:
            break # continue playing the game
        else:
            print("spot already taken")
            continue

    _grid[index]=_my_turn #place marker on the board
    return _grid

def convert(h,v):
    return v*3+h

def get_from_grid(h,v):
    return grid[convert(h,v)]

def detect_win(_grid,_my_turn):
    #column 1
    if _grid[0]==_my_turn and _grid[3]==_my_turn and _grid[6]==_my_turn:
        return True
    #column 2
    elif _grid[1]==_my_turn and _grid[4]==_my_turn and _grid[7]==_my_turn:
        return True
    #column 3
    elif _grid[2]==_my_turn and _grid[5]==_my_turn and _grid[8]==_my_turn:
        return True
    #row 1
    elif _grid[0]==_my_turn and _grid[1]==_my_turn and _grid[2]==_my_turn:
        return True
    #row 2
    elif _grid[3]==_my_turn and _grid[4]==_my_turn and _grid[5]==_my_turn:
        return True
    #row 3
    elif _grid[6]==_my_turn and _grid[7]==_my_turn and _grid[8]==_my_turn:
        return True
    #diagonal 1
    elif _grid[0]==_my_turn and _grid[4]==_my_turn and _grid[8]==_my_turn:
        return True
    #diagonal 2
    elif _grid[2]==_my_turn and _grid[4]==_my_turn and _grid[6]==_my_turn:
        return True
    else:
        return False
    
while True:
    print(f"it is currently {my_turn}'s turn")#print stuff

    print_grid(grid)

    grid=take_your_turn(marker1,marker2,my_turn,grid)

    if detect_win(grid, my_turn)==True:
        print(f"player {my_turn} won")
        print_grid(grid)
        game_over=True
    else:
        board_is_full=True
        for index in range(9):
            if grid[index]==empty:
                board_is_full=False
        if board_is_full==True:
            game_over=True
            print("the board is full")
  
    #sets next players turn
    if my_turn==marker1:
        my_turn=marker2
    elif my_turn==marker2:
        my_turn=marker1

    if game_over==False:
        continue
    else:
        break
