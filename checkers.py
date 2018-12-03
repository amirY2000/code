class Checkers:
    def __init__(self) -> list:
        self.board = [[" ",1,2,3,4,5,6,7,8],[1,"w",".","w",".","w",".","w","."],[2,".","w",".","w",".","w",".","w"],[3,"w",".","w",".","w",".","w","."],[4,".",0,".",0,".",0,".",0],[5,0,".",0,".",0,".",0,"."],[6,".","B",".","B",".","B",".","B"],[7,"B",".","B",".","B",".","B","."],[8,".","B",".","B",".","B",".","B"]]
        self.player = 1
    def display_board(self) -> str:
        """
        return the board display
        """
        for i in self.board:
            for c in i:
                print(c,end = " ")
            print()
        return '----------------'

    def valid_piece(self,piece:int) -> bool:
        """
        return True iff the piece exist
        first number is column and second is row
        >>>valid_piece(board)
        >>>valid_piece(11)
        True
        >>>valid_piece(board)
        >>>valid_piece(12)
        False
        """
        a = int(piece[0])
        b = int(piece[1])
        if self.board[b][a] == "w" or self.board[b][a] == "B":
            return True
        return False

    def valid_move(self,piece:int,move:int) -> bool:
        """
        return True iff the move is valid in checkers game
        first letter is column and second one is row
        >>>valid_move(board)
        >>>33
        >>>44
        True
        >>>valid_move(board)
        >>>44
        >>>88
        False
        """
        a = int(move[0])
        b = int(move[1])
        g = int(piece[0])
        h = int(piece[1])
        print(self.board[h][g])
        if self.board[h][g] == "w" or self.board[h][g] == "B":
            if b-h == 1 or b-h == -1:
                if a-g == 1 or a-g == -1:
                    return True
            return False        
        return False
                
    def update_board(self : list, player:int, piece:int,move:int)-> str:
        """
        Update board by moving piece to move. Return True if and only if
        the opposing player (the one that is not moving a piece) has no valid
        moves after updating the game.
        >>>update_board(board)
        >>>1
        >>>33
        >>>44
        print board
        """
        if player != "1" and player != "2":
            return "please enter a valid player"
        a = int(move[0])
        b = int(move[1])
        if self.board[b][a] == 0:
            g = int(piece[0])
            h = int(piece[1])
            if player == "2" and self.board[h][g] == "B":
                if b-h == -1 and a-g == 1 or a-g == -1:
                        temp = self.board[h][g]
                        self.board[h][g] = self.board[b][a]
                        self.board[b][a] = temp
                        self.display_board()
            if player == "1" and self.board[h][g] == "w":
                if b-h == 1 and a-g == 1 or a-g == -1:
                    temp = self.board[h][g]
                    self.board[h][g] = self.board[b][a]
                    self.board[b][a] = temp
                    self.display_board()
    def update_player(self, player:int) -> int:
        if self.player == 1:
            self.player = 2
            return self.player
        else:
            self.player = 1
            return self.player

def main():
    checkers = Checkers()
    checkers.player = 1
    gameover = False
    while not gameover:
        print(checkers.display_board())
        piece = input("which piece would you like to move?")
        while not checkers.valid_piece(piece):
            piece = input("pick a valid piece")
        move = input("where would you like to move?")
        while not checkers.valid_move(piece,move):
            move = input("pick a valid move.")
        gameover = checkers.update_board(checkers.player,piece,move)
        player = checkers.update_player(checkers.player)
    player = checkers.update_player(player)
    print("Game over")

if __name__ == "__main__":
    main()            