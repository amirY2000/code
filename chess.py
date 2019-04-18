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
class piece():
    def __init__(self,color):
        self.color = color
class Pawn(piece):
        """ 
        the characteristics of pawn in chess: 
        Normal movements.
        Special movement.
        capability.
        """
        def __init__(self, color):
            """
            initializing the piece
            """
            super().__init__(color)
        def Normal_move(self,origin,destination):
            """
            move one house forward or two houses if it has never move before
            """
            numbers = [1,2,3,4,5,6,7,8]
            origin = str(origin)
            destination = str(destination)
            x = int(origin[0])
            x1 = int(destination[0])
            y = int(origin[1])
            y1 = int(destination[1])
            if y and y1 not in numbers:
                return False
            if y == 2 and self.color == "w" :
                if y1-y == 2 and x1 == x:
                    return True
                elif y1-y == 1 and x1 == x:
                    return True
                return False
            if y == 7 and self.color == "b":  
                if y-y1 == 2 and x1 == x:
                    return True
                elif y-y1 == 1 and x1 == x:
                    return True
                return False 
            if y != 2 and self.color == "w":
                if y1-y == 1 and x1 == x:
                    return True
                return False
            if y != 7 and self.color == "b":
                if y-y1 == 1 and x1 == x:
                    return True
                return False  
            return False  
        def Special_move(self,origin,destination):
            """
            * capturing
            """
            origin = str(origin)
            x = int(origin[0])
            y = int(origin[1])
            destination = str(destination)
            x1 = int(destination[0])
            y1 = int(destination[1])
            if self.color == "w":
                if y1-y == 1 and x-x1 == 1:
                    return True
                if y1-y == 1 and x1-x == 1:
                    return True
                else:
                    False
            if self.color == "b":
                if y-y1 == 1 and x1-x == 1:
                    return True
                if y-y1 == 1 and x-x1 == 1:
                    return True
                else:
                    False
        def capability(self,origin,destination):
            """
            change to another piece when it arrives the last square.
            """
            origin = str(origin)
            y = int(origin[1])
            destination = str(destination)
            y1 = int(destination[1])
            if self.color == "w" and y == 7:
                if y1 == 8:
                    return True
                return False
            if self.color == "b" and y == 2:
                if y1 == 1:
                    return True
                return False
            return False
        def __str__(self):
            return "P{0}".format(self.color)            
class King(piece):
        """
        The characteristics of a king in chess:
        normal movement
        special move
        """
        def __init__(self,color):
            """
            initializing the piece
            """
            super().__init__(color)
        def movement(self,origin,destination):
            """
            this function will cover all movements of the king:
            *cross
            *forward and backward
            *sides
            """
            numbers = [1,2,3,4,5,6,7,8]
            origin = str(origin)
            x = int(origin[0])
            y = int(origin[1])
            destination = str(destination)
            x1 = int(destination[0])
            y1 = int(destination[1])
            if x and x1 and y and y1 not in numbers:
                return False 
            if self.color == "w" or "b":
                if y1-y == 1 and x1-x == 0:#north
                    return True
                elif y-y1 == 1 and x1-x == 0:#south
                    return True
                elif y1-y == 1 and x1-x == 1:#north-east
                    return True 
                elif y-y1 == 1 and x-x1 == 1:#south-west
                    return True 
                elif y1-y == 1 and x-x1 == 1:#north-west
                    return True 
                elif y-y1 == 1 and x1-x == 1:#south-east
                    return True 
                elif y1-y == 0 and x1-x == 1:#east
                    return True 
                elif y1-y == 0 and x-x1 == 1:#west
                    return True
                return False
        def castle(self,origin,destination):
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
            origin = str(origin)
            x = int(origin[0])
            y = int(origin[1])
            destination = str(destination)
            x1 = int(destination[0])
            y1 = int(destination[1])
            if x == 4 and self.color == "w" and y == 1 and y1 == 1:
                if x1 == 2:
                    return "king"
                elif x1 == 6:
                    return "queen"
            if x == 4 and self.color == "b" and y == 8 and y1 == 8:
                if x1 == 2:
                    return "king"
                elif x1 == 6:
                    return "queen"
                return False
            return False
        def __str__(self):
            return "K{0}".format(self.color) 
