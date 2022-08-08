from abc import ABC, abstractmethod

class AbsGame(ABC):
    """Abstract class for general rules
    """

    def __init__(self, board_size):
        self.board_size = board_size

    @abstractmethod
    def change_player(self):
        pass

    @abstractmethod
    def make_move(self, row, col):
        pass

