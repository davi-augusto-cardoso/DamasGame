import sys
from turtle import position

class Piece:
    def __init__(self, color: str = None, position: tuple = None, dama: bool = None):
        self.color = color
        self.position = position
        self.dama     = dama
        
class Tile:
    def __init__(self, color, piece, position):
        self.color = color
        self.piece = piece
        self.position = position
        
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
                    if(tile.piece.color == "black"):
                        sys.stdout.write("\033[0;31m" + "\u2B57 "+"\033[0;0m")
                    elif(tile.piece.color == "white"):
                        sys.stdout.write("\033[0;30m" + "\u2B57 "+"\033[0;0m")      
            sys.stdout.write("\n")   
        sys.stdout.write("\033[0;0m")  
    
    def clearConsole(self):
        pass
        
class Player:
    board = list()

    def __init__(self, board: Board):
        self.board = board.board

    def fillBoard(self):
        i, j = 0, 0
        for row in self.board:
            for tile in row:
                if(tile.color == "black" and j < 3):
                    tile.piece = Piece("black", (i, j))
                elif(tile.color == "black" and j >= 5):
                    tile.piece = Piece("white", (i, j))
                i+=1
            i = 0
            j +=1 
            
    def play(self, startPosition, endPosition):
        tile        = self.board
        tileStart   = tile[startPosition[0]][startPosition[1]]
        tileEnd     = tile[endPosition[0]][endPosition[1]]
        
        piece = tileStart.piece
        playValid, makePoint = self.rulesGame(tileStart, tileEnd, startPosition, endPosition)
        
        # Caso a jogada seja válida e não faça ponto
        if(playValid and  (not makePoint)):
            tileEnd.piece = piece
            tileStart.piece = None
            
        # Caso a jogada seja válida e haja uma peça adversária no ponto de destino
        elif(playValid and makePoint):
            tileEnd.piece = None
            
            columnPosition = piece.position[1]
            rowPosition    = piece.position[0]
            
            # Ajustando posição vertical da peça
            if(endPosition[0]-startPosition[0] < 0):
                columnPosition -=2
            else:
                columnPosition +=2
                
            # Ajustando posição horizontal da peça
            if(endPosition[1]-startPosition[1] < 0):
                rowPosition -=2
            else:
                rowPosition +=2
            
            tile[columnPosition][rowPosition].piece = piece
            tileStart.piece = None
                
        # Caso a jogada não seja válida
        else:
            print("Jogada inválida!")
    
    def  rulesGame(self, tileStart, tileEnd, endPosition, startPosition):
        # verificando se existe peça na posiçao inicial
        if(tileStart.piece == None):
            return False, False
        
        #Verificando se a posição destino da peça é um tile de cor preta
        elif(tileEnd.color != "black"):
            return False, False
        
        # Verificando se a posição destino esta dentro do tabuleiro
        elif(64 < (endPosition[0] * endPosition[1]) or
            (endPosition[0] * endPosition[1]) < 0):
            return False, False

            
        # Verificando se o tile detino ultrapassa o alcance da peça
        elif(abs(endPosition[0]-startPosition[0]) > 1 or abs(endPosition[1]-startPosition[1]) > 1 ):
            return False, False
        
        # Verificando se a posição destino esta vazia 
        elif(tileEnd.piece != None):
            # Verificando se há uma peça da mesma cor na posição destino
            if(tileStart.piece.color == tileEnd.piece.color):
                return False, False
            else:
                return True, True
        
        return True, False
        

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
player.play((2, 2), (3, 3))
board.showTable()