class Queen(piece):
        """
        We have one queen on the board which has some features.
        The characteristics of a Queen in chess:
        normal movement.
        """
        def __init__(self,color):
            """
            initialize the piece
            """
            super().__init__(color)
        def movement(self,origin,destination):
            """
            this func will cover all movements of the queen in chess:
            *cross
            *forward & backward
            *sides
            it can move to all these directions without any limitaition.
            only limitation is that, it can jump like the Night.
            """
            numbers = [1,2,3,4,5,6,7,8]
            x = int(origin[0])
            y = int(origin[1])
            x1 = int(destination[0])
            y1 = int(destination[1])
            if x and x1 and y and y1 not in numbers:
                return False
            if self.color == "w" or "b":
                if (x1-x) > 0 and (y1-y) > 0 and x1-x == y1-y:
                    return "north east"
                if (x1-x) < 0 and (y1-y) < 0 and x1-x == y1-y:
                    return "south west"
                if (x1-x) < 0 and (y1-y) > 0 and x-x1 == y1-y:
                    return "north west"
                if (x1-x) > 0 and (y1-y) < 0 and x1-x == y-y1:
                    return "south east"
                if y1-y == 0:#horizontal
                    return "horizontal"
                if x1-x == 0:#vertical
                    return "vertical"
                return False
            return False
        def __str__(self):
            return "Q{0}".format(self.color) 
class Bishob(piece):
        """
        the characteristics of Bishob in chess:
        movement
        """
        def __init__(self,color):
            """
            initializing the piece
            """
            super().__init__(color)
        def movement(self,origin,destination):
            """
            this func will cover all movements of a bishob
            *cross
            """
            numbers = [1,2,3,4,5,6,7,8]
            origin = str(origin)
            x = int(origin[0])
            y = int(origin[1])
            destination = str(destination)
            x1 = int(destination[0])
            y1 = int(destination[1])
            if x and x1 and y and y1 not in numbers:
                return False
            if self.color == "w" or "b":
                if (x1-x) > 0 and (y1-y) > 0 and x1-x == y1-y:
                    return "north east"
                if (x1-x) < 0 and (y1-y) < 0 and x1-x == y1-y:
                    return "south west"
                if (x1-x) < 0 and (y1-y) > 0 and x-x1 == y1-y:
                    return "north west"
                if (x1-x) > 0 and (y1-y) < 0 and x1-x == y-y1:
                    return "south east"
                return False
            return False
        def __str__(self):
            return "B{0}".format(self.color) 
class Night(piece):
        """
        the characteristics of a night in chess:
        movement
        """
        def __init__(self,color):
            """
            initializing the piece
            """            
            super().__init__(color)
        def movement(self,origin,destination):
            """
            this function will cover night's moves
            *L
            """
            numbers = [1,2,3,4,5,6,7,8]
            origin = str(origin)
            x = int(origin[0])
            y = int(origin[1])
            destination = str(destination)
            x1 = int(destination[0])
            y1 = int(destination[1])
            if x and x1 and y and y1 not in numbers:
                return False
            if self.color is "w" or "b":
                if y1-y == 2 and x1-x == 1:
                    return True
                if y1-y == 2 and x-x1 == 1:
                    return True
                if y-y1 == 2 and x1-x == 1:
                    return True
                if y-y1 == 2 and x-x1 == 1:
                    return True
                if x1-x == 2 and y1-y == 1:
                    return True
                if x1-x == 2 and y-y1 == 1:
                    return True
                if x-x1 == 2 and y1-y == 1:
                    return True
                if x-x1 == 2 and y-y1 == 1:
                    return True
                return False
            return False
        def __str__(self):
            return "N{0}".format(self.color) 
