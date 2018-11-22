# complete the example and description for this function
# then test it
def initialize_board() -> list:
    b = [" 1 1 1 1", "1 1 1 1 ", " 1 1 1 1", "0 0 0 0 ", " 0 0 0 0", "2 2 2 2 ", " 2 2 2 2", "2 2 2 2 "]
    return b

# write this function according to the function design recipe
def display_board(board) -> str:
    pass

# write this function according to the function design recipe
def valid_piece(board, piece) -> bool:
    pass

# write this function according to the function design recipe
def valid_move(board, move, piece) -> bool:
    pass

# write examples for this function, then complete the code body
# and test it.
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
    board = initilaize_board()
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
