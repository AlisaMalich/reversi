from view.game_console_view import GameConsoleView
from model.game import Game

class GameController:
    mode = None

    def __init__(self, view:GameConsoleView, model: Game):
        self.view = view
        self.model = model

    def run_game(self):
        mode = self.view.print_greeting()

        if mode == '1':
            while True:
                # while current player has any valid move - continue the game
                if self.model.has_valid_moves(self.model.curr_player):
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

                # elif only opponent player has any valid move
                # -> opponent player becomes current player
                # -> returns to the beginning of the while-loop
                elif self.model.has_valid_moves(self.model.opponent):
                    self.model.change_player()
                    continue
                # if neither current player nor opponent player has any valid move
                # -> the while-loop is broken (game is over)
                break

        elif mode == '2':
            while True:
                # at each itteration of while-loop, 
                # if each of them has any valid move, 
                # the current player makes a move & the opponent player makes a move
                if self.model.has_valid_moves(self.model.curr_player):
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

                    if self.model.has_valid_moves(self.model.opponent):
                        self.model.make_move_ai(self.model.opponent) 
                    continue
                
                # if only opponent player has valid move
                # -> opponent player makes a move
                # -> returns to the beginning of the while-loop
                if self.model.has_valid_moves(self.model.opponent):
                    self.model.make_move_ai(self.model.opponent) 
                    continue

                # if neither current player nor opponent player has any valid move
                # -> the while-loop is broken (game is over)
                break

        self.view.draw_board()
        result = self.view.print_winner()
        print(self.view.print_winner())
        self.model.store_results(result)

            
        




                        

                
                

