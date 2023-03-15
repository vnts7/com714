from constants import Constants
import math

class Board:
    def __init__(self, size):
        self.size = size
        # Create a 2D array size*size, init value of element is None
        self.grid = [[None for _ in range(size)] for _ in range(size)]

    # get all lines 5 cells and 6 cells
    def get_all_lines(self):
        grid = self.grid
        n = len(grid)
        lines = []
        # horizontal lines
        for row in range(n):
            for col in range(n-4):
                lines.append([grid[row][col:col+5]])
                self.append_info_last_line(lines, 'H', row, col)

            for col in range(n-5):
                lines.append([grid[row][col:col+6]])
                self.append_info_last_line(lines, 'H', row, col)

        # vertical lines
        for row in range(n):
            for col in range(n-4):
                lines.append([[grid[k][row] for k in range(col, col+5)]])
                self.append_info_last_line(lines, 'V', col, row)
            for col in range(n-5):
                lines.append([[grid[k][row] for k in range(col, col+6)]])
                self.append_info_last_line(lines, 'V', col, row)

        # diagonal lines
        for row in range(n-4):
            for col in range(n-4):
                lines.append([[grid[row+k][col+k] for k in range(5)]])
                self.append_info_last_line(lines, 'D1', row, col)

                lines.append([[grid[row+k][col+4-k] for k in range(5)]])
                self.append_info_last_line(lines, 'D2', row, col)

        for row in range(n-5):
            for col in range(n-5):
                lines.append([[grid[row+k][col+k] for k in range(6)]])
                self.append_info_last_line(lines, 'D1', row, col)

                lines.append([[grid[row+k][col+5-k] for k in range(6)]])
                self.append_info_last_line(lines, 'D2', row, col)

        return lines

    def is_empty_cell(self, row, col):
        return self.grid[row][col] == None

    def is_full(self):
        for row in range(self.size):
            for col in range(self.size):
                if self.is_empty_cell(row, col):
                    return False
        return True

    def append_info_last_line(self, lines, type, row, col):
        lines[-1].append(type)
        lines[-1].append((row, col))

    def count_empty_cell(self):
        count = 0
        for row in range(self.size):
            for col in range(self.size):
                if self.is_empty_cell(row, col):
                    count += 1
        return count

    def has_winner(self):
        lines = self.get_all_lines()
        for line in lines:
            if (self.score_line(line) == Constants.FIVE_IN_A_ROW_SCORE):
                return Constants.COMP
            if (self.score_line(line) == -Constants.FIVE_IN_A_ROW_SCORE):
                return Constants.HUMAN
        return None

    def score_line(self, line):
        score = 0
        line = line[0]
        try:
            if (len(line) == 6):
                score += Constants.SCORE_DICT_COMP_6[tuple(line)]
            else:
                score += Constants.SCORE_DICT_COMP_5[tuple(line)]
        except (KeyError):
            score += 0
        try:
            if (len(line) == 6):
                score += Constants.SCORE_DICT_HUMAN_6[tuple(line)]
            else:
                score += Constants.SCORE_DICT_HUMAN_5[tuple(line)]
        except (KeyError):
            score += 0
        return score

    def evaluate(self):
        score = 0
        lines = self.get_all_lines()
        for line in lines:
            score += self.score_line(line)
        return score

    def set_move(self, x, y, player_name):
        if (self.grid[x][y] == None):
            self.grid[x][y] = player_name
            return True
        else:
            return False

    def alpha_beta_pruning(self, player_name, alpha, beta, depth):
        if depth == 0 or self.has_winner() is not None:
            return self.evaluate(), None, None

        grid = self.grid
        if player_name == Constants.COMP:
            x, y = None, None
            max_score = -math.inf
            for i in range(self.size):
                for j in range(self.size):
                    if grid[i][j] == None:
                        grid[i][j] = Constants.COMP
                        score, _, _ = self.alpha_beta_pruning(
                            Constants.HUMAN, alpha, beta, depth-1)
                        grid[i][j] = None
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
            for i in range(self.size):
                for j in range(self.size):
                    if grid[i][j] == None:
                        grid[i][j] = Constants.HUMAN
                        score, _, _ = self.alpha_beta_pruning(
                            Constants.COMP, alpha, beta, depth-1)
                        grid[i][j] = None
                        if (score < min_score):
                            x, y = i, j
                            min_score = score
                        beta = min(beta, score)
                        if beta <= alpha:
                            break
            return min_score, x, y

    def ai_choose_next_move(self):
        next_move = None
        lines = self.get_all_lines()
        list_function = [self.is_three_in_a_row_comp_line,
                         self.is_blocked_four_human_line, self.is_blocked_four_comp_line]
        for i in range(len(list_function)):
            for line in lines:
                if (list_function[i](line)):
                    next_move = self.get_coordinate_of_none_in_line(line)
        return next_move

    def get_coordinate_of_none_in_line(self, line):
        index = line[0].index(None)
        try: 
            index = line[0].index(None, index + 1)
        except ValueError:
            pass
        if (line[1] == 'H'):
            return line[2][0], line[2][1] + index
        if (line[1] == 'V'):
            return line[2][0] + index, line[2][1]
        if (line[1] == 'D1'):
            return line[2][0] + index, line[2][1] + index
        if (line[1] == 'D2'):
            return line[2][0] + index, line[2][1] + len(line[0]) - 1 - index
        
    def is_blocked_four_human_line(self, line):
        if (self.score_line(line) == -Constants.BLOCKED_FOUR_SCORE):
            return True
        return False

    def is_blocked_four_comp_line(self, line):
        if (self.score_line(line) == Constants.BLOCKED_FOUR_SCORE):
            return True
        return False

    def is_three_in_a_row_comp_line(self, line):
        if (self.score_line(line) == Constants.THREE_IN_A_ROW_SCORE):
            return True
        return False
