from model.player import Player

class Score():
    def __init__(self) -> None:
        self.Player_X_score = 2
        self.Player_O_score = 2

    def update_score(self, num_of_moves, curr_player):
        if curr_player == Player.X:
            self.Player_X_score += num_of_moves
            self.Player_O_score -= (num_of_moves - 1)
        else:
            self.Player_X_score -= (num_of_moves - 1)
            self.Player_O_score += num_of_moves




