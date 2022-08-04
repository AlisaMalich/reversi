from model.game import Game
from model.board import Board
from model.player import Player
# from model.score import Score

class GamePlayerVsPlayer(Game):
    DIRECTIONS = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]
    # DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

    def __init__(self, board_size):
        super().__init__(board_size)
        self.curr_player = Player.X
        self.opponent = Player.O
        self.board = Board(board_size)

    def change_player(self):
        """This function changes a current player
        """
        self.curr_player, self.opponent = self.opponent, self.curr_player

    def make_move(self, row, col):
        """Calls function to update the cell value
        """
        cells_to_update = self.is_valid_move(row, col)
        if cells_to_update:
            for cell in cells_to_update:
                self.board.update_cell(cell[0], cell[1], self.curr_player)
        else: 
            # TODO error handling
            print('The move is not valid')
            

    def is_empty_cell(self, row, col):
        """Check whether the cell value equals 0 
        """
        return self.board.get_cell(row, col) == Board.EMPTY_CELL

    def is_on_board(self, row, col):
        return row <= self.board.size and col <= self.board.size and row >= 0 and col >= 0

    def is_opponent_cell(self, row, col):
        """Check whether the opposite disk on given cell
        """
        return self.board.get_cell(row, col) == self.opponent

    def is_valid_move(self, row, col):
        # target_cell = (row, col)
        target_cell = [row, col]
        is_valid = False

        for direction in self.DIRECTIONS:
            curr_cell = target_cell
            # curr_cell = (curr_cell[0] + direction[0], curr_cell[1] + direction[1])
            curr_cell = [curr_cell[0] + direction[0], curr_cell[1] + direction[1]]

            if self.is_opponent_cell(curr_cell[0], curr_cell[1]):
                while self.is_opponent_cell(curr_cell[0], curr_cell[1]):
                    curr_cell = (curr_cell[0] + direction[0], curr_cell[1] + direction[1])

                if not self.is_on_board(curr_cell[0], curr_cell[1]):
                    break

                if not self.is_opponent_cell(curr_cell[0], curr_cell[1]):
                    is_valid = True
                break

        if is_valid:
            return self.get_list_of_moves(target_cell, curr_cell, direction)
        else:
            return None

    def get_list_of_moves(self, target_cell, curr_cell, direction):
        """Get list of cells to update
        """
        cells_to_update = []
        curr_cell = list(curr_cell)
        while target_cell != curr_cell:
            curr_cell[0] = curr_cell[0] - direction[0]
            curr_cell[1] = curr_cell[1] - direction[1]
            cells_to_update.append([curr_cell[0], curr_cell[1]])
        return cells_to_update

    def check_winner(self):
        """Check whether the game is over
        """
        
