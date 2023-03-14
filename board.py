class Board:
    def __init__(self, size):
        self.size = size
        #Create a 2D array size*size, init value of element is None
        self.grid = [[None for _ in range(size)] for _ in range(size)]

    def get_cell(self, row, col):
        return self.grid[row][col]

    def set_cell(self, row, col, value):
        self.grid[row][col] = value
    
    # get all lines 5 cells and 6 cells
    def get_all_lines(self):
        grid = self.grid
        n = len(grid)
        lines = []
        # horizontal lines
        for i in range(n):
            for j in range(n-4):
                lines.append(grid[i][j:j+5])
            for j in range(n-5):
                lines.append(grid[i][j:j+6])

        # vertical lines
        for i in range(n):
            for j in range(n-4):
                lines.append([grid[k][i] for k in range(j, j+5)])
            for j in range(n-5):
                lines.append([grid[k][i] for k in range(j, j+6)])
        # diagonal lines
        for i in range(n-4):
            for j in range(n-4):
                lines.append([grid[i+k][j+k] for k in range(5)])
                lines.append([grid[i+k][j+4-k] for k in range(5)])
        for i in range(n-5):
            for j in range(n-5):
                lines.append([grid[i+k][j+k] for k in range(6)])
                lines.append([grid[i+k][j+5-k] for k in range(6)])
        return lines

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