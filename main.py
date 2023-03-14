from game import Game
from player import Player
from board import Board


def get_input():
    size = 0
    h_choice = ''  # X or O
    c_choice = ''  # X or O
    first = ''
    while size < 6:
        try:
            print('')
            size = int(input('Input size of the board (>=6): '))
        except (KeyError, ValueError):
            print('Bad choice')

    while h_choice != 'O' and h_choice != 'X':
        try:
            print('')
            h_choice = input('Choose X or O\nChosen: ').upper()
        except (KeyError, ValueError):
            print('Bad choice')

    if h_choice == 'X':
        c_choice = 'O'
    else:
        c_choice = 'X'

    while first != 'Y' and first != 'N':
        try:
            first = input('First to start?[y/n]: ').upper()
        except (KeyError, ValueError):
            print('Bad choice')
    return size, h_choice, c_choice, first

def main():
    size, h_choice, c_choice, first = get_input()
    player1 = Player(h_choice, False)
    player2 = Player(c_choice, True)
    board = Board(size)
    game = Game(board, player1, player2, first)
    game.start_game()


