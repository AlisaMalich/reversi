from model.board import Board
from model.player import Player
from model.score import Score

class Game:
    DIRECTIONS = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]
    # DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

    def __init__(self, board_size):
        self.board = Board(board_size)
        self.curr_player = Player.X
        self.score = Score

    def change_player(self):
        """This function changes a player
        """
        self.curr_player = 3 - self.curr_player

    def make_move(self, row, col):
        """Calls function to update the cell value

        Args:
            row (int)
            col (int)
        """
        steps = self.is_valid_move(row, col)
        if len(steps) == 0:
            return False
        else:
            for step in steps:
                print(self.curr_player)
                self.board.update_cell(step[0], step[1], self.curr_player)
                self.score.increase_score(self.curr_player)
                self.score.decrease_score(3 - self.curr_player)
                print(self.score)


    def is_empty_cell(self, row, col):
        """Check whether the cell value equals 0 

        Args:
            row (int)
            col (int)

        Returns:
            Bool
        """
        return self.board.get_cell(row, col) == Board.EMPTY_CELL

    def is_on_board(self, row, col):
        return row <= self.board.size and col <= self.board.size 

    def is_opponent_cell(self, row, col):
        """Check whether the opposite disk on given cell

        Args:
            row (int)
            col (int)

        Returns:
            Bool
        """
        return self.board.get_cell(row, col) != self.curr_player

    def is_valid_move(self, row, col):
        # save the cell program started from
        target_cell = [row, col]
        print('target_cell',target_cell)
        print('curr player', self.curr_player)

        for direction in self.DIRECTIONS:
            steps = []
            print('dir: ', direction)
            curr_cell = list(target_cell)
            # make the first step in the direction
            curr_cell = (curr_cell[0] + direction[0], curr_cell[1] + direction[1])
            # continue making steps while the cell is on board and occupied by opponents disk
            if self.is_on_board(curr_cell[0], curr_cell[1]) and self.is_opponent_cell(curr_cell[0], curr_cell[1]) and not self.is_empty_cell(curr_cell[0], curr_cell[1]):
                while (self.is_on_board(curr_cell[0], curr_cell[1]) and self.is_opponent_cell(curr_cell[0], curr_cell[1])) and not self.is_empty_cell(curr_cell[0], curr_cell[1]):
                    curr_cell = (curr_cell[0] + direction[0], curr_cell[1] + direction[1])
                    print('new curr cell:', curr_cell)
                    print('is on board:', self.is_on_board(curr_cell[0], curr_cell[1]))
                    print('is opponent cell:', not self.is_opponent_cell(curr_cell[0], curr_cell[1]))

                # after while loop check why it was interupted
                # if there are no more steps on board -> returns to for loop and checking next direction
                
                if not self.is_on_board(curr_cell[0], curr_cell[1]):
                    continue
            
                # if current cell disk equals to current player disk 
                if not self.is_opponent_cell(curr_cell[0], curr_cell[1]):
                    # create a list to store all steps
                    # print('sec_loop!')
                    curr_cell = list(curr_cell)
                    while (curr_cell[0] != target_cell[0] or curr_cell[1] != target_cell[1]):
                    # while curr_cell[1] != target_cell[1]:
                        curr_cell[0] = curr_cell[0] - direction[0]
                        curr_cell[1] = curr_cell[1] - direction[1]
                        steps.append((curr_cell[0], curr_cell[1]))
                    print(steps)
                return steps
        
    # def is_valid_move(self, row, col):
    #     steps = []
    #     for direction in self.DIRECTIONS:
    #         target_cell = [row, col]
    #         curr_cell = list(target_cell)
    #         curr_cell = (curr_cell[0] + direction[0], curr_cell[1] + direction[1]) 
    #         if self.is_on_board(curr_cell[0], curr_cell[1]) and self.is_opponent_cell(curr_cell[0], curr_cell[1]) and not self.is_empty_cell(curr_cell[0], curr_cell[1]):
    #            curr_cell = (curr_cell[0] + direction[0], curr_cell[1] + direction[1]) 
    #            if not self.is_on_board(curr_cell[0], curr_cell[1]):
    #             continue
    #            while self.is_opponent_cell(curr_cell[0], curr_cell[1]):
    #                curr_cell = (curr_cell[0] + direction[0], curr_cell[1] + direction[1]) 
    #                if not self.is_on_board(curr_cell[0], curr_cell[1]):
    #                 break
    #            if not self.is_on_board(curr_cell[0], curr_cell[1]):
    #                 continue
    #            if not self.is_opponent_cell(curr_cell[0], curr_cell[1]):
    #                 curr_cell = list(curr_cell)
    #                 while (curr_cell[0] != target_cell[0] or curr_cell[1] != target_cell[1]):
    #                     curr_cell[0] = curr_cell[0] - direction[0]
    #                     curr_cell[1] = curr_cell[1] - direction[1]
    #                     steps.append((curr_cell[0], curr_cell[1]))
    #     return steps





    