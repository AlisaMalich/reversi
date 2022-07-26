from view.board_view import BoardView
from model.board import Board

class BoardConsoleView(BoardView):
    symbols = {0: ' ', 1: 'X', 2: "O"}

    def __init__(self, board: Board):
        super().__init__(board)

    def draw_board(self):
        """_summary_
        """
        board_size = self.board.size
        header = '  |'
        divider = '--+'
        for i in range(1, board_size + 1):
            header += f' {i} |'
            divider += '---+'
        print(header)
        print(divider)

        for i in range(1, board_size + 1):
            str = f' {i}|'
            for j in range(1, board_size + 1):
                cell = self.board.get_cell(i, j)
                str += f' {self.symbols[cell]} |'
            print(str)
            print(divider)
                


