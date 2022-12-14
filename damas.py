import sys
from gameRules import Rules

class Piece:
    def __init__(self, color: str = None, position: tuple = None, dama: bool = False):
        self.color      = color
        self.position   = position
        self.dama       = dama
        
class Tile:
    def __init__(self, color: str, piece: Piece, position: tuple):
        self.color      = color
        self.piece      = piece
        self.position   = position
        
class Board:

    board = list()
             
    def __init__(self):
        self.generateBoard()

    def generateBoard(self):
        key = 0

        for i in range(8):
            row = list()
            for j in range(8):
                if(key == 0):
                    color = "black"
                    key = 1
                else:
                    color = "white"
                    key = 0     
                row.append(Tile(color, None, (i, j))) 
            key = 1 if key == 0 else 0
            self.board.append(row)

    def showTable(self):
        count = 0
        sys.stdout.write("\033[0;32m" + "  0 1 2 3 4 5 6 7\n" + "\033[0;0m")
        for row in self.board:
            sys.stdout.write("\033[0;32m" +str(count)+ "\033[0;0m") 
            count += 1 
            for tile in row:
                if(tile.piece == None): 
                    if(tile.color == "black"):
                        sys.stdout.write("\u2B1B")
                    elif(tile.color == "white"):
                        sys.stdout.write("\u2B1C")   
                else:
                    if(tile.piece.color == "red"):
                        sys.stdout.write("\033[0;31m" + "\u2B57 "+"\033[0;0m")
                    elif(tile.piece.color == "black"):
                        sys.stdout.write("\033[0;30m" + "\u2B57 "+"\033[0;0m")      
            sys.stdout.write("\n")   
        sys.stdout.write("\033[0;0m")  
    
    def clearConsole(self):
        pass
        
class Player:
    board = list()

    def __init__(self, board: list, myPiecesColor: str = None):
        self.board          = board
        self.myPiecesColor  = myPiecesColor
        
        self.rules = Rules()

    # Colocando as pe??as nas suas posi????es iniciais
    def fillBoard(self):
        i, j = 0, 0
        for row in self.board:
            for tile in row:
                if(tile.color == "black" and j < 3):
                    tile.piece = Piece("red", (j, i))
                elif(tile.color == "black" and j >= 5):
                    tile.piece = Piece("black", (j, i))
                i+=1
            i = 0
            j +=1 
            
    def play(self, startPosition: tuple, endPosition: tuple):
        tile        = self.board
        tileStart   = tile[startPosition[0]][startPosition[1]]
        tileEnd     = tile[endPosition[0]][endPosition[1]]
        
        piece = tileStart.piece
        playValid, makePoint = self.rules.checkRules(self.board, startPosition, endPosition, self.myPiecesColor)
        
        # Verificando se a pe??a ?? uma dama e se a jogada ?? valida
        if(piece.dama and playValid):
        
            valueI = 1 if (endPosition[0]-startPosition[0]) > 0 else -1
            valueJ = 1 if (endPosition[1]-startPosition[1]) > 0 else -1
            j = startPosition[1]
            
            # Verificando se h?? alguma pe??a inimiga na diagonal percorrida pela da dama
            for i in range(startPosition[0]+valueI, endPosition[0]+valueI, valueI):
                j += valueJ
                if(tile[i][j].piece != None and tile[i][j].piece.color != piece.color):
                    tileEnd     = tile[i][j]
                    endPosition = (i, j) 
                    makePoint   = True  
                
  
        # Caso a jogada seja v??lida e n??o haja uma pe??a advers??ria no ponto de destino
        if(playValid and  (not makePoint)):
            if(piece.position[0] == 8 and piece.color == "red"):
                piece.dama = True
            elif(piece.position[0] == 0 and piece.color == "black"):
                piece.dama = True
                 
            tileEnd.piece = piece
            tileStart.piece = None
            
        # Caso a jogada seja v??lida e haja uma pe??a advers??ria no ponto de destino
        elif(playValid and makePoint):
            tileEnd.piece = None
            
            col, row = self.rules.checkDirection(startPosition, endPosition)
            
            tile[col][row].piece = piece
            tileStart.piece = None
                
        # Caso a jogada n??o seja v??lida
        else:
            print("Jogada inv??lida!")
    
        return playValid


# board = Board()

# player1 = Player(board, "red")
# player2 = Player(board, "black")
# player1.fillBoard()
# board.showTable()

# board.board[2][0].piece.dama = True
# player1.play((2,0), (3,1))
# board.showTable()
# player1.play((2,0), (4,2))
# board.showTable()
# board.board[5][3].piece.dama = True
# player2.play((5,1), (4,2))
# board.showTable()
# player2.play((5,3), (3,1))
# board.showTable()