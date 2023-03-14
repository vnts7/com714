class Game:
    def __init__(self, size, player1, player2):
        self.board = Board(size)
        self.player1 = player1
        self.player2 = player2
        self.current_player = player1

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
