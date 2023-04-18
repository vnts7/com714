import pygame
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
        self.font = pygame.font.SysFont(None, 50)
        
    def draw_piece(self, row, col, symbol):
        x = col * self.SQUARE_SIZE + self.SQUARE_SIZE // 2
        y = row * self.SQUARE_SIZE + self.SQUARE_SIZE // 2
        if (symbol == 'X'):
            pygame.draw.line(self.screen, self.BLACK, (x - self.SQUARE_SIZE // 3, y -
                                                       self.SQUARE_SIZE // 3), (x + self.SQUARE_SIZE // 3, y + self.SQUARE_SIZE // 3), 5)
            pygame.draw.line(self.screen, self.BLACK, (x - self.SQUARE_SIZE // 3, y +
                                                       self.SQUARE_SIZE // 3), (x + self.SQUARE_SIZE // 3, y - self.SQUARE_SIZE // 3), 5)
        else:
            pygame.draw.circle(self.screen, self.BLACK,
                               (x, y), self.SQUARE_SIZE // 2 - 5)
        pygame.display.update()

    def draw_board(self):
        self.screen.fill(self.WHITE)
        for x in range(0, self.length, self.SQUARE_SIZE):
            pygame.draw.line(self.screen, self.GRAY, (x, 0), (x, self.length))
        for y in range(0, self.length, self.SQUARE_SIZE):
            pygame.draw.line(self.screen, self.GRAY, (0, y), (self.length, y))
        pygame.display.update()    

    def draw_message(self, message):
        text = self.font.render(message, True, self.RED)
        text_rect = text.get_rect(
            center=(self.length//2, self.length-self.SQUARE_SIZE//2))
        self.screen.blit(text, text_rect)

    def draw_button(self):
        button_width, button_height = 160, 80
        text_surface = self.font.render("Restart", True, self.BLACK)
        self.button_rect = pygame.Rect(
            (self.length - button_width) // 2, 0, button_width, button_height)
        pygame.draw.rect(self.screen, self.WHITE, self.button_rect)

        text_rect = text_surface.get_rect(center=self.button_rect.center)
        self.screen.blit(text_surface, text_rect)

    # def fill_screen(self):
    #     self.screen.fill(self.WHITE)
