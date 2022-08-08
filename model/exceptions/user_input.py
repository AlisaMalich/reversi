import re

class UserInputError(Exception):
    """Custom exception class to check validity of user input
    """

    str_format = '^[0-8],[0-8]$'
    mode_format = '^[1-2]$'

    def is_numeric(self, str):
        """Check validity of the User input when User enter a cell coordinates to make a move
        """
        if not re.match(self.str_format, str):
            raise UserInputError('Input is not in a valid format. Try again!')
    
    def check_mode(self, mode):
        """Check validity of the User input when User enter a mode of the game
        """
        if not re.match(self.mode_format, mode):
            raise UserInputError('Please, choose 1 or 2!')




