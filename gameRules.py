
class Rules:
    
    def __init__(self, tile):
        self.tile  = tile
    def checkRules(self, tileStart, tileEnd, startPosition, endPosition, myPiecesColor):
        # verificando se existe peça na posiçao inicial
        if(tileStart.piece == None):
            return False, False
        
        # Verificando se o jogador está tentando mover uma peça adversária
        if(myPiecesColor != tileStart.piece.color):
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
            
            # Verificando se a pedra esta andando para frente
            if(tileStart.piece.color == "red"):
                if((endPosition[0]-startPosition[0]) < 0):
                    return False, False
            else:
                if((endPosition[0]-startPosition[0]) > 0):
                    return False, False
                
            # Verificando se o tile detino ultrapassa o alcance da peça
            if(abs(endPosition[0]-startPosition[0]) > 1 or abs(endPosition[1]-startPosition[1]) > 1 ):
                return False, False   
        else:
            valueI = 1 if (endPosition[0]-startPosition[0]) > 0 else -1
            valueJ = 1 if (endPosition[1]-startPosition[1]) > 0 else -1
            j = startPosition[1]
            
            # Verificando se há alguma peça amiga na diagonal percorrida pela da dama
            for i in range(startPosition[0]+valueI, endPosition[0]+valueI, valueI):
                j += valueJ
                if(self.tile[i][j].piece != None and self.tile[i][j].piece.color == tileStart.piece.color):
                    return False, False
                
        # Verificando se a posição destino esta vazia 
        if(tileEnd.piece != None):
            # Verificando se há uma peça da mesma cor na posição destino
            if(tileStart.piece.color == tileEnd.piece.color):
                return False, False
            
            col, row = self.checkDirection(startPosition, endPosition)
            
            # Verificando se há alguma peça na posição atrás da posição destino
            if(self.tile[col][row].piece != None):
                return False, False
            
            else:
                return True, True
        
        return True, False
    def checkDirection(self, startPosition: tuple, endPosition: tuple):
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