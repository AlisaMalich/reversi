from model.exceptions.user_input import UserInputError
from view.game_view import GameView
from view.board_console_view import BoardConsoleView
from model.game import Game
from model.player import Player

class GameConsoleView(GameView):

    def __init__(self, game: Game):
        super().__init__(GameView)
        self.board_view = BoardConsoleView(game.board)
        self.game = game
        self.error = UserInputError()
        self.player_x = Player.X
        self.player_o = Player.O


    def print_greeting(self):
        """Prints greeting and let User choose a game mode
        
        Returns:
            int: 1(for player-vs-player mode) or 2(for player-vs-computer mode)
        """
        print('Welcome to Reversi!\n' \
        'Choose a player mode:\n' \
        '1. Player vs Player\n' \
        '2. Player vs Computer\n')
        
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
        """Get cell coordinates from User and check if it's in valid format

        Args:
            prompt (str, optional). Defaults to 'Enter your move (row, col): '.

        Returns:
            int: row  - stands for [i] index of the board
            int: col  - stands for [j] index of the board
        """
        # check the input format
        while True:
            try:
                str = input(prompt)
                self.error.is_numeric(str)
            except UserInputError as e:
                print(e)
                continue
            else:
                break
        
        row = int(str.split(',')[0]) - 1
        col = int(str.split(',')[1]) - 1

        return row, col

    def draw_board(self):
        """Prints current board in console with current score of both players
        """

        self.board_view.draw_board()
        print(f"Player 1 score: {self.game.score.Player_X_score}, " \
        f"Player 2 score: {self.game.score.Player_O_score}")
        print(f"Player {self.game.curr_player}: It's your turn")

    def print_winner(self):
        """Prints result of the game
        """

        if self.game.score.Player_X_score > self.game.score.Player_O_score:
            return f'Player {self.player_x} won! The score is {self.game.score.Player_X_score}:{self.game.score.Player_O_score}'
        elif self.game.score.Player_O_score > self.game.score.Player_X_score:
            return f'Player {self.player_o} won! The score is {self.game.score.Player_O_score}:{self.game.score.Player_X_score}'
        else:
            return f"It's a draw! The score is {self.game.score.Player_X_score}:{self.game.score.Player_O_score}"

