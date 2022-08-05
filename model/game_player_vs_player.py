from model.game import Game
from model.board import Board
from model.player import Player
from model.score import Score

class GamePlayerVsPlayer(Game):
    DIRECTIONS = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]
    # DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

    def __init__(self, board_size):
        super().__init__(board_size)
        self.curr_player = Player.X
        self.opponent = Player.O
        self.board = Board(board_size)
        self.score = Score()

    def change_player(self):
        """This function changes a current player
        """
        self.curr_player, self.opponent = self.opponent, self.curr_player
        # self.curr_player = 3 - self.curr_player
        # if self.curr_player == Player.X:
        #     self.curr_player = Player.O
        # elif self.curr_player == Player.O:
        #     self.curr_player = Player.X

    def make_move(self, row, col):
        """Calls function to update the cell value
        """
        # print('make_move', row, col)
        cells_to_update = self.is_valid_move(row, col)
        if cells_to_update:
            for cell in cells_to_update:
                self.board.update_cell(cell[0], cell[1], self.curr_player)
            self.score.update_score(len(cells_to_update), self.curr_player)
        else: 
            # TODO error handling
            print('The move is not valid')
        
        # print('X: ', self.score.Player_X_score)
        # print('O: ', self.score.Player_O_score)

    
    def is_empty_cell(self, row, col):
        """Check whether the cell value equals 0 
        """
        return self.board.get_cell(row, col) == Board.EMPTY_CELL

    def is_on_board(self, row, col):
        # print("is on board",row, col)
        # print('board_size', self.board.size)
        return row < self.board.size and col < self.board.size and row >= 0 and col >= 0

    def is_opponent_cell(self, row, col):
        """Check whether the opposite disk on given cell
        """
        # print('from is_opponent', row, col)
        # print('from is_opponent -> get cell', self.board.get_cell(row, col))
        # print('from is_opponent -> opponent', self.opponent)
        return self.board.get_cell(row, col) == self.opponent

    def is_valid_move(self, row, col):
        # target_cell = (row, col)
        target_cell = [row, col]
        is_valid = False

        for direction in self.DIRECTIONS:
            curr_cell = target_cell
            curr_cell = [curr_cell[0] + direction[0], curr_cell[1] + direction[1]]
            # print('direction', direction)
            # print('curr_cell', curr_cell)
            if self.is_on_board(curr_cell[0], curr_cell[1]):
                # print('is_on_board', self.is_on_board(curr_cell[0], curr_cell[1]))
                if self.is_opponent_cell(curr_cell[0], curr_cell[1]):
                    # print('is_opponent_cell', self.is_opponent_cell(curr_cell[0], curr_cell[1]))
                    while self.is_on_board(curr_cell[0], curr_cell[1]) and self.is_opponent_cell(curr_cell[0], curr_cell[1]):
                        curr_cell = (curr_cell[0] + direction[0], curr_cell[1] + direction[1])
                        # print('curr_cell', curr_cell)

                    if not self.is_on_board(curr_cell[0], curr_cell[1]):
                        continue
                    
                    if self.is_empty_cell(curr_cell[0], curr_cell[1]):
                        continue

                    # if not self.is_opponent_cell(curr_cell[0], curr_cell[1]):
                    if self.board.get_cell(curr_cell[0], curr_cell[1]) == self.curr_player:
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

    def is_game_over(self):
        """Check whether the game is over
        """
        for i in range(self.board.size):
            for j in range(self.board.size):
                if self.is_empty_cell(i, j) and self.is_valid_move(i, j):
                    print(self.curr_player)
                    print(self.is_valid_move(i, j))
                    return False
        return True

    def get_results(self):
        if self.score.Player_X_score > self.score.Player_O_score:
            return f'{Player.X} won! The score is {self.score.Player_X_score}:{self.score.Player_O_score}'
        elif self.score.Player_O_score > self.score.Player_X_score:
            return f'{Player.O} won! The score is {self.score.Player_O_score}:{self.score.Player_X_score}'
        else:
            return f"It's a draw! The score is {self.score.Player_X_score}:{self.score.Player_O_score}"

        



        
        
