from datetime import datetime
from model.abs_game import AbsGame
from model.board import Board
from model.player import Player
from model.score import Score

class Game(AbsGame):
    """Class for all the game logic
    """

    DIRECTIONS = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]

    def __init__(self, board_size):
        super().__init__(board_size)
        self.curr_player = Player.X
        self.opponent = Player.O
        self.board = Board(board_size)
        self.score = Score()

    def change_player(self):
        self.curr_player, self.opponent = self.opponent, self.curr_player
        
    def make_move(self, row, col):
        """If the move is valid: gets list of cells to update, 
        calls functions to update the board and scores of players.
        If the move is valid: returns None
        """
        cells_to_update = self.is_valid_move(row, col, self.curr_player)
        if cells_to_update:
            for cell in cells_to_update:
                self.board.update_cell(cell[0], cell[1], self.curr_player)
            self.score.update_score(len(cells_to_update), self.curr_player)
        else: 
            return None
    
    def is_empty_cell(self, row, col):
        """Checks whether the cell value equals 0 
        """
        return self.board.get_cell(row, col) == Board.EMPTY_CELL

    def is_on_board(self, row, col):
        """Checks whether the cells indexes is in the board range
        """
        return row < self.board.size and col < self.board.size and row >= 0 and col >= 0

    def is_opponent_cell(self, row, col, player):
        """Check whether the cell is occupied by the opponent disk
        """
        if player == self.curr_player:
            return self.board.get_cell(row, col) == self.opponent
        else:
            return self.board.get_cell(row, col) == self.curr_player


    def is_valid_move(self, row, col, player):
        """Checks whether the move is valid

        Returns:
            If is valid: returns a list of cells
            If isn't valid: returns None
        """
        # save the value of target cell
        target_cell = [row, col]
        is_valid = False

        for direction in self.DIRECTIONS:
            curr_cell = target_cell
            curr_cell = [curr_cell[0] + direction[0], curr_cell[1] + direction[1]]
            if self.is_on_board(curr_cell[0], curr_cell[1]):
                if self.is_opponent_cell(curr_cell[0], curr_cell[1], player):
                    while self.is_on_board(curr_cell[0], curr_cell[1]) and self.is_opponent_cell(curr_cell[0], curr_cell[1], player):
                        curr_cell = (curr_cell[0] + direction[0], curr_cell[1] + direction[1])

                    if not self.is_on_board(curr_cell[0], curr_cell[1]):
                        continue
                    
                    if self.is_empty_cell(curr_cell[0], curr_cell[1]):
                        continue

                    # the move is valid only if loop stops because the cell is occupied 
                    # by the current player disk
                    if self.board.get_cell(curr_cell[0], curr_cell[1]) == player:
                        is_valid = True
                    break

        if is_valid:
            return self.get_list_of_moves(target_cell, curr_cell, direction)
        else:
            return None

    def get_list_of_moves(self, target_cell, curr_cell, direction):
        """Returns list of cells to update

        Returns:
            list: list of cells to update
        """
        cells_to_update = []
        curr_cell = list(curr_cell)
        while target_cell != curr_cell:
            curr_cell[0] = curr_cell[0] - direction[0]
            curr_cell[1] = curr_cell[1] - direction[1]
            cells_to_update.append([curr_cell[0], curr_cell[1]])
        return cells_to_update

    def has_valid_moves(self, player):
        """Check whether the player has at least one valid move or not
        """
        for i in range(self.board.size):
            for j in range(self.board.size):
                if self.is_empty_cell(i, j) and self.is_valid_move(i, j, player):
                    return True
        return False

    def store_results(self, str, file_path='reversi_results.txt'):
        """Stores results in txt.file

        Args:
            str (string): The result itself
            file_path (str, optional). Defaults to 'reversi_results.txt'.
        """
        date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        with open(file_path, 'a') as f:
            f.write(f'{date} - {str}\n')

    # def make_move_ai(self, player=Player.O):
    #     """Makes the most efficient move 
    #     """
        # all_valid_moves = []
        # # stores all possible moves in a list
        # for i in range(self.board.size):
        #     for j in range(self.board.size):
        #         if self.is_empty_cell(i, j) and self.is_valid_move(i, j, player):
        #             all_valid_moves.append(self.is_valid_move(i, j, player))
        # define the best move as move with the maximum length: the move with
        # the largest number of cells to update
        # best_move = max(all_valid_moves, key=lambda x: len(x))
        # updates the cells and scores of both players
    #     best_move = self.game_simple_ai.find_best_move()
    #     for cell in best_move:
    #         self.board.update_cell(cell[0], cell[1], player)
    #     self.score.update_score(len(best_move), player)
    # # def make_move_ai(self, player=Player.O):
    #     """Makes the most efficient move 
    #     """
    #     all_valid_moves = []
    #     # stores all possible moves in a list
    #     for i in range(self.board.size):
    #         for j in range(self.board.size):
    #             if self.is_empty_cell(i, j) and self.is_valid_move(i, j, player):
    #                 all_valid_moves.append(self.is_valid_move(i, j, player))
    #     # define the best move as move with the maximum length: the move with
    #     # the largest number of cells to update
    #     best_move = max(all_valid_moves, key=lambda x: len(x))
    #     # updates the cells and scores of both players
    #     for cell in best_move:
    #         self.board.update_cell(cell[0], cell[1], player)
    #     self.score.update_score(len(best_move), player)

    # def choose_move(self, player=Player.O):
    #     all_valid_moves = []
    #     for i in range(self.board.size):
    #         for j in range(self.board.size):
    #             if self.is_empty_cell(i, j) and self.is_valid_move(i, j, player):
    #                 all_valid_moves.append(self.is_valid_move(i, j, player))

    #     for move in all_valid_moves:
    #         new_score = self.score.get_score(len(move), player)
    #         value = minimax(self, new_score)
        
    #     # ???
    #     return move

    # def minimax(self, score, player_ai=Player.O, player_human=Player.X):

    #     if self.board


