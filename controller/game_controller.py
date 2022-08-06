from view.game_console_view import GameConsoleView
from model.game_player_vs_player import GamePlayerVsPlayer

class GameController:

    def __init__(self, view:GameConsoleView, model: GamePlayerVsPlayer):
        self.view = view
        self.model = model

    def run_game(self):
        self.view.draw_board()
        while True:
            # print(not self.model.is_game_over(self.model.curr_player))
            print('opponent', not self.model.is_game_over(self.model.opponent))

            if not self.model.is_game_over(self.model.curr_player):
                self.view.draw_board()
                row, col = self.view.get_move()
                while not self.model.is_empty_cell(row, col):
                    print('Invalid move, try again')
                    row, col = self.view.get_move()
                self.model.make_move(row, col)            
                self.model.change_player()
                continue
            elif not self.model.is_game_over(self.model.opponent):
                self.model.change_player()
                continue

            break


        self.view.draw_board()
        print(self.model.get_results())
        self.model.store_results()


    # def run_game(self):
    #     self.view.draw_board()
    #     while not self.model.is_game_over():
    #         self.view.draw_board()
    #         row, col = self.view.get_move()
    #         while not self.model.is_empty_cell(row, col):
    #             print('Invalid move, try again')
    #             row, col = self.view.get_move()
    #         self.model.make_move(row, col)            
    #         self.model.change_player()
        

    #     self.view.draw_board()
    #     print(self.model.get_results())
            
        




                        

                
                

