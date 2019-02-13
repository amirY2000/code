'''
Chess is a two-players game played on a chess board.
The chess board is a square surface which has 64 squares on it.
Half of these squares are white and the rest of them are black.
Each player has 16 pieces: 8 pawns, 1 king, 1 queen, 2 bishobs, 2 nights,
2 rooks. The colour of each player's pieces is different. For instance, player 
one's pieces are white and the other player's pieces are black. White should
move first. All pieces have different features. For insance, all of the 
pieces can capture other pieces except the king place on the threat of capturing
check will happen that the player shoud block this threat or move his king.
checkmate is the situation that one player's king by placing it under
an inescapable threat of capture in this situation the player will lose.
If there is no piece to checkmate, then the resualt will be draw.

We need a loop which ask for the next move and in this loop we have to change
player aoutomatically after each move. Also, this loop will update board after 
each move. The break condition of this loop is gameover == True. this while-
loop will work untill the game over becomes true.

'''
class board():
    """
    this class will creat our chess board and 
    with specific identification for each square 
    in the board
    """
    def __init__(self):
        """
        this function is for initializing the board 
        with its pieces.
        --|a | b | c | d | e | f | g | h 
        8  R | N | B | Q | K | B | N | R 
        7  P | P | P | P | P | P | P | P 
        6  . | . | . | . | . | . | . | . 
        5  . | . | . | . | . | . | . | . 
        4  . | . | . | . | . | . | . | . 
        3  . | . | . | . | . | . | . | . 
        2  P | P | P | P | P | P | P | P 
        1  R | N | B | Q | K | B | N | R 
        --|a | b | c | d | e | f | g | h 

        we will undrestimate to see a board 
        same as the above figure
        """
    def display_board(self):
        """
        this function will creat our board on the screen
        """
class Pawn():
    """
    the characteristics of pawn in chess: 
    Normal movements.
    Special movement.
    capability.
    """
    def __init__(self):
        """
        initializing the piece
        """
    def Normal_move(self):
        """
        move one house forward
        """
    def Special_move(self):
        """
        this function will cover:
        * capturing
        *anpasan
        * Two house forward at the beginning
        * changing to another piece
    """
class King():
    """
    The characteristics of a king in chess:
    normal movement
    special move
    """
    def __init__(self):
        """
        initializing the piece
        """
    def movement(self):
        """
        this function will cover all movements of the king:
        *cross
        *forward and backward
        *sides
        """
    def castle(self):
        """
        it will cover the castle move in chess which has special conditions
        """
class Queen():
    """
    We have one queen on the board which has some features.
    The characteristics of a Queen in chess:
    normal movement.
    """
    def __init__(self):
        """
        initialize the piece
        """
    def movement(self):
        """
        this func will cover all movements of the queen in chess:
        *cross
        *forward & backward
        *sides
        it can move to all these directions without any limitaition.
        only limitation is that, it can jump like the Night.
        """
class Bishob():
    """
    the characteristics of Bishob in chess:
    movement
    """
    def __init__(self):
        """
        initializing the piece
        """
    def movement(self):
        """
        this func will cover all movements of a bishob
        *cross
        """
class Night():
    """
    the characteristics of a night in chess:
    movement
    """
    def __init__(self):
        """
        initializing the piece
        """
    def movement(self):
        """
        this function will cover night's moves
        *L
        """
class Rook():
    """
    characteristics of a rook in chess:
    movement
    """
    def __init__(self):
        """
        initializing the piece
        """
    def movement(self):
        """
        this function will cover rook's moves
        *forward and backward
        *sides
        """
class Game():
    """
    This class is for the updating players, updating board,
    valid peice, valid move.
    """
    def update_board(self):
        """
        this function will update board after each move
        """
    def valid_move(self):
        """
        this function will recognize the valid move 
        and will return not valid move if you move wrong.
        """
    def valid_piece(self):
        """
        this function will recognize that when a piece is valid to move
        or not in diffetrent situations like check, checkmate, play with 
        wrong colour,....
        """
    def update_player(self):
        """
        this function will update player after each move
        """
    def main(self):
        """
        this function will include the loops which play the role of 
        engine in the game and will recognize that game over is true or not.
        """
if __name__ == "__main__":
    pass

