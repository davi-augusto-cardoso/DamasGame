import sys

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
        count = 1
        sys.stdout.write("\033[0;32m" + "  a b c d e f g h\n" + "\033[0;0m")
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

    def __init__(self, board: Board, myPiecesColor: str = None):
        self.board          = board.board
        self.myPiecesColor  = myPiecesColor

    def fillBoard(self):
        i, j = 0, 0
        for row in self.board:
            for tile in row:
                if(tile.color == "black" and j < 3):
                    tile.piece = Piece("red", (i, j))
                elif(tile.color == "black" and j >= 5):
                    tile.piece = Piece("black", (i, j))
                i+=1
            i = 0
            j +=1 
            
    def play(self, startPosition: tuple, endPosition: tuple):
        tile        = self.board
        tileStart   = tile[startPosition[0]][startPosition[1]]
        tileEnd     = tile[endPosition[0]][endPosition[1]]
        
        piece = tileStart.piece
        playValid, makePoint = self.rulesGame(tileStart, tileEnd, startPosition, endPosition)
        
        # Verificando se a peça é uma dama e se a jogada é valida
        if(piece.dama and playValid):
        
            valueI = 1 if (endPosition[0]-startPosition[0]) >= 0 else -1
            valueJ = 1 if (endPosition[1]-startPosition[1]) >= 0 else -1
            j = startPosition[1]
            
            # Verificando se há alguma peça inimiga na diagonal percorrida pela da dama
            for i in range(startPosition[0]-abs(valueI), endPosition[0]-abs(valueI), valueI):
                j += valueJ
                if(tile[i][j].piece != None and tile[i][j].piece.color != piece.color):
                    tileEnd     = tile[j][i]
                    endPosition = (j, i) 
                    makePoint   = True  
                
  
        # Caso a jogada seja válida e não haja uma peça adversária no ponto de destino
        if(playValid and  (not makePoint)):
            if(piece.position[0] == 8 and piece.color == "red"):
                piece.dama = True
            elif(piece.position[0] == 0 and piece.color == "black"):
                piece.dama = True
                 
            tileEnd.piece = piece
            tileStart.piece = None
            
        # Caso a jogada seja válida e haja uma peça adversária no ponto de destino
        elif(playValid and makePoint):
            tileEnd.piece = None
            
            col, row = self.adjustDirection(startPosition, endPosition)
            
            tile[col][row].piece = piece
            tileStart.piece = None
                
        # Caso a jogada não seja válida
        else:
            print("Jogada inválida!")
    
        return playValid
    
    def  rulesGame(self, tileStart, tileEnd, startPosition, endPosition):
        
        # verificando se existe peça na posiçao inicial
        if(tileStart.piece == None):
            return False, False
        
        # Verificando se é um movimento diagonal
        if(abs(endPosition[0]-startPosition[0]) != abs(endPosition[1]-startPosition[1])):
            return False, False  
        
        # Verificando se a posição destino esta dentro do tabuleiro
        if(64 < (endPosition[0] * endPosition[1]) or
            (endPosition[0] * endPosition[1]) < 0):
            return False, False

        # Verificando se é uma peça comum
        if(not tileStart.piece.dama):
            # Verificando se o tile detino ultrapassa o alcance da peça
            if(abs(endPosition[0]-startPosition[0]) > 1 or abs(endPosition[1]-startPosition[1]) > 1 ):
                return False, False   

        # Verificando se a posição destino esta vazia 
        if(tileEnd.piece != None):
            # Verificando se há uma peça da mesma cor na posição destino
            if(tileStart.piece.color == tileEnd.piece.color):
                return False, False
            
            col, row = self.adjustDirection(startPosition, endPosition)
            
            # Verificando se há alguma peça na posição atrás da posição destino
            if(self.board[col][row].piece != None):
                return False, False
            
            else:
                return True, True
        
        return True, False
    
    def adjustDirection(self, startPosition: tuple, endPosition: tuple):
        columnPosition = startPosition[0]
        rowPosition    = startPosition[1]
        
        value = abs(endPosition[0]-startPosition[0])+1
        
        # Ajustando vertical
        if(endPosition[0]-startPosition[0] < 0):
            columnPosition -= value
        else:
            columnPosition += value
                
        # Ajustando horizontal
        if(endPosition[1]-startPosition[1] < 0):
            rowPosition -= value
        else:
            rowPosition += value
        
        return columnPosition, rowPosition 
           
board = Board()

player = Player(board)
player.fillBoard()
board.showTable()
player.play((2, 0), (3, 1))
board.showTable()
player.play((3, 1), (4, 2))
board.showTable()
player.play((5, 1), (4, 2))
board.showTable()
player.play((3, 3), (4, 4))
board.showTable()
board.board[4][4].piece.dama = True
player.play((1, 1), (2, 0))
board.showTable()
player.play((4, 4), (3, 3))
board.showTable()
player.play((2, 2), (3, 1))
board.showTable()
board.board[5][5].piece.dama = True
player.play((5, 5), (2, 2))
board.showTable()