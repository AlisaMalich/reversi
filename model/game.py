from board import Board
from players import Player

class Game:
    def __init__(self, board_size):
        self.board = Board(board_size)
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

    def is_valid_move(self, row, col):
        """Check whether the cell value equals 0 

        Args:
            row (int)
            col (int)

        Returns:
            Bool
        """
        return self.board.get_cell(row, col) == Board.EMPTY_CELL

    # def check_winner(self):
    #     pass
        