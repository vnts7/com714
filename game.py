class Game:
    def __init__(self, board, player1, player2, first):
        self.board = board
        self.player1 = player1
        self.player2 = player2
        if (first == 'Y'):
            self.current_player = player1
        else:
            self.current_player = player2
             

    def switch_player(self):
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1

    def is_winner(self):
        for i in range(self.board.size):
            for j in range(self.board.size):
                    return True
        return False
    
    def start_game(self):
         pass
