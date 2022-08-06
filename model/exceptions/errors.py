import re
class Errors(Exception):
    
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
            raise Errors('Input is not in a valid format')
