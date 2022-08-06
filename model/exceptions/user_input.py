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
class UserInputError(Exception):
    
    # def __init__(self):
    #     super().__init__()
    #     self.str = str
    #     self.str_format = '^[0-8],[0-8]$'
    str_format = '^[0-8],[0-8]$'

    # def __str__(self) -> str:
    #     return f'Input is not in a valid format'

    def is_numeric(self, str):
        if not re.match(self.str_format, str):
            # raise Errors(str)
            raise UserInputError('Input is not in a valid format')


