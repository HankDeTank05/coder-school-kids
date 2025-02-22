playerX = "X"
playerO = "O"
empty = " "
my_turn = playerO

board = []

print(len(board))

for i in range(9):
    #print(i)
    board.append(empty)

print(len(board))

print(f"player {my_turn} will go first")

def clear_board():
    for i in range(9):
        board[i] = empty

def winnerr():
    if winnerr_helper(2,4,6):
        print("win in / !")
        return "win"
    elif winnerr_helper(0,3,6):
        print("win in column 1!")
        return "win" 
    elif winnerr_helper(0,4,8):
        print("win in \ !")
        return "win"
    elif winnerr_helper(1,4,7):
        print("win in column 2!")
        return "win"
    elif winnerr_helper(2,5,8):
        print("win in column 3!")
        return "win"
    elif winnerr_helper(0,1,2):
        print("win in row 1!")
        return "win"
    elif winnerr_helper(3,4,5):
        print("win in row 2!")
        return "win"
    elif winnerr_helper(6,7,8):
        print("win in row 3!")
        return "win"
    elif board[0] != empty and board[1] != empty and board[2] != empty and board[3] != empty and board[4] != empty and board[5] != empty and board[6] != empty and board[7] != empty and board[8] != empty:
        return "cats" #MEOW
    else:
        return "thermostat" 
    

def winnerr_helper(_indexA, _indexB, _indexC):
    if board[_indexA] != empty and board[_indexB] != empty and board[_indexC] != empty and board[_indexA] == board[_indexC] and board[_indexA] == board[_indexB]:
        return True
    else:
        return False

while True:
    #step one print stuff
    
    print(f"it is currently {my_turn}'s turn")

    #empty is equal to a space
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print(f"-+-+-")
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print(f"-+-+-")
    print(f"{board[6]}|{board[7]}|{board[8]}")

    #step two place marker
    
    response = input("where do you want your marker? (choose a number 1-9). ")
    index = int(response)
    print(index)
    if 1 <= index <= 9: # checking if the number that was put in is between 0 and 8
        if board[index-1] != empty:
            print (" You can't steal a space from the other player. You have now lost your turn. HA HA HA!")
        else:
            board[index-1] = my_turn # places marker on board
    elif index < 1:
        print ("The number you put in was invalid because it was too low. You lost your turn.")
    elif index > 9:
        print ("The number you put in was invalid because it was too high. You lost your turn.")

    #step three (part one) check for win

    # code goes here
    status = winnerr()
    if status == "win":
        print(f"Player {my_turn} has officially unofficially won this round of Mean Tac Toe!")
        clear_board()
    elif status == "thermostat":
        pass
    elif status == "cats":
        print("Unfourtunately, no one has won this round of Mean Tac Toe!")
        clear_board()
    
    #step three (part two) change turn
    
    if my_turn == playerX: # == means check if it's equal to
        my_turn = playerO
    elif my_turn == playerO:
        my_turn = playerX
