def initialize_board() -> list:
    board = ['',"w",".","w",".","w",".","w",".",".","w",".","w",".","w",".","w","w",".","w",".","w",".","w",".",".",0,".",0,".",0,".",0,0,".",0,".",0,".",0,".",".","B",".","B",".","B",".","B","B",".","B",".","B",".","B",".",".","B",".","B",".","B",".","B"]
    return board

def display_board(board) -> str:
    """
    return the board display
    """
    board = [[" ",1,2,3,4,5,6,7,8],[1,"w",".","w",".","w",".","w","."],[2,".","w",".","w",".","w",".","w"],[3,"w",".","w",".","w",".","w","."],[4,".",0,".",0,".",0,".",0],[5,0,".",0,".",0,".",0,"."],[6,".","B",".","B",".","B",".","B"],[7,"B",".","B",".","B",".","B","."],[8,".","B",".","B",".","B",".","B"]]
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
    first number is column and second is row
    >>>valid_piece(b,11)
    True
    >>>valid_piece(b,22)
    False
    """
    piece = input("which peice are you looking for ? ")
    board = [[" ",1,2,3,4,5,6,7,8],[1,"w",".","w",".","w",".","w","."],[2,".","w",".","w",".","w",".","w"],[3,"w",".","w",".","w",".","w","."],[4,".",0,".",0,".",0,".",0],[5,0,".",0,".",0,".",0,"."],[6,".","B",".","B",".","B",".","B"],[7,"B",".","B",".","B",".","B","."],[8,".","B",".","B",".","B",".","B"]]
    a = piece[0]
    b = piece[1]
    for i in range(100):
        if str(i) == a:
            a = i
            for j in range(100):
                if str(j) == b:
                    b = j
                    break
    if board[b][a] == "w" or board[b][a] == "B":
        return True
    return False
board = initialize_board()
print(valid_piece(board))

def valid_move(board) -> bool:
    """
    return True iff the move is valid in checkers game
    first letter is column and second one is row
    >>>valid_move(b,33,44)
    True
    >>>valid_move(b,17,25)
    False
    """
    piece = input("Which piece would you like to move ? ")
    move = input("to?! ")
    board = [[" ",1,2,3,4,5,6,7,8],[1,"w",".","w",".","w",".","w","."],[2,".","w",".","w",".","w",".","w"],[3,"w",".","w",".","w",".","w","."],[4,".",0,".",0,".",0,".",0],[5,0,".",0,".",0,".",0,"."],[6,".","B",".","B",".","B",".","B"],[7,"B",".","B",".","B",".","B","."],[8,".","B",".","B",".","B",".","B"]]
    a = move[0]
    b = move[1]
    for i in range(100):
        if str(i) == a:
            a = i
            for j in range(100):
                if str(j) == b:
                    b = j
                    break
    print(board[b][a])
    if board[b][a] == 0:
        g = piece[0]
        h = piece[1]
        for l in range(100):
            if str(l) == g:
                g = l
                for p in range(100):
                    if str(p) == h:
                        h = p
                        break
        if board[h][g] == "w" or board[h][g] == "B":
            if b-h == 1 or b-h == -1:
                if a-g == 1 or a-g == -1:
                    return True
            return False        
        return False
    return False
              
board = initialize_board()
print(valid_move(board))

def update_board(board : list) -> bool:
    """
    Update board by moving piece to move. Return True if and only if
    the opposing player (the one that is not moving a piece) has no valid
    moves after updating the game.
    """
    board = [[" ",1,2,3,4,5,6,7,8],[1,"w",".","w",".","w",".","w","."],[2,".","w",".","w",".","w",".","w"],[3,"w",".","w",".","w",".","w","."],[4,".",0,".",0,".",0,".",0],[5,0,".",0,".",0,".",0,"."],[6,".","B",".","B",".","B",".","B"],[7,"B",".","B",".","B",".","B","."],[8,".","B",".","B",".","B",".","B"]]
    player = input("player 1 or player 2 ? ")
    piece = input("which piece do you want to move ? ")
    move = input("what is your destination ? ")
    a = move[0]
    b = move[1]
    for i in range(100):
        if str(i) == a:
            a = i
            for j in range(100):
                if str(j) == b:
                    b = j
    print(board[b][a])
    if board[b][a] == 0:
        g = piece[0]
        h = piece[1]
        for l in range(100):
            if str(l) == g:
                g = l
                for p in range(100):
                    if str(p) == h:
                        h = p
        if player == str(1) and board[h][g] == "w":
            if b-h == 1 and a-g == 1:
                    temp = board[h][g]
                    board[h][g] = board[b][a]
                    board[b][a] = temp
                    for d in board:
                        for c in d:
                            print(c,end = " ")
                        print()
        if player == str(2) and board[h][g] == "B":
            if b-h == -1 or a-g == -1:
                temp = board[h][g]
                board[h][g] = board[b][a]
                board[b][a] = temp
                for d in board:
                    for c in d:
                        print(c,end = " ")
                    print()
        else:
            return "Please enter a valid player"
board = initialize_board()
print(update_board(board))
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
            while not valid_move(board):
                move = input("Player {}, pick a valid move for the piece at {}.".format(player, piece))
            gameover = update_board(board)
            player = update_player(player)
        player = update_player(player)
        print("Game over, player {} wins!".format(player))
     