class Rook(piece):
        """
        characteristics of a rook in chess:
        movement
        """
        def __init__(self,color):
            """
            initializing the piece
            """
            super().__init__(color)
        def movement(self,origin,destination):
            """
            this function will cover rook's moves
            *forward and backward
            *sides
            """
            numbers = [1,2,3,4,5,6,7,8]
            origin = str(origin)
            x = int(origin[0])
            y = int(origin[1])
            destination = str(destination)
            x1 = int(destination[0])
            y1 = int(destination[1])
            if x and x1 and y and y1 not in numbers:
                return False
            if self.color == "w" or "b":
                if y1 == y:#horizontal
                    return "horizontal"
                if x1 == x:#vertical
                    return "vertical"
                else:
                    return False
            return False
        def __str__(self):
            return "R{0}".format(self.color) 
class Game():
    def __init__(self):
        self.board = [["|"," h",' g',' f',' e',' d',' c',' b',' a'],[1,Rook("w"),Night("w"),Bishob("w"),King("w"),Queen("w"),Bishob("w"),Night("w"),Rook("w")],[2,Pawn("w"),Pawn("w"),Pawn("w"),Pawn("w"),Pawn("w"),Pawn("w"),Pawn("w"),Pawn("w")],[3," "," "," "," "," "," "," "," "],[4," "," "," "," "," "," "," "," "],[5," "," "," "," "," "," "," "," "],[6," "," "," "," "," "," "," "," "],[7,Pawn("b"),Pawn("b"),Pawn("b"),Pawn("b"),Pawn("b"),Pawn("b"),Pawn("b"),Pawn("b")],[8,Rook("b"),Night("b"),Bishob("b"),King("b"),Queen("b"),Bishob("b"),Night("b"),Rook("b")],["|"," h",' g',' f',' e',' d',' c',' b',' a']] 
    
    def display_board(self):
        """
        this function will creat our board on the screen
        --| a | b  | c  | d  | e  | f  | g  | h 
        8  Rb | Nb | Bb | Qb | Kb | Bb | Nb | Rb 
        7  Pb | Pb | Pb | Pb | Pb | Pb | Pb | Pb 
        6  .  | .  | .  | .  | .  | .  | .  | . 
        5  .  | .  | .  | .  | .  | .  | .  | . 
        4  .  | .  | .  | .  | .  | .  | .  | . 
        3  .  | .  | .  | .  | .  | .  | .  | . 
        2  Pw | Pw | Pw | Pw | Pw | Pw | Pw | Pw 
        1  Rw | Nw | Bw | Qw | Kw | Bw | Nw | Rw 
        --| a | b  | c  | d  | e  | f  | g  | h
            we will expect see a board 
            same as the above figure
        """
        for i in self.board:
            for c in i:
                print(c,end = " ")
            print()
        return '------------------------'
    
    def update_board(self,origin,destination,player):
        """
        this function will update board after each move
        """
        x = int(origin[0])
        y = int(origin[1])
        x1 = int(destination[0])
        y1 = int(destination[1])
        if type(self.board[y1][x1]) == str:
            temp = self.board[y][x]
            self.board[y][x] = self.board[y1][x1]
            self.board[y1][x1] = temp
        elif type(self.board[y1][x1]) != str:
            temp = self.board[y][x]
            self.board[y][x] = " "
            self.board[y1][x1] = temp
        for i in self.board:
            for c in i:
                print(c,end = " ")
            print()
        return '------------------------'
    
    def valid_move(self,origin,destination):
        """
        this function will recognize the valid move 
        and will return not valid move if you move wrong.
        """
        x = int(origin[0])
        y = int(origin[1])
        x1 = int(destination[0])
        y1 = int(destination[1])
        if x1 and y1 <= 8:
            origin = str(x) + str(y)
            destination = str(x1) + str(y1)
            piece_to_move = self.board[y][x]
            place_to_move = self.board[y1][x1]
            if type(piece_to_move) == Pawn:
                if piece_to_move.Normal_move(origin,destination) == True and type(place_to_move) == str :
                    if piece_to_move.capability(origin,destination) == True:
                        if type(place_to_move) == str:
                            return "cap"
                        return False
                    return True
                elif piece_to_move.Special_move(origin,destination) == True and type(place_to_move) != str:
                    if piece_to_move.color != place_to_move.color:
                        if piece_to_move.capability(origin,destination) == True:
                            return "cap"  
                        return True  
                    return False
                return False
            
            if type(piece_to_move) == King:
                if type(place_to_move) == str:
                    if piece_to_move.movement(origin,destination) == True:
                        return True
                    elif piece_to_move.castle(origin,destination) == "king" and type(self.board[y1][x1-1]) == Rook:
                        if type(place_to_move) and type(self.board[y1][x1+1]) == str:
                            return "castle king"
                    elif piece_to_move.castle(origin,destination) == "queen" and type(self.board[y1][x1+2]) == Rook:
                        if type(place_to_move) and type(self.board[y1][x1-1]) and type(self.board[y1][x1+1]) == str:
                            return "castle queen"
                    return False
                else:    
                    if piece_to_move.movement(origin,destination) == True and place_to_move.color != piece_to_move.color:
                        return True
                    return False
                return False
    
            if type(piece_to_move) == Night:
                if type(place_to_move) == str:
                    if piece_to_move.movement(origin,destination) == True:
                        return True
                    return False
                else:
                    if place_to_move.color != piece_to_move.color and piece_to_move.movement(origin,destination) == True:     
                        return True   
                return False  
            
            if type(piece_to_move) == Rook:
                if piece_to_move.movement(origin,destination) == "horizontal":
                    a = x1-x 
                    if a < 0:
                        a *= -1
                        for i in range(1,a+1):
                            if type(self.board[y1][x-i]) != str:
                                if piece_to_move.color == self.board[y1][x-i].color:
                                    return False
                                elif piece_to_move.color != self.board[y1][x-i].color and x-i != x1:
                                    return False
                                elif piece_to_move.color != self.board[y1][x-i].color and x-i == x1:
                                    return True
                                return False
                            elif x-i == x1:
                                return True
                        return False
                    else:
                        for i in range(1,a+1):
                            if type(self.board[y1][x+i]) != str:
                                if piece_to_move.color == self.board[y1][x+i].color:
                                    return False
                                elif piece_to_move.color != self.board[y1][x+i].color and x+i != x1:
                                    return False
                                elif piece_to_move.color != self.board[y1][x+i].color and x+i == x1:
                                    return True
                                return False
                            elif x+i == x1:
                                return True
                        return False
                    return False
                if piece_to_move.movement(origin,destination) == "vertical":
                    a = y1-y 
                    if a < 0:
                        a *= -1
                        for i in range(1,a+1):
                            if type(self.board[y-i][x1]) != str:
                                if piece_to_move.color == self.board[y-i][x1].color:
                                    return False
                                elif piece_to_move.color != self.board[y-i][x1].color and y-i != y1:
                                    return False
                                elif piece_to_move.color != self.board[y-i][x1].color and y-i == y1:
                                    return True
                                return False
                            if y-i == y1:
                                return True
                        return False 
                    else:
                        for i in range(1,a+1):
                            if type(self.board[y+i][x1]) != str:
                                if piece_to_move.color == self.board[y+i][x].color:
                                    return False
                                elif piece_to_move.color != self.board[y+i][x1].color and y+i != y1:
                                    return False
                                elif piece_to_move.color != self.board[y+i][x1].color and y+i == y1:
                                    return True
                                return False
                            elif y+i == y1:
                                return True
                        return False     
                    return False
                return False

            if type(piece_to_move) == Bishob:
                if piece_to_move.movement(origin,destination) == "north east":
                    for j in range(1,(x1-x)+1):
                        if type(self.board[y+j][x+j]) != str:    
                            if piece_to_move.color == self.board[y+j][x+j].color:
                                return False
                            elif piece_to_move.color != self.board[y+j][x+j].color and y+j != y1:
                                return False
                            elif piece_to_move.color != self.board[y+j][x+j].color and y+j == y1:
                                    return True
                        elif y+j == y1:
                            return True
                    return False
                if piece_to_move.movement(origin,destination) == "south west":
                    for j in range(1,(y-y1)+1):
                        if type(self.board[y-j][x-j]) != str:    
                            if piece_to_move.color == self.board[y-j][x-j].color:
                                return False
                            elif piece_to_move.color != self.board[y-j][x-j].color and y-j != y1:
                                return False
                            elif piece_to_move.color != self.board[y-j][x-j].color and y-j == y1:
                                    return True
                        elif y-j == y1:
                            return True
                    return False
                if piece_to_move.movement(origin,destination) == "north west":
                    for j in range(1,(y1-y)+1):
                        if type(self.board[y+j][x-j]) != str:    
                            if piece_to_move.color == self.board[y+j][x-j].color:
                                return False
                            elif piece_to_move.color != self.board[y+j][x-j].color and y+j != y1:
                                return False
                            elif piece_to_move.color != self.board[y+j][x-j].color and y+j == y1:
                                    return True
                        elif y+j == y1:
                            return True
                    return False
                if piece_to_move.movement(origin,destination) == "south east":
                    for j in range(1,(x1-x)+1):
                        if type(self.board[y-j][x+j]) != str:    
                            if piece_to_move.color == self.board[y-j][x+j].color:
                                return False
                            elif piece_to_move.color != self.board[y-j][x+j].color and y-j != y1:
                                return False
                            elif piece_to_move.color != self.board[y-j][x+j].color and y-j == y1:
                                    return True
                        elif y-j == y1:
                            return True
                    return False
                return False

            if type(piece_to_move) == Queen:
                if piece_to_move.movement(origin,destination) == "north east":
                    for j in range(1,(x1-x)+1):
                        if type(self.board[y+j][x+j]) != str:    
                            if piece_to_move.color == self.board[y+j][x+j].color:
                                return False
                            elif piece_to_move.color != self.board[y+j][x+j].color and y+j != y1:
                                return False
                            elif piece_to_move.color != self.board[y+j][x+j].color and y+j == y1:
                                    return True
                        elif y+j == y1:
                            return True
                    return False
                if piece_to_move.movement(origin,destination) == "south west":
                    for j in range(1,(y-y1)+1):
                        if type(self.board[y-j][x-j]) != str:    
                            if piece_to_move.color == self.board[y-j][x-j].color:
                                return False
                            elif piece_to_move.color != self.board[y-j][x-j].color and y-j != y1:
                                return False
                            elif piece_to_move.color != self.board[y-j][x-j].color and y-j == y1:
                                    return True
                        elif y-j == y1:
                            return True
                    return False
                if piece_to_move.movement(origin,destination) == "north west":
                    for j in range(1,(y1-y)+1):
                        if type(self.board[y+j][x-j]) != str:    
                            if piece_to_move.color == self.board[y+j][x-j].color:
                                return False
                            elif piece_to_move.color != self.board[y+j][x-j].color and y+j != y1:
                                return False
                            elif piece_to_move.color != self.board[y+j][x-j].color and y+j == y1:
                                    return True
                        elif y+j == y1:
                            return True
                    return False
                if piece_to_move.movement(origin,destination) == "south east":
                    for j in range(1,(x1-x)+1):
                        if type(self.board[y-j][x+j]) != str:    
                            if piece_to_move.color == self.board[y-j][x+j].color:
                                return False
                            elif piece_to_move.color != self.board[y-j][x+j].color and y-j != y1:
                                return False
                            elif piece_to_move.color != self.board[y-j][x+j].color and y-j == y1:
                                    return True
                        elif y-j == y1:
                            return True
                    return False
                elif piece_to_move.movement(origin,destination) == "horizontal":
                    a = x1-x 
                    if a < 0:
                        a *= -1
                        for i in range(1,a+1):
                            if type(self.board[y1][x-i]) != str:
                                if piece_to_move.color == self.board[y1][x-i].color:
                                    return False
                                elif piece_to_move.color != self.board[y1][x-i].color and x-i != x1:
                                    return False
                                elif piece_to_move.color != self.board[y1][x-i].color and x-i == x1:
                                    return True
                                return False
                            elif x-i == x1:
                                return True
                        return False
                    else:
                        for i in range(1,a+1):
                            if type(self.board[y1][x+i]) != str:
                                if piece_to_move.color == self.board[y1][x+i].color:
                                    return False
                                elif piece_to_move.color != self.board[y1][x+i].color and x+i != x1:
                                    return False
                                elif piece_to_move.color != self.board[y1][x+i].color and x+i == x1:
                                    return True
                                return False
                            elif x+i == x1:
                                return True
                        return False
                    return False
                if piece_to_move.movement(origin,destination) == "vertical":
                    a = y1-y 
                    if a < 0:
                        a *= -1
                        for i in range(1,a+1):
                            if type(self.board[y-i][x1]) != str:
                                if piece_to_move.color == self.board[y-i][x1].color:
                                    return False
                                elif piece_to_move.color != self.board[y-i][x1].color and y-i != y1:
                                    return False
                                elif piece_to_move.color != self.board[y-i][x1].color and y-i == y1:
                                    return True
                                return False
                            if y-i == y1:
                                return True
                        return False 
                    else:
                        for i in range(1,a+1):
                            if type(self.board[y+i][x1]) != str:
                                if piece_to_move.color == self.board[y+i][x].color:
                                    return False
                                elif piece_to_move.color != self.board[y+i][x1].color and y+i != y1:
                                    return False
                                elif piece_to_move.color != self.board[y+i][x1].color and y+i == y1:
                                    return True
                                return False
                            elif y+i == y1:
                                return True
                        return False     
                    return False
                return False
            return False
    
    def valid_piece(self,origin,player):
        """
        this function will recognize that when a piece is valid to move
        or not in diffetrent situations like check, checkmate, play with 
        wrong colour,....
        """
        x = int(origin[0])
        y = int(origin[1])
        if type(self.board[y][x]) == str:
            return False 
        if player == "White" and self.board[y][x].color == "w":
            return True
        elif player == "Black" and self.board[y][x].color == "b":
            return True
        return False
    
    def update_player(self,player:int):
        """
        this function will update player after each move
        """
        if player == "White":
            player = "Black"
            return player
        else:
            player = "White"
            return player   
    
    def factory(self,old_piece,new_piece,player):
        """this function is for making new objects"""
        x = int(old_piece[0])
        y = int(old_piece[1])
        if new_piece == "Q" and player == "White":
            self.board[y][x] = Queen("w")
            return str(x)+str(y)
        elif new_piece == "Q" and player == "Black":
            self.board[y][x] = Queen("b")
            return str(x)+str(y)
        elif new_piece == "R" and player == "White":
            self.board[y][x] = Rook("w")
            return str(x)+str(y)
        elif new_piece == "R" and player == "Black":
            self.board[y][x] = Rook("b")
            return str(x)+str(y)
        elif new_piece == "B" and player == "White":
            self.board[y][x] = Rook("w")
            return str(x)+str(y)
        elif new_piece == "B" and player == "Black":
            self.board[y][x] = Rook("b")
            return str(x)+str(y)
        elif new_piece == "N" and player == "White":
            self.board[y][x] = Rook("w")
            return str(x)+str(y)
        elif new_piece == "N" and player == "Black":
            self.board[y][x] = Rook("b")
            return str(x)+str(y)

    def castle(self,side,player):
        """
        this function will happens once for each player instead update board
        when a player wants to do castle
        """
        if side == "castle king" and player == "White":
            temp = self.board[1][4]
            self.board[1][4] = self.board[1][2]
            self.board[1][2] = temp
            temp = self.board[1][1]
            self.board[1][1] = self.board[1][3]
            self.board[1][3] = temp
            for i in self.board:
                for c in i:
                    print(c,end = " ")
                print()
            return '------------------------'
        elif side == "castle queen" and player == "White":
            temp = self.board[1][4]
            self.board[1][4] = self.board[1][6]
            self.board[1][6] = temp
            temp = self.board[1][8]
            self.board[1][8] = self.board[1][5]
            self.board[1][5] = temp
            for i in self.board:
                for c in i:
                    print(c,end = " ")
                print()
            return '------------------------'
        if side == "castle king" and player == "Black":
            temp = self.board[8][4]
            self.board[8][4] = self.board[8][2]
            self.board[8][2] = temp
            temp = self.board[8][1]
            self.board[8][1] = self.board[8][3]
            self.board[8][3] = temp
            for i in self.board:
                for c in i:
                    print(c,end = " ")
                print()
            return '------------------------'
        elif side == "castle queen" and player == "Black":
            temp = self.board[8][4]
            self.board[8][4] = self.board[8][6]
            self.board[8][6] = temp
            temp = self.board[8][8]
            self.board[8][8] = self.board[8][5]
            self.board[8][5] = temp
            for i in self.board:
                for c in i:
                    print(c,end = " ")
                print()
            return '------------------------'

    def check(self,player):
        kx = 0
        ky = 0
        if player == "White":
            for j in range(1,len(self.board)):
                for i in range(1,len(self.board[j])):
                    if type(self.board[j][i]) == King and self.board[j][i].color == "w":
                        kx = str(i)
                        ky = str(j)
            if kx == 0 and ky == 0:
                return "checkmate"
            for y in range(1,len(self.board)):
                for x in range(1,len(self.board[y])):
                    if type(self.board[y][x]) != str and int:
                        if type(self.board[y][x]) != King and self.board[y][x].color == "b":
                            if self.valid_move(str(x)+str(y),kx+ky) == True:
                                return True
                            elif self.valid_move(str(x)+str(y),kx+ky) == "cap":
                                return True
            return False
        elif player == "Black":
            for j in range(1,len(self.board)):
                for i in range(1,len(self.board[j])):
                    if type(self.board[j][i]) == King and self.board[j][i].color == "b":
                        kx = str(i)
                        ky = str(j)
            if kx == 0 and ky == 0:
                return "checkmate"
            for y in range(1,len(self.board)):
                for x in range(1,len(self.board[y])):
                    if type(self.board[y][x]) != str and int:    
                        if type(self.board[y][x]) != King and self.board[y][x].color == "w":
                            if self.valid_move(str(x)+str(y),kx+ky) == True:
                                return True
                            elif self.valid_move(str(x)+str(y),kx+ky) == "cap":
                                return True
            return False
        return False  

