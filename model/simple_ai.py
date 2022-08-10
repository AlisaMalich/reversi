from model.game import Game
from model.player import Player

class SimpleAi():
    def __init__(self, game:Game) -> None:
        self.game = game

    def get_all_valid_moves(self, player=Player.O):
        all_valid_moves = []
        # stores all possible moves in a list
        for i in range(self.game.board.size):
            for j in range(self.game.board.size):
                if self.game.is_empty_cell(i, j) and self.game.is_valid_move(i, j, player):
                    all_valid_moves.append(self.game.is_valid_move(i, j, player))

        return all_valid_moves

    def find_best_move(self, player=Player.O):
        best_move = max(self.get_all_valid_moves(player), key=lambda x: len(x))
        return best_move
    
    def make_move(self, player=Player.O):
        best_move = self.find_best_move(player=Player.O)
        for cell in best_move:
            self.game.board.update_cell(cell[0], cell[1], player)
        self.game.score.update_score(len(best_move), player)

