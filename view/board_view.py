from abc import ABC, abstractmethod
from model.board import Board

class BoardView(ABC):
    def __init__(self, board:Board):
        super().__init__()
        self.board = board

    @abstractmethod
    def draw_board(self):
        pass