from model.player import Player

class Board:
    EMPTY_CELL = 0

    def __init__(self, size):
        self.size = size
        # Allocate the board with empty squares
        # self.mat = [[self.EMPTY_CELL] * size for _ in range(size)]
        self.mat = [[self.EMPTY_CELL] * size for _ in range(size)]
        half = int(size / 2)
        self.mat[half-1][half-1] = Player.X
        self.mat[half-1][half] = Player.O
        self.mat[half][half-1] = Player.O
        self.mat[half][half] = Player.X


    def get_cell(self, row, col):
        """Returns a value of specific cell of matrix

        Args:
            row (int)
            col (int)

        Returns:
            int: 0 or 1 or 2
        """
        return self.mat[row][col]

    def update_cell(self, row, col, player):
        self.mat[row][col] = player

