## @file ABCParser.py
#   Implementation of parsing abc file to neural network input.

from FileHandle import ReadOnlyFileHandle
from ABCValidator import ABCValidator
# TODO: ABC converter - neural network input type has to be specified first

## @class ABCParser
#   ABC file parser.
class ABCParser:
    def __init__(self):
        pass

    # TODO: Implementation cannot go further without implemented ABC converter.
    def parse(self, fileHandle):
        if ABCValidator.validate(fileHandle):
            return fileHandle.read()
        else:
            return None