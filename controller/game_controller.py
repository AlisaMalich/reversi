from view.game_console_view import GameConsoleView
from model.game import Game

class GameController:

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
            
            self.model.make_move(row, col)

            # player = self.model.check_winner()
            # if player:
            #     self.view.display_winner(player)
            #     break
            
            self.model.change_player()


            # # save the cell program started from
            # target_cell = (row, col)
            # # 
            # score = []
            # for direction in self.DIRECTIONS:
            #     curr_cell = target_cell
            #     # make the first step in the direction
            #     curr_cell = (curr_cell[0] + direction[0], curr_cell[1] + direction[1])
            #     # continue making steps while the cell is on board and occupied by opponents disk
            #     while self.model.is_on_board(curr_cell[0], curr_cell[1]) and self.model.is_opposite_cell(curr_cell[0], curr_cell[1]):
            #         curr_cell = (curr_cell[0] + direction[0], curr_cell[1] + direction[1])
            #     # after while loop check why it was interupted
            #     # if there are no more steps on board -> returns to for loop and checking next direction
            #     if not self.model.is_on_board(curr_cell[0], curr_cell[1]):
            #         continue
            #     # if current cell disk equals to current player disk 
            #     if not self.model.is_opposite_cell(curr_cell[0], curr_cell[1]):

                        

                
                

