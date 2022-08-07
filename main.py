# from model.game_player_vs_player import GamePlayerVsPlayer
from model.game_player_vs_ai import GamePlayerVsAi
from view.game_console_view import GameConsoleView
from controller.game_controller import GameController

# model1 = GamePlayerVsPlayer(board_size=8)
model = GamePlayerVsAi(board_size=4)
view = GameConsoleView(model)
controller = GameController(view, model)

controller.run_game()