## @file ABCParser.py
#   Implementation of parsing abc file to neural network input.

from FileHandle import ReadOnlyFileHandle
from ABCKeyTransposer import *
from music21 import *

## @class ABCParser
#   ABC file parser.
class ABCParser:
    @staticmethod
    def parse(fileHandle):
        content = fileHandle.read()
        musicStream = converter.parseData(content)
        abcHandler = abcFormat.ABCHandler()
        abcHandler.process(content)
        key = None
        for token in abcHandler.tokens:
            if token.isKey():
                key = token.getKeySignatureObject()
                break

        return ABCKeyTransposer.transposeToC(musicStream, key)

