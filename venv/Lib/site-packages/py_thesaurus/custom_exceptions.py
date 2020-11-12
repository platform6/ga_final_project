"""Module for defining custom exceptions"""


class PosTagError(Exception):
    """Exception raised when incorrect pos tag is passed to Thesaurus.get_synonym"""

    def __init__(self, message):
        super(PosTagError, self).__init__(message)
        self.message = message

    # __str__ is to print() the value
    def __str__(self):
        return(repr(self.message))