def main():
    """
    this function will include the loops which play the role of 
    engine in the game and will recognize that game over is true or not.
    """
    game = Game()
    player = "White"
    alph_to_num = {"a":8,"b":7,"c":6,"d":5,"e":4,"f":3,"g":2,"h":1}
    gameover = False
    print(game.display_board())
    while gameover is not True:
        if game.check(player) == True:
            print("CHECK  !!!!!!!!!")
        origin = input("which piece would you like to move?")
        x = origin[0]
        y = origin[1]
        for k in alph_to_num.keys():
            if x == k:
                x = alph_to_num[k]
                break
        origin = str(x) + y
        while not game.valid_piece(origin,player):
            origin = input("pick a valid piece ")
            x = origin[0]
            y = origin[1]
            for k in alph_to_num.keys():
                if x == k:
                    x = alph_to_num[k]
                    break
            origin = str(x) + y
        destination = input("where would you like to move?")
        x1 = destination[0]
        y1 = destination[1]
        for i in alph_to_num.keys():
            if x1 == i:
                x1 = alph_to_num[i]
                break
        destination = str(x1) + y1
        while game.valid_move(origin,destination) == False:
            destination = input("pick a valid move.")
            x1 = destination[0]
            y1 = destination[1]
            for i in alph_to_num.keys():
                if x1 == i:
                    x1 = alph_to_num[i]
                    break
            destination = str(x1) + y1
        if game.valid_move(origin,destination) == "cap":
            new_piece = input("what piece do you want to take in? (Q,R,B,N)")
            origin = game.factory(origin,new_piece,player)
        if game.valid_move(origin,destination) == "castle king" or game.valid_move(origin,destination) == "castle queen":
            print(game.castle(game.valid_move(origin,destination),player))
        else:
            print(game.update_board(origin,destination,player))
        player = game.update_player(player)
        if game.check(player) == "checkmate":
            gameover = True
    player = game.update_player(player)
    print("Check Mate!",player,"won.")
if __name__ == "__main__":
    main()

