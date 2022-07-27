from model.player import Player

class Score:

    def __init__(self):
        self.score = {Player.X: 2, Player.O: 2}

    def increase_score(self, player):
        print('player',player)
        score = self.score[player]
        score += 1

    def decrease_score(self, player):
        score = self.score[player]
        score -= 1

    def __str__(self) -> str:
        print('Player.X: ', self.score[Player.X], 'Player.Y: ', self.score[Player.Y])