import random
from constants import Constants
import math

from ui_helper import UIHelper
from player import Player
from enum import Enum


class Direction(Enum):
  VERTICAL = 1
  HORIZONTAL = 2
  DIAGONAL1 = 3
  DIAGONAL2 = 4


class Line:

  def __init__(self, data: list, direction: Direction, pos: tuple):
    self.data = data
    self.direction = direction
    self.pos = pos


class Board:

  def __init__(self, size):
    self.size = size
    # Create a 2D array size*size, init value of element is None
    self.grid = [[None for _ in range(size)] for _ in range(size)]
    self.ui = UIHelper(size)

  # get all lines 5 cells and 6 cells
  def get_all_lines(self):
    grid = self.grid
    n = len(grid)
    lines: list[Line] = []
    # horizontal lines
    for row in range(n):
      for col in range(n - 4):
        lines.append(Line(grid[row][col:col + 5], Direction.HORIZONTAL, (row, col)))

      for col in range(n - 5):
        lines.append(Line(grid[row][col:col + 6], Direction.HORIZONTAL, (row, col)))

    # vertical lines
    for row in range(n):
      for col in range(n - 4):
        lines.append(Line(
            [grid[k][row] for k in range(col, col + 5)],
            Direction.VERTICAL,
            (col, row),
        ))
      for col in range(n - 5):
        lines.append(Line(
            [grid[k][row] for k in range(col, col + 6)],
            Direction.VERTICAL,
            (col, row),
        ))

    # diagonal lines
    for row in range(n - 4):
      for col in range(n - 4):
        lines.append(Line(
            [grid[row + k][col + k] for k in range(5)],
            Direction.DIAGONAL1,
            (row, col),
        ))

        lines.append(Line(
            [grid[row + k][col + 4 - k] for k in range(5)],
            Direction.DIAGONAL2,
            (row, col),
        ))

    for row in range(n - 5):
      for col in range(n - 5):
        lines.append(Line(
            [grid[row + k][col + k] for k in range(6)],
            Direction.DIAGONAL1,
            (row, col),
        ))

        lines.append(Line(
            [grid[row + k][col + 5 - k] for k in range(6)],
            Direction.DIAGONAL2,
            (row, col),
        ))

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
    # line []
    for line in lines:
      if self.score_line(line) == Constants.FIVE_IN_A_ROW_SCORE:
        return Constants.COMP
      if self.score_line(line) == -Constants.FIVE_IN_A_ROW_SCORE:
        return Constants.HUMAN
    return None

  def score_line(self, line: Line):
    score = 0
    data = line.data
    try:
      if len(data) == 6:
        score += Constants.SCORE_DICT_COMP_6[tuple(data)]
      else:
        score += Constants.SCORE_DICT_COMP_5[tuple(data)]
    except KeyError:
      score += 0
    try:
      if len(data) == 6:
        score += Constants.SCORE_DICT_HUMAN_6[tuple(data)]
      else:
        score += Constants.SCORE_DICT_HUMAN_5[tuple(data)]
    except KeyError:
      score += 0
    return score

  def evaluate(self):
    score = 0
    lines = self.get_all_lines()
    for line in lines:
      score += self.score_line(line)
    return score

  def set_move(self, x, y, player: Player):
    if self.grid[x][y] == None:
      self.grid[x][y] = player.name
      self.ui.draw_piece(x, y, player.symbol)
      return True
    else:
      return False

  def ai_next_move(self):
    depth = self.count_empty_cell()
    size = self.size
    if depth >= size * size - 2:
      x = math.floor(size / 2)
      y = math.floor(size / 2)
      while (self.grid[x][y] != None):
        x = random.randint(math.floor(size / 2) - 2, math.floor(size / 2) + 2)
        y = random.randint(math.floor(size / 2) - 2, math.floor(size / 2) + 2)
    else:
      result = self.obvious_ai_move()
      if (result is not None):
        x, y = result
      else:
        if (depth > 2):
          depth = 2
        _, x, y = self.alpha_beta_pruning(Constants.COMP, -math.inf, math.inf, depth)
    return x, y

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
            score, _, _ = self.alpha_beta_pruning(Constants.HUMAN, alpha, beta, depth - 1)
            grid[i][j] = None
            if score > max_score:
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
            score, _, _ = self.alpha_beta_pruning(Constants.COMP, alpha, beta, depth - 1)
            grid[i][j] = None
            if score < min_score:
              x, y = i, j
              min_score = score
            beta = min(beta, score)
            if beta <= alpha:
              break
      return min_score, x, y

  def obvious_ai_move(self):
    lines = self.get_all_lines()
    list_function = [
        self.is_blocked_four_comp_line,
        self.is_blocked_four_human_line,
        self.is_three_in_a_row_comp_line,
    ]
    for i in range(len(list_function)):
      for line in lines:
        if list_function[i](line):
          return self.get_coordinate_of_none_in_line(line)
    return None

  def get_coordinate_of_none_in_line(self, line: Line):
    index = line.data.index(None)
    try:
      index = line.data.index(None, index + 1)
    except ValueError:
      pass
    direction = line.direction
    pos = line.pos
    if direction == Direction.HORIZONTAL:
      return pos[0], pos[1] + index
    if direction == Direction.VERTICAL:
      return pos[0] + index, pos[1]
    if direction == Direction.DIAGONAL1:
      return pos[0] + index, pos[1] + index
    if direction == Direction.DIAGONAL2:
      return pos[0] + index, pos[1] + len(line.data) - 1 - index

  def is_blocked_four_human_line(self, line):
    if self.score_line(line) == -Constants.BLOCKED_FOUR_SCORE:
      return True
    return False

  def is_blocked_four_comp_line(self, line):
    if self.score_line(line) == Constants.BLOCKED_FOUR_SCORE:
      return True
    return False

  def is_three_in_a_row_comp_line(self, line):
    if self.score_line(line) == Constants.THREE_IN_A_ROW_SCORE:
      return True
    return False
