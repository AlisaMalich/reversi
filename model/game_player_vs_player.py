from model.game import Game
from model.board import Board
from model.player import Player
# from model.score import Score

class GamePlayerVsPlayer(Game):
    # DIRECTIONS = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]
    DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

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
        valid_move = self.is_valid_move(row, col)
        if valid_move:
            print('cell', valid_move[0])
            print('dir', valid_move[1])
        else: 
            # TODO error handling
            print('The move is not valid')
            

        if steps:
            for step in steps:
                self.board.update_cell(step[0], step[1], self.curr_player)
            # нужен else?
            else:
                return False

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
        target_cell = (row, col)
        valid_move = []

        for direction in self.DIRECTIONS:
            curr_cell = target_cell
            curr_cell = (curr_cell[0] + direction[0], curr_cell[1] + direction[1])

            if self.is_opponent_cell(curr_cell[0], curr_cell[1]):
                while self.is_opponent_cell(curr_cell[0], curr_cell[1]):
                    curr_cell = (curr_cell[0] + direction[0], curr_cell[1] + direction[1])

                if not self.is_on_board(curr_cell[0], curr_cell[1]):
                    break

                if not self.is_opponent_cell(curr_cell[0], curr_cell[1]):
                    valid_move.append(curr_cell)
                    valid_move.append(direction)
                break
            else:
                valid_move = []

        if len(valid_move) > 0:
            return valid_move
        else:
            return None

    def check_winner(self):
        """Check whether the game is over
        """
        
