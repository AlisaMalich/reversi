from view.game_console_view import GameConsoleView
from model.game import Game

class GameController:
    DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

    def __init__(self, view:GameConsoleView, model: Game):
        self.view = view
        self.model = model

    def run_game(self):
        while True:
            self.view.draw_board()

            row, col = self.view.get_move()
            while not self.model.is_empty_cell(row, col):
                #TODO display error message
                row, col = self.view.get_move()

            target_cell = (row, col)
            score = []
            for direction in self.DIRECTIONS:
                curr_cell = target_cell
                curr_cell = (curr_cell[0] + direction[0], curr_cell[1] + direction[1])
                if self.model.is_opposite_cell(curr_cell[0], curr_cell[1])

