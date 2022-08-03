# from model.game import Game
from model.game_against_human import GameAgainstHuman
from view.game_console_view import GameConsoleView
from controller.game_controller import GameController

model = GameAgainstHuman(board_size=8)
view = GameConsoleView(model)
controller = GameController(view, model)

controller.run_game()