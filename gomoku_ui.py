import pygame
import sys
from constants import Constants

class GomokuUI:
    GRAY = (128, 128, 128)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    BLACK = (0, 0, 0)
    SQUARE_SIZE = 40
    def __init__(self, size):
        pygame.init()
        self.length = self.SQUARE_SIZE*size
        self.size = size
        self.screen = pygame.display.set_mode((self.length, self.length))
        pygame.display.set_caption(f"Gomoku Game {self.size} x {self.size}")
        self.font = pygame.font.SysFont(None, 30)

    def draw_board(self, grid, symbol_human, symbol_comp):
        for row in range(self.size):
            for col in range(self.size):
                if grid[row][col] == Constants.COMP:
                    self.draw_piece(row, col, symbol_comp)
                elif grid[row][col] == Constants.HUMAN:
                    self.draw_piece(row, col, symbol_human)

    def draw_piece(self, row, col, symbol):
        x = col * self.SQUARE_SIZE + self.SQUARE_SIZE // 2
        y = row * self.SQUARE_SIZE + self.SQUARE_SIZE // 2
        if (symbol == 'X'):
            pygame.draw.line(self.screen, self.BLACK, (x - self.SQUARE_SIZE // 3, y -
                            self.SQUARE_SIZE // 3), (x + self.SQUARE_SIZE // 3, y + self.SQUARE_SIZE // 3), 5)
            pygame.draw.line(self.screen, self.BLACK, (x - self.SQUARE_SIZE // 3, y +
                            self.SQUARE_SIZE // 3), (x + self.SQUARE_SIZE // 3, y - self.SQUARE_SIZE // 3), 5)
        else:
            pygame.draw.circle(self.screen, self.BLACK, (x, y), self.SQUARE_SIZE // 2 - 5)

    def draw_grid(self):
        for x in range(0, self.length, self.SQUARE_SIZE):
            pygame.draw.line(self.screen, self.GRAY, (x, 0), (x, self.length))
        for y in range(0, self.length, self.SQUARE_SIZE):
            pygame.draw.line(self.screen, self.GRAY, (0, y), (self.length, y))

    def draw_game(self, grid, symbol_human, symbol_comp):
        self.screen.fill(self.WHITE)
        self.draw_grid()
        self.draw_board(grid, symbol_human, symbol_comp)

    def draw_message(self, message):
        text = self.font.render(message, True, self.BLACK)
        text_rect = text.get_rect(center=(self.length//2, self.length-self.SQUARE_SIZE//2))
        self.screen.blit(text, text_rect)

    def update(self):
        pygame.display.update()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                col = mouse_pos[0] // self.SQUARE_SIZE
                row = mouse_pos[1] // self.SQUARE_SIZE
                return (row, col)
        return None