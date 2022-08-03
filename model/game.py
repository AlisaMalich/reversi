from abc import ABC, abstractmethod

class Game(ABC):
    """Abstract class for general rules
    """

    def __init__(self, board_size):
        self.board_size = board_size

    @abstractmethod
    def change_player(self):
        """This function changes a player
        """
        pass

    @abstractmethod
    def make_move(self, row, col):
        """Calls function to update the cell value
        """
        pass

    # @abstractmethod
    # def check_winner(self):
    #     """Check whether the game is over
    #     """
    #     pass
