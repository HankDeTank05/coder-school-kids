class Game:

    def __init__(self):
        self.marker1="x"
        self.marker2="o"
        self.board= Board()
        self.my_turn= self.marker1

    def run(self):
        result: str = self.detect_win()
        while True:
            #print stuff
            print(self.board)
            print(self.my_turn)
            
            #take your turn
            self.take_your_turn()
            
            #detect win (no win=change turn)
            result = self.detect_win()
            if result=="no win":
                self.change_turn()
                continue # continue playing game
            else:
                print(self.board)
                print("game over")
                break
        

        print(result)

    def take_your_turn(self):
        while True:
            choice: str =input("where would you like to place your marker? ")
            pos_x: int =None
            pos_y: int =None
            if "top left"==choice:
                pos_x,pos_y=0,0
            elif "top middle"==choice:
                pos_x,pos_y=1,0
            elif "top right"==choice:
                pos_x,pos_y=2,0
            elif "middle left"==choice:
                pos_x,pos_y=0,1
            elif "middle center"==choice:
                pos_x,pos_y=1,1
            elif "middle right"==choice:
                pos_x,pos_y=2,1
            elif "bottom left"==choice:
                pos_x,pos_y=0,2
            elif "bottom middle"==choice:
                pos_x,pos_y=1,2
            elif "bottom right"==choice:
                pos_x,pos_y=2,2
            else:
                print("you've picked an invalid spot. please try again")
                continue
            spot_contents=self.board.get_marker_at_spot(pos_x,pos_y) #Gets marker at the spot you have chosen
            if spot_contents!=self.marker1 and spot_contents!=self.marker2: #checks if spot is empty
                #allowed to put marker on spot
                self.board.place_marker(self.my_turn,pos_x,pos_y) #places marker
                break
            else:
                print("spot is taken. try again")
                continue

    # come back                 
    def detect_win(self)->str:
        #ask board if it is full or not
        win_status: str= "no win"
        checklist: list[list[int]] = [
            [0, 0, 1, 0, 2, 0], #top row
            [0, 1, 1, 1, 2, 1], #middle row
            [0, 2, 1, 2, 2, 2], #bottom row
            [0, 0, 0, 1, 0, 2], #left column
            [1, 0, 1, 1, 1, 2], #middle column
            [2, 0, 2, 1, 2, 2], #right column
            [0, 0, 1, 1, 2, 2], # \ diagonal
            [2, 0, 1, 1, 0, 2] # / diagonal
        ]
        index: int = 0
        while win_status=="no win" and index<len(checklist):
            current_list: list[int]=checklist[index]
            x1: int=current_list[0]
            y1: int=current_list[1]
            x2: int=current_list[2]
            y2: int=current_list[3]
            x3: int=current_list[4]
            y3: int=current_list[5]
            win_status=self.detect_win_helper(x1,y1,x2,y2,x3,y3)
            index+=1
        if win_status=="no win" and self.board.is_full()==True:
            win_status="cats"
        return win_status

        
    def detect_win_helper(self, x1: int, y1: int, x2: int, y2: int, x3: int, y3:int)->str:
        spot_1_contents=self.board.get_marker_at_spot(x1,y1)
        spot_2_contents=self.board.get_marker_at_spot(x2,y2)
        spot_3_contents=self.board.get_marker_at_spot(x3,y3)
        #                        Checks if all spots are the same                     checks if all spots are not empty
        #   vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv      vvvvvvvvvvvvvvvvvvvvvvvvvvvvv
        if (spot_1_contents==spot_2_contents and spot_1_contents==spot_3_contents) and (spot_1_contents is not None):
            #We have a winner!
            if spot_1_contents==self.marker1:
                return self.marker1 #player 1 won (x)
            elif spot_1_contents==self.marker2:
                return self.marker2 #player 2 won (o)
            else:
                print(spot_1_contents)
                assert False
        else:
            return "no win"

    def change_turn(self):
        if self.my_turn==self.marker1: #checking if it is x's turn
            self.my_turn=self.marker2 # if it is, change to o's turn
        elif self.my_turn==self.marker2: #if not, we check if it's o's turn
            self.my_turn=self.marker1 # if it is, change to x's turn
            
    

class Board:

    def __init__(self):
        self.grid=[
            [BoardSpot(0,0), BoardSpot(1,0), BoardSpot(2,0)],
            [BoardSpot(0,1), BoardSpot(1,1), BoardSpot(2,1)],
            [BoardSpot(0,2), BoardSpot(1,2), BoardSpot(2,2)]
        ]

    def __str__(self)-> str:
        output: str = ""
        output += f"{self.grid[0][0]} | {self.grid[0][1]} | {self.grid[0][2]}\n"
        output += "---------\n"
        output += f"{self.grid[1][0]} | {self.grid[1][1]} | {self.grid[1][2]}\n"
        output += "---------\n"
        output += f"{self.grid[2][0]} | {self.grid[2][1]} | {self.grid[2][2]}\n"
        return output

    def place_marker(self, _marker: str, _x: int, _y: int):
        assert 0<=_x
        assert _x<=2
        assert 0<=_y
        assert _y<=2
        self.grid[_y][_x].set_contents(_marker)
        
    def get_marker_at_spot(self, _x: int, _y: int) -> str:
        return self.grid[_y][_x].get_contents()

    def is_full(self)->bool:
        pass

class BoardSpot:

    def __init__(self, _x, _y):
        self.x=_x
        self.y=_y
        self.contents: str =None

    def __str__(self)->str:
        if self.contents==None:
            return "*"
        else:
            return self.contents

    def set_contents(self, _new_contents):
        self.contents=_new_contents

    def get_contents(self) -> str:
        return self.contents
        

game=Game()

#print(game.board)

game.run()
