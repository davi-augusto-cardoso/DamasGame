from damas import *

class Game:
    def __init__(self):
        self.gameStart()
        
    def gameStart(self):
        board = Board()
        
        # Escolhendo as cores de cada joagador
        chooseColor = -1
        while(chooseColor < 0):
            chooseColor = int(input("Escolha a cor das suas peças:\n 1-Vermelhas\n 2-Pretas\n"))
        colorPlayer1 = "red" if chooseColor == 1 else "black"
        colorPlayer2 = "red" if colorPlayer1 == "black" else "black"
        
        player1 = Player(board, colorPlayer1)
        player2 = Player(board, colorPlayer2)
        
        player1.fillBoard()
        
        turn = 0
        while(True):
            board.showTable()
            
            # Os turnos pares serão os turnos do player 1
            if(turn % 2 == 0):
                start = (int(input("Coluna origem: ")), int(input("Linha origem: ")))
                end = (int(input("Coluna destino: ")), int(input("Linha destino: ")))
                isvalid = player1.play(start, end)
                if isvalid : turn += 1
            # Os turnos ímpares serão os turnos do player 1
            else:
                start = (int(input("Coluna origem: ")), int(input("Linha origem: ")))
                end = (int(input("Coluna destino: ")), int(input("Linha destino: ")))
                isvalid = player2.play(start, end)
                if isvalid : turn += 1
            
Game()
