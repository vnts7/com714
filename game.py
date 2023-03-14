import math
from gomoku_ui import GomokuUI
from board import Board
from player import Player
from constants import Constants

class Game:
    def __init__(self, board: Board, player_human: Player, player_comp: Player, first):
        self.board = board
        self.player_human = player_human
        self.player_comp = player_comp
        self.ui = GomokuUI(board.size)
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
        return self.board.is_full() or self.board.has_winner() is not None
    
    def alpha_beta_pruning(self, player, alpha, beta, depth):
        if depth == 0 or self.board.has_winner() is not None:
            return self.board.evaluate(), None, None

        if player == self.player_comp:
            x, y = None, None
            max_score = -math.inf
            for i in range(self.board.size):
                for j in range(self.board.size):
                    if self.board.grid[i][j] == None:
                        self.board.grid[i][j] = Constants.COMP
                        score, _, _ = self.alpha_beta_pruning(
                           self.player_human, alpha, beta, depth-1)
                        self.board.grid[i][j] = None
                        if (score > max_score):
                            x, y = i, j
                            max_score = score
                        alpha = max(alpha, score)
                        if beta <= alpha:
                            break
            return max_score, x, y
        else:
            x, y = None, None
            min_score = math.inf
            for i in range(self.board.size):
                for j in range(self.board.size):
                    if self.board.grid[i][j] == None:
                        self.board.grid[i][j] = Constants.HUMAN
                        score, _, _ = self.alpha_beta_pruning(
                            self.player_comp, alpha, beta, depth-1)
                        self.board.grid[i][j] = None
                        if (score < min_score):
                            x, y = i, j
                            min_score = score
                        beta = min(beta, score)
                        if beta <= alpha:
                            break
            return min_score, x, y
    
    def handle_comp_turn(self):
        if self.is_game_over():
            return
        
        depth = self.board.count_empty_cell()
        print(f'Computer turn [{self.player_comp.symbol}]')
        size = self.board.size
        if depth == size* size:
            x = math.floor(size/2)
            y = math.floor(size/2)
        else:
            if (depth > 2):
                depth = 2
            _, x, y = self.alpha_beta_pruning(self.player_comp, -math.inf, math.inf, depth)
        self.board.set_move(x, y, Constants.COMP)
        self.draw_ui()

    def handle_human_turn(self):
        if self.is_game_over():
            return
        print(f'Human turn [{self.player_human.symbol}]')
        is_choose = False
        while not is_choose:
            row, col = self.ui.handle_click_events()
            if self.board.set_move(row, col, Constants.HUMAN):
                is_choose = True
                break
            else:
                continue
        self.draw_ui()
        

    def draw_ui(self):
        self.ui.fill_screen()
        self.ui.draw_grid()
        self.ui.draw_board(self.board.grid, self.player_human.symbol, self.player_comp.symbol)
        self.ui.update()
    
    def start_game(self):
        self.draw_ui()
        while (not self.is_game_over()):
            if(self.current_player == self.player_comp):
                self.handle_comp_turn()
            else:
                self.handle_human_turn()
            self.switch_player()
            