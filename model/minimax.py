from copy import deepcopy
import math
from model.game import Game
from model.player import Player

class Minimax():
    def __init__(self, game:Game, max_depth=3):
        self.max_depth = max_depth
        self.game = deepcopy(game)
        self.curr_player = Player.O
        self.opponent = Player.X

    def choose_move(self):
        max_value = -math.inf
        best_move = None

        moves = self.get_all_valid_moves()
        for move in moves:
            new_board = deepcopy(self.game.board)
            self.make_move(move, new_board)
            board_value = self.minimax(0, new_board, self.curr_player, self.opponent)

            if board_value > max_value:
                best_move = move
        
        return best_move

    def get_all_valid_moves(self, player=Player.O):
        all_valid_moves = []
        # stores all possible moves in a list
        for i in range(self.game.board.size):
            for j in range(self.game.board.size):
                if self.game.is_empty_cell(i, j) and self.game.is_valid_move(i, j, player):
                    all_valid_moves.append(self.game.is_valid_move(i, j, player))

        return all_valid_moves

    def make_move(self, cells_to_update, board, player=Player.O):
        for cell in cells_to_update:
            board.update_cell(cell[0], cell[1], player)

    def is_terminal_state(self, board):
        for i in range(self.game.board_size):
            for j in range(self.game.board_size):
                if board.is_empty_cell(i, j):
                    if self.game.is_valid_move(i, j, Player.X) or self.game.is_valid_move(i, j, Player.O):
                        return False
        return True

    def get_score(self, board):
        player_x_score = 0
        player_o_score = 0

        for i in range(self.game.board_size):
            for j in range(self.game.board_size):
                cell = board.get_move(i, j)

                if cell == self.curr_player:
                    player_o_score += 1
                elif cell == self.opponent:
                    player_x_score += 1

        return player_o_score, player_x_score

    def minimax(self, depth, board, max_player, min_player):
        if depth == self.max_depth or self.is_terminal_state(board):
            (player_score, opponent_score) = self.get_score(board)
            if player_score > opponent_score:
                return 1
            elif player_score < opponent_score:
                return -1
            else: 
                return

        values = []

        moves = self.get_all_valid_moves(max_player)
        for move in moves:
            new_board = deepcopy(self.game.board)
            self.make_move(move, new_board)
            board_value = self.minimax(depth + 1, new_board, min_player, max_player)
            values.append(board_value)

        if self == max_player:
            return max(values)
        else:
            return min(values)

