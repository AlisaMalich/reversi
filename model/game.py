from board import Board
from player import Player

class Game:
    def __init__(self, board_size):
        self.board = Board.get_board(board_size)
        self.curr_player = Player.X

    def change_player(self):
        """This function changes a player
        """
        self.curr_player = 3 - self.curr_player

    def make_move(self, row, col):
        """Calls function to update the cell value

        Args:
            row (int)
            col (int)
        """
        self.board.update_cell(row, col, self.curr_player)

    def is_empty_cell(self, row, col):
        """Check whether the cell value equals 0 

        Args:
            row (int)
            col (int)

        Returns:
            Bool
        """
        return self.board.get_cell(row, col) == Board.EMPTY_CELL

    def is_opposite_cell(self, row, col):
        """Check whether the opposite disk on given cell

        Args:
            row (int)
            col (int)

        Returns:
            Bool
        """
        return self.board.get_cell(row, col) == self.curr_player

    # def checking_directions(self, row, col):
    #     target_cell = (row, col)
    #     directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    #     for direction in directions:
    #         curr_cell = target_cell
    #         curr_cell = (curr_cell[0] + direction[0], curr_cell[1] + direction[1])
            


    # def check_winner(self):
    #     pass
        