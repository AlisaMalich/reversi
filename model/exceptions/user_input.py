# import re
# from model.exceptions.errors import Errors

# class UserInputError():
#     def __init__(self) -> None:
#         self.errors = Errors()

# def get_input(self, prompt):
#     while True:
#         try:
#             str = input(prompt)
#             self.error.is_numeric(str)
#         except self.errors as e:
#             print(e)








    # while True:
    #         try:
    #             str = input(prompt)
    #             # lst = [int(s) for s in re.findall('\d', str)]
    #             return lst
    #         except ValueError:
    #             print('Input must be numeric! Try again')


# def get_input(prompt):
#     # str = input(prompt)
#     lst = []
#     while True:
#         # str = input(prompt)
#         # for num in str.split(','):
#             try:
#                 str = input(prompt)
#                 for num in str.split(','):
#                     lst.append(int(num))
#                 return lst
#             except ValueError:
#                 print('Input must be numeric! Try again')

import re
# from model.board import Board

class UserInputError(Exception):
    
    str_format = '^[0-8],[0-8]$'
    mode_format = '^[1-2]$'


    def is_numeric(self, str):
        if not re.match(self.str_format, str):
            raise UserInputError('Input is not in a valid format. Try again!')
    
    def check_mode(self, mode):
        if not re.match(self.mode_format, mode):
            raise UserInputError('Please, choose 1 or 2!')




