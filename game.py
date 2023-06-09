from ui_helper import UIHelper
from board import Board
from player import Player
import pygame
import math
import random


class Game:

  def __init__(self, board: Board, player_human: Player, player_comp: Player, first):
    self.board = board
    self.player_human = player_human
    self.player_comp = player_comp
    self.ui = board.ui
    self.first = first
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

  def handle_comp_turn(self):
    if self.is_game_over():
      return
    print(f'Computer turn [{self.current_player.symbol}]')

    x,y = self.board.ai_next_move()
    self.board.set_move(x, y, self.current_player)

  def handle_human_turn(self):
    if self.is_game_over():
      return
    print(f'Human turn [{self.current_player.symbol}]')
    is_choose = False
    while not is_choose:
      row, col = self.handle_human_choose_cell_event()
      if self.board.set_move(row, col, self.current_player):
        is_choose = True
        break
      else:
        continue

  def handle_human_choose_cell_event(self):
    while True:
      for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
          col = event.pos[0] // self.ui.SQUARE_SIZE
          row = event.pos[1] // self.ui.SQUARE_SIZE
          if (row < self.ui.size and col < self.ui.size):
            return row, col
        if event.type == pygame.QUIT:
          exit()

  def handle_click_restart_button_event(self):
    for event in pygame.event.get():
      if event.type == pygame.MOUSEBUTTONUP:
        mouse_pos = pygame.mouse.get_pos()
        if self.ui.button_rect.collidepoint(mouse_pos):
          self.restart_game()
      if event.type == pygame.QUIT:
        exit()

  def show_notification(self):
    if self.board.has_winner() == self.player_human.name:
      self.ui.draw_message('YOU WIN')
    elif self.board.has_winner() == self.player_comp.name:
      self.ui.draw_message('YOU LOSE')
    else:
      self.ui.draw_message('DRAW')
    pygame.display.update()

  def show_restart_button(self):
    self.ui.draw_button()
    pygame.display.update()

  def start_game(self):
    self.ui.draw_board()
    while (not self.is_game_over()):
      if (self.current_player == self.player_comp):
        self.handle_comp_turn()
      else:
        self.handle_human_turn()
      self.switch_player()
      pygame.time.Clock().tick(60)
    #--game over
    self.show_notification()
    self.show_restart_button()
    while (True):
      self.handle_click_restart_button_event()

  def restart_game(self):
    self.__init__(Board(self.board.size), Player(self.player_human.symbol, self.player_human.name),
                  Player(self.player_comp.symbol, self.player_comp.name), self.first)
    self.start_game()
