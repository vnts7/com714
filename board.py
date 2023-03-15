from constants import Constants


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
                lines.append(grid[row][col:col+5])
            for col in range(n-5):
                lines.append(grid[row][col:col+6])

        # vertical lines
        for row in range(n):
            for col in range(n-4):
                lines.append([grid[k][row] for k in range (col, col+5)])
            for col in range(n-5):
                lines.append([grid[k][row] for k in range (col, col+6)])
        # diagonal lines
        for row in range(n-4):
            for col in range(n-4):
                lines.append([grid[row+k][col+k] for k in range(5)])
                lines.append([grid[row+k][col+4-k] for k in range(5)])
        for row in range(n-5):
            for col in range(n-5):
                lines.append([grid[row+k][col+k] for k in range(6)])
                lines.append([grid[row+k][col+5-k] for k in range(6)])
        return lines

    def is_empty_cell(self, row, col):
        return self.grid[row][col] == None

    def is_full(self):
        for row in range(self.size):
            for col in range(self.size):
                if self.is_empty_cell(row, col):
                    return False
        return True

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

    def set_move(self, x, y, player):
        if (self.grid[x][y] == None):
            self.grid[x][y] = player
            return True
        else:
            return False

    def ai_choose_next_move(self):
        grid = self.grid
        n = len(grid)
        # horizontal lines
        for row in range(n):
            for col in range(n-4):
                line = grid[row][col:col+5]
                if (self.is_blocked_four_comp_line(line)):
                    index = line.index(None)
                    return row, col + index
                if (self.is_blocked_four_human_line(line)):
                    index = line.index(None)
                    return row, col + index
        # vertical lines
        for row in range(n):
            for col in range(n-4):
                line = [grid[k][row] for k in range (col, col+5)]
                if (self.is_blocked_four_comp_line(line)):
                    index = line.index(None)
                    return col + index, row
                if (self.is_blocked_four_human_line(line)):
                    index = line.index(None)
                    return col + index, row

        # diagonal lines
        for row in range(n-4):
            for col in range(n-4):
                line = [grid[row+k][col+k] for k in range(5)]
                if (self.is_blocked_four_comp_line(line)):
                    index = line.index(None)
                    return row + index, col + index
                if (self.is_blocked_four_human_line(line)):
                    index = line.index(None)
                    return row + index, col + index

                line = [grid[row+k][col+4-k] for k in range(5)]
                if (self.is_blocked_four_comp_line(line)):
                    index = line.index(None)
                    return row + index, col + 4 - index
                if (self.is_blocked_four_human_line(line)):
                    index = line.index(None)
                    return row + index, col + 4 - index
        return None

    def is_blocked_four_human_line(self, line):
        if (self.score_line(line) == -Constants.BLOCKED_FOUR_SCORE):
            return True
        return False

    def is_blocked_four_comp_line(self, line):
        if (self.score_line(line) == Constants.BLOCKED_FOUR_SCORE):
            return True
        return False
