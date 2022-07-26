from model.board import Board
from model.player import Player

class Game:
    DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

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
        print('make_move_func')
        steps = self.is_valid_move(row, col)
        if len(steps) == 0:
            return False
        else:
            for step in steps:
                self.board.update_cell(step[0], step[1], self.curr_player)


    def is_empty_cell(self, row, col):
        """Check whether the cell value equals 0 

        Args:
            row (int)
            col (int)

        Returns:
            Bool
        """
        return self.board.get_cell(row, col) == Board.EMPTY_CELL

    def is_on_board(self, row, col):
        return row <= self.board.size and col <= self.board.size 

    def is_opposite_cell(self, row, col):
        """Check whether the opposite disk on given cell

        Args:
            row (int)
            col (int)

        Returns:
            Bool
        """
        return self.board.get_cell(row, col) == self.curr_player

    def is_valid_move(self, row, col):
        # save the cell program started from
        target_cell = (row, col)

        for direction in self.DIRECTIONS:
            curr_cell = target_cell
            # make the first step in the direction
            curr_cell = (curr_cell[0] + direction[0], curr_cell[1] + direction[1])
            # continue making steps while the cell is on board and occupied by opponents disk
            while self.is_on_board(curr_cell[0], curr_cell[1]) and self.is_opposite_cell(curr_cell[0], curr_cell[1]):
                curr_cell = (curr_cell[0] + direction[0], curr_cell[1] + direction[1])
            # after while loop check why it was interupted
            # if there are no more steps on board -> returns to for loop and checking next direction
            if not self.is_on_board(curr_cell[0], curr_cell[1]):
                continue
            # if current cell disk equals to current player disk 
            if not self.is_opposite_cell(curr_cell[0], curr_cell[1]):
                # create a list to store all steps
                steps = []
                while curr_cell[0] == target_cell[0] and curr_cell[1] == target_cell[1]:
                    curr_cell[0] -= direction[0]
                    curr_cell[1] -= direction[1]
                    steps.append((curr_cell[0], curr_cell[1]))
            return steps



    # def checking_directions(self, row, col):
    #     target_cell = (row, col)
    #     directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    #     for direction in directions:
    #         curr_cell = target_cell
    #         curr_cell = (curr_cell[0] + direction[0], curr_cell[1] + direction[1])
            


    # def check_winner(self):
    #     pass
        