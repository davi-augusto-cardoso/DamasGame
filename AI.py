from damas import Board, Player
from gameRules import Rules

class AI:
    def __init__(self, player):
        self.board = Board()
        
        self.player = player
        self.board = player.board 
        
        self.me = Player(self.board, player.myPiecesColor)
        
        self.myPiecesPosition = list()
        
        self.rules = Rules()
        
        self.lookBoard()
        self.makePlay(self.think())
        
    def lookBoard(self):
        
        piecesAmount = 0
        
        # Identificando onde estão minhas peças
        for row in self.board:
            for tile in row:
                if(tile.piece != None):
                    if(self.player.myPiecesColor == tile.piece.color):
                        self.myPiecesPosition.append(tile)
                        piecesAmount += 1 
        return piecesAmount
    
    def think(self):  
        possiblePlays = list()

        # Verificando o que posso mecher    
        for tile in self.myPiecesPosition:  
            piece = tile.piece
            top    = piece.position[0]+1
            right  = piece.position[1]+1
            bottom = piece.position[0]-1
            left   = piece.position[1]-1
            endPositions = [[top, right],
                            [bottom, right], 
                            [bottom, left],
                            [top, left]]
            # Verificando se é uma dama 
            if(piece.dama):
                pass
            
            # Verificando se é uma pedra
            else:   
                # Verificando se a jogada é válida
                for endPosition in endPositions:
                    if(self.rules.checkRules(self.me.board, piece.position, endPosition, self.me.myPiecesColor)[0]):
                        possiblePlays.append([piece.position, endPosition])
            
            myPlay = possiblePlays[0]
            
            for play in possiblePlays:
                self.me.play(play[0], play[1]) 
                
                if(self.lookBoard() < 12): 
                    myPlay = play
                    
            return myPlay    
        
        # Faz a jogada nas 4 posições com cada pedra
        
        # Faz a jogada nas 4 posições com cada dama
        
        # Verifica se o valor de cada joga a e seleciona o maior
    
    def makePlay(self, myPlay):
        self.player.play(myPlay[0], myPlay[1])
    

    
    