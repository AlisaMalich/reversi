from view.game_console_view import GameConsoleView
# from model.game_player_vs_player import GamePlayerVsPlayer
from model.game_player_vs_ai import GamePlayerVsAi

class GameController:
    
    mode = None

    def __init__(self, view:GameConsoleView, model: GamePlayerVsAi):
        self.view = view
        self.model = model

    # def __init__(self, view:GameConsoleView, model: GamePlayerVsPlayer):
    #     self.view = view
    #     self.model = model

    def run_game(self):
        mode = self.view.greeting_msg()

        if mode == '1':
            while True:
                if not self.model.is_game_over(self.model.curr_player):
                    self.view.draw_board()
                    while True:
                        try:
                            row, col = self.view.get_move()
                            assert self.model.is_empty_cell(row, col), 'This cell is not empty. Try again!'
                        except AssertionError as e:
                            print(e)
                            continue
                        else:
                            break

                    self.model.make_move(row, col) 
                    self.model.change_player()
                    continue

                elif not self.model.is_game_over(self.model.opponent):
                    self.model.change_player()
                    continue
                break

        elif mode == '2':
            while True:
                if not self.model.is_game_over(self.model.curr_player):
                    self.view.draw_board()
                    while True:
                        try:
                            row, col = self.view.get_move()
                            assert self.model.is_empty_cell(row, col), 'This cell is not empty. Try again!'
                        except AssertionError as e:
                            print(e)
                            continue
                        else:
                            break
                    self.model.make_move(row, col)
                    self.view.draw_board()

                    if not self.model.is_game_over(self.model.opponent):
                        self.model.make_move_ai(self.model.opponent) 
                    continue
                
                if not self.model.is_game_over(self.model.opponent):
                    self.model.make_move_ai(self.model.opponent) 
                    continue
                break

        self.view.draw_board()
        print(self.model.get_results())
        self.model.store_results()

            
        




                        

                
                

