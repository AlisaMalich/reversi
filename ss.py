    def is_valid_move(self, row, col):
        # save the cell program started from
        target_cell = [row, col]
        # print('target cell = ', target_cell)
        for direction in self.DIRECTIONS:
            steps = []
            curr_cell = list(target_cell)
            print("curr_cell: ", curr_cell)
            print(direction)
            # print("curr_cell: ", self.board.get_cell(curr_cell[0], curr_cell[1]))
            # make the first step in the direction
            curr_cell = (curr_cell[0] + direction[0], curr_cell[1] + direction[1])
            # print("curr_cell: ", curr_cell[0], curr_cell[1])
            # print("curr_cell: ", self.board.get_cell(curr_cell[0], curr_cell[1]))
            # continue making steps while the cell is on board and occupied by opponents disk
            # print(self.is_on_board(curr_cell[0], curr_cell[1]))
            # print('curr_player', self.curr_player)
            # print(self.is_opposite_cell(curr_cell[0], curr_cell[1]))
            if self.is_on_board(curr_cell[0], curr_cell[1]) and self.is_opposite_cell(curr_cell[0], curr_cell[1]):
                while self.is_on_board(curr_cell[0], curr_cell[1]) and self.is_opposite_cell(curr_cell[0], curr_cell[1]):
                    curr_cell = (curr_cell[0] + direction[0], curr_cell[1] + direction[1])
                    # print('curr_cell = ', curr_cell)
                # after while loop check why it was interupted
                # if there are no more steps on board -> returns to for loop and checking next direction
                
                if not self.is_on_board(curr_cell[0], curr_cell[1]):
                    continue
            
                # if current cell disk equals to current player disk 
                if not self.is_opposite_cell(curr_cell[0], curr_cell[1]):
                    # create a list to store all steps
                    # print('sec_loop!')
                    curr_cell = list(curr_cell)
                    # print('curr_cell:', curr_cell, 'target_cell:', target_cell)
                    while (curr_cell[0] != target_cell[0] or curr_cell[1] != target_cell[1]):
                    # while curr_cell[1] != target_cell[1]:
                        # curr_cell[0] -= direction[0]
                        # curr_cell[1] -= direction[1]
                        curr_cell[0] = curr_cell[0] - direction[0]
                        curr_cell[1] = curr_cell[1] - direction[1]
                        # print('curr_cell:', curr_cell, 'target_cell:', target_cell)
                        steps.append((curr_cell[0], curr_cell[1]))
                print(steps)
            return steps
