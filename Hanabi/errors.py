desc = """
This file is used to create custom error classes that may 
    be useful for debugging purposes.
"""


class InformationTypeError(Exception):
    """
    """
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return str(self.message)