from gomoku_ui import GomokuUI
from board import Board
from player import Player
class Game:
    def __init__(self, board: Board, player_human: Player, player_comp: Player, first):
        self.board = board
        self.player_human = player_human
        self.player_comp = player_comp
        if (first == 'Y'):
            self.current_player = player_human
        else:
            self.current_player = player_comp
             

    def switch_player(self):
        if self.current_player == self.player_human:
            self.current_player = self.player_comp
        else:
            self.current_player = self.player_human
    
    def is_game_over(self):
        return self.board.is_full() or self.board.has_winner()
    
    def handle_comp_turn(self, c_choice, h_choice, size):
        if self.is_game_over():
            return
        
        depth = count_empty_cell(board)

        clean()
        print(f'Computer turn [{c_choice}]')

        if depth == size * size:
            x = math.floor(size/2)
            y = math.floor(size/2)
        else:
            if (depth > 2):
                depth = 2
            _, x, y = alpha_beta_pruning(board, COMP, -math.inf, math.inf, depth)
        set_move(x, y, COMP)
        screen.fill(WHITE)
        draw_grid()
        draw_board(board, h_choice, c_choice)
    
    def start_game(self):
        while (not self.is_game_over()):
            if(self.current_player == self.player_comp):
                self.handle_comp_turn()
            else:
                self.handle_human_turn()