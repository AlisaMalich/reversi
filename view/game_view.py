from abc import ABC, abstractmethod
from model.game import Game

class GameView(ABC):
    def __init__(self, game:Game):
        self.game = Game

    @abstractmethod
    def print_greeting(self):
        pass

    @abstractmethod
    def get_move(self):
        pass

    @abstractmethod
    def draw_board(self):
        pass

    @abstractmethod
    def print_winner(self):
        pass

    
