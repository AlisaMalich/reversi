from model.game_player_vs_player import GamePlayerVsPlayer
from view.game_console_view import GameConsoleView
from controller.game_controller import GameController

model = GamePlayerVsPlayer(board_size=4)
view = GameConsoleView(model)
controller = GameController(view, model)

controller.run_game()