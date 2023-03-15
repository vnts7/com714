from game import Game
from player import Player
from board import Board
from constants import Constants

def get_input():
    size = 0
    human_symbol = ''  # X or O
    comp_symbol = ''  # X or O
    first = ''
    while size < 6:
        try:
            print('')
            size = int(input('Input size of the board (>=6): '))
        except (KeyError, ValueError):
            print('Bad choice')

    while human_symbol != 'O' and human_symbol != 'X':
        try:
            print('')
            human_symbol = input('Choose X or O\nChosen: ').upper()
        except (KeyError, ValueError):
            print('Bad choice')

    if human_symbol == 'X':
        comp_symbol = 'O'
    else:
        comp_symbol = 'X'

    while first != 'Y' and first != 'N':
        try:
            first = input('First to start?[y/n]: ').upper()
        except (KeyError, ValueError):
            print('Bad choice')
    return size, human_symbol, comp_symbol, first


def main():
    size, human_symbol, comp_symbol, first = get_input()
    player_human = Player(human_symbol, Constants.HUMAN)
    player_comp = Player(comp_symbol, Constants.COMP)
    board = Board(size)
    game = Game(board, player_human, player_comp, first)
    game.start_game()

main()
