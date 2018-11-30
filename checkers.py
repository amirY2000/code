def initialize_board() -> list:
    b = [" 1 1 1 1", "1 1 1 1 ", " 1 1 1 1", "0 0 0 0 ", " 0 0 0 0", "2 2 2 2 ", " 2 2 2 2", "2 2 2 2 "]
    return b

def display_board(board) -> str:
    """
    return the board display
    """
    board = [["   ","a","b","c","d","e","f","g","h"],[1,"|","w",".","w",".","w",".","w","."],[2,"|",".","w",".","w",".","w",".","w"],[3,"|","w",".","w",".","w",".","w","."],[4,"|",".",0,".",0,".",0,".",0],[5,"|",0,".",0,".",0,".",0,"."],[6,"|",".","B",".","B",".","B",".","B"],[7,"|","B",".","B",".","B",".","B","."],[8,"|",".","B",".","B",".","B",".","B"]]
    for i in board:
        for c in i:
            print(c,end = " ")
        print()
    return ''
board = initialize_board()
print(display_board(board))

def valid_piece(board,piece = None) -> bool:
    """
    return True iff the piece exist
    >>>valid_piece(b,1)
    True
    >>>valid_piece(b,2)
    False
    """
    piece = input("which peice are you looking for ? ")
    board = ['',"w",".","w",".","w",".","w",".",".","w",".","w",".","w",".","w","w",".","w",".","w",".","w",".",".",0,".",0,".",0,".",0,0,".",0,".",0,".",0,".",".","B",".","B",".","B",".","B","B",".","B",".","B",".","B",".",".","B",".","B",".","B",".","B"]
    if piece == "0":
        return False
    for i in range(len(board)):
        if str(i) == piece:
            if board[i] == "w" or board[i] == "B":
                return True
            return False
board = initialize_board()
print(valid_piece(board))

def valid_move(board) -> bool:
    """
    return True iff the move is valid in checkers game
    >>>valid_move(b,17,26)
    True
    >>>valid_move(b,17,25)
    False
    """
    piece = input("Which piece would you like to move ? ")
    move = input("to?! ")
    board = ['',"w",".","w",".","w",".","w",".",".","w",".","w",".","w",".","w","w",".","w",".","w",".","w",".",".",0,".",0,".",0,".",0,0,".",0,".",0,".",0,".",".","B",".","B",".","B",".","B","B",".","B",".","B",".","B",".",".","B",".","B",".","B",".","B"]
    if piece == "0" or move == "0":
        return False
    for i in range(len(board)):
        if str(i) == move:
            move = i
            if board[i] == "w" or board[i] == "B":
                for j in range(len(board)):
                    if str(j) == piece:
                        if board[j] == "w" or board[j] == "B":
                                if move - j == 7 or move - j == 9 and board[move] == 0:
                                    return True
                                return False
            else:
                return False              
board = initialize_board()
print(valid_move(board))

def update_board(board : list, move : str, piece : str, player : int) -> bool:
    """
    Update board by moving piece to move. Return True if and only if
    the opposing player (the one that is not moving a piece) has no valid
    moves after updating the game.
    """
    pass
 # write this function according to the function design recipe.

def update_player(player) -> int:
    pass
    if __name__ == "__main__":
        board = initialize_board()
        player = 1
        gameover = False
        while not gameover:
            print(display_board(board))
            piece = input("Player {}, which piece would you like to move?".format(player))
            while not valid_piece(board, piece):
                piece = input("Player {}, pick a valid piece".format(player))
            move = input("Player {}, where would you like to move the piece at {}?".format(player, piece))
            while not valid_move(board, move, piece):
                move = input("Player {}, pick a valid move for the piece at {}.".format(player, piece))
            gameover = update_board(board, move, piece, player)
            player = update_player(player)
        player = update_player(player)
        print("Game over, player {} wins!".format(player))