class Board:
    def __init__(self, size):
        self.size = size
        #Create a 2D array size*size, init value of element is None
        self.grid = [[None for _ in range(size)] for _ in range(size)]

    def get_cell(self, row, col):
        return self.grid[row][col]

    def set_cell(self, row, col, value):
        self.grid[row][col] = value

    def is_empty_cell(self, row, col):
        return self.grid[row][col] == None

    def is_full(self):
        for row in range(self.size):
            for col in range(self.size):
                if self.grid[row][col] == None:
                    return False
        return True

    def get_empty_cells(self):
        cells = []
        for row in range(self.size):
            for col in range(self.size):
                if self.is_empty_cell(row, col):
                    cells.append((row, col))
        return cells