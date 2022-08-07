from model.exceptions.user_input import UserInputError
from view.game_view import GameView
from view.board_console_view import BoardConsoleView
from model.game_player_vs_player import GamePlayerVsPlayer

class GameConsoleView(GameView):

    def __init__(self, game: GamePlayerVsPlayer):
        # super().__init__(game)
        super().__init__(GameView)
        self.board_view = BoardConsoleView(game.board)
        self.game = game
        self.error = UserInputError()

    def greeting_msg(self):
        print('\n \
        Welcome to Reversi!\n \
        Choose a player mode:\n \
        1. Player vs Player\n \
        2. Player vs Computer\n')
        
        while True:
            try:
                mode = input('Enter mode: ')
                self.error.check_mode(mode)
            except UserInputError as e:
                print(e)
                continue
            else:
                break
        return mode

    def get_move(self, prompt='Enter your move (row, col): '):

        while True:
            try:
                str = input(prompt)
                self.error.is_numeric(str)
            except UserInputError as e:
                print(e)
                continue
            else:
                break
        
        # print(str)
        row = int(str.split(',')[0]) - 1
        col = int(str.split(',')[1]) - 1
        return row, col

    def draw_board(self):
        self.board_view.draw_board()
        print(f"Player 1 score: {self.game.score.Player_X_score}, Player 2 score: {self.game.score.Player_O_score}")
        print(f"Player {self.game.curr_player}: It's your turn")
