class Player:
    def __init__(self, symbol, is_ai):
        self.symbol = symbol
        self.is_ai = is_ai
        self.moves = []

    def add_move(self, move):
        self.moves.append(move)