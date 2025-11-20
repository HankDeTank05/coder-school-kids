import java.util.Scanner;

class tictactoe {
    
    public static void main(String[] args) {
        int[] board = {0,0,0,
                       0,0,0,
                       0,0,0};
       int playerTurn = 1;
       int winner = 0;
       Scanner input = new Scanner(System.in);
       while (winner == 0){
        System.out.println("make a move" );
        int Move = input.nextInt();
        if (board[Move -1] == 0){
        board[Move-1] = playerTurn;
        if (playerTurn == 1){
            playerTurn = 2;
        }
        else {
            playerTurn = 1;
        }
        }
       
        printBoard(board);
        
        winner = (checkWin(board));
       }
    }
    public static void printBoard(int[] board){
        String toPrint = "";

        for (int i = 0; i < board.length; i++) {
            if (board[i] == 0) {
                toPrint += "_";
            } else if (board[i] == 1) {
                toPrint += "X";
            } else if (board[i] == 2) {
                toPrint += "O";
            }
            if (i == 2 || i == 5) {
                toPrint += "\n";
            }
        }
        System.out.println(toPrint);
        //0, 1, 2, 0, 2, 2, 1, 0, 1
        /*_XO
          _OO
          X_X */
    } 
    public static int checkWin(int[] board) {
        if (board[0] == board[1] && board[1] == board[2] && board[0] != 0){
            return board[0];
        }
        if (board[3] == board[4] && board[4] == board[5] && board[3] != 0){
            return board[3];
        }
        return 0;
    }
}
