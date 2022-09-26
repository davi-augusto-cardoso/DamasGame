from damas import *

class Game:
    def __init__(self):
        self.gameStart()
        
    def gameStart(self):
        board = Board()
        
        player1 = Player(Board, str(input("Escolha a cor das suas peças:\n 1-Vermelhas\n 2-Pretas")))
        player2 = Player(Board)
        
        player1.fillBoard()
        player1.fillBoard()
        
        board.showTable()
        while(True):
            
        
    def gameStop(self):