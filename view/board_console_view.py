from board_view import BoardView
from model.board import Board

class BoardConsoleView(BoardView):
    symbols = {0: ' ', 1: 'X', 2: "O"}

    def __init__(self, board: Board) -> None:
        super().__init__(board)

    # def draw_board(self):
    #     board_size = self.board.size
    #     header = 