'''
Chess is a game which will play between two players.
The chess board is a square surface which has 64 squares on it.
Half of these squares are white and the rest of them are black.
Each player has 16 pieces: 8 pawns, 1 king, 1 queen, 2 bishobs, 2 nights,
2 rooks:
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
        
The colour of each player's pieces is different. For instance, player 
one's pieces are white and the other player's pieces are black. White should
move first. All pieces have different features. For insance, all of the 
pieces can capture other pieces except the king place on the threat of capturing
check will happen that the player shoud block this threat or move his king:
it is a posisssion of a check:
        --| a | b  | c  | d  | e  | f  | g  | h 
        8  Rb | .  | Bb | Qb | Kb | Bb | Nb | Rb 
        7  Pb | Pb | Pb | .  | .  | .  | Pb | Pb 
        6  .  | .  | Nb | Pb | .  | .  | .  | . 
        5  .  | .  | .  | .  | Pb | .  | .  | Qw 
        4  .  | .  | Bw | .  | Pw | .  | .  | . 
        3  .  | .  | .  | .  | .  | .  | .  | . 
        2  Pw | Pw | Pw | Pw | .  | Pw | Pw | Pw 
        1  Rw | Nw | Bw | .  | Kw | .  | Nw | Rw 
        --| a | b  | c  | d  | e  | f  | g  | h
checkmate is the situation that one player's king by placing it under
an inescapable threat of capture in this situation the player will lose.
it is a posission of a checkmate:
        --| a | b  | c  | d  | e  | f  | g  | h 
        8  Rb | .  | Bb | Qb | Kb | Bb | Nb | Rb 
        7  Pb | Pb | Pb | .  | .  | Qw | Pb | Pb 
        6  .  | .  | Nb | Pb | .  | .  | .  | . 
        5  .  | .  | .  | .  | Pb | .  | .  | . 
        4  .  | .  | Bw | .  | Pw | .  | .  | . 
        3  .  | .  | .  | .  | .  | .  | .  | . 
        2  Pw | Pw | Pw | Pw | .  | Pw | Pw | Pw 
        1  Rw | Nw | Bw | .  | Kw | .  | Nw | Rw 
        --| a | b  | c  | d  | e  | f  | g  | h
If there is no piece to checkmate, then the resualt will be draw.
it is an example of a draw:
        --|a | b | c | d | e  | f | g | h 
        8  . | . | . | . | KB | . | . | .
        7  . | . | . | . | .  | . | . | . 
        6  . | . | . | . | .  | . | . | . 
        5  . | . | . | . | .  | . | . | . 
        4  . | . | . | . | .  | . | . | . 
        3  . | . | . | . | .  | . | . | . 
        2  . | . | . | . | .  | . | . | . 
        1  . | . | . | . | Kw | . | . | . 
        --|a | b | c | d | e  | f | g | h 
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

        we will expect see a board 
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
        move one house forward or two houses if it has never move before
        """
    def Special_move(self):
        """
        * capturing
        """
    def capability(self):
        """
        change to another piece when it arrives the last square.
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
        it is for special move "castle"
        if this move is going to happen in the king side
        the king will move two house to the right and the rook will 
        move the the left of the king. Or if it is going to happen in the 
        queen side, the king will move two houses to the left and the rook 
        will move to the right side of the king.
        king side:
        4  . | . | . | . | . | . | . | . 
        3  . | . | . | . | . | . | . | . 
        2  * | * | * | * | * | * | * | * 
        1  * | * | * | * | . | R | K | . 
        queen side:
        4  . | . | . | . | . | . | . | . 
        3  . | . | . | . | . | . | . | . 
        2  * | * | * | * | * | * | * | * 
        1  . | . | k | R | * | * | * | * 
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
    def castle(self):
        """
        it is for special move "castle"
        if this move is going to happen in the king side
        the king will move two house to the right and the rook will 
        move the the left of the king. Or if it is going to happen in the 
        queen side, the king will move two houses to the left and the rook 
        will move to the right side of the king.
        king side:
        4  . | . | . | . | . | . | . | . 
        3  . | . | . | . | . | . | . | . 
        2  * | * | * | * | * | * | * | * 
        1  * | * | * | * | . | R | K | . 
        queen side:
        4  . | . | . | . | . | . | . | . 
        3  . | . | . | . | . | . | . | . 
        2  * | * | * | * | * | * | * | * 
        1  . | . | k | R | * | * | * | * 
        """

class Game():
    """
    This class is for updating players, updating board,
    valid peice, valid move.
    """
    def __init__(self):
        """
        make the board
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

