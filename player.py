class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
        self.moves = []

    def add_move(self, move):
        self.moves.append(move)