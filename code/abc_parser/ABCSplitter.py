## @file ABCSplitter.py
#   Implementation of class for splitting ABC file.

import io
from FileHandle import ReadOnlyFileHandle

## @class ABCSplitter
# Class for splitting ABC file.
# This assume that ABC file first line starts with '[X or some other single character]:'
# The strings should be validated after the split before using them.
class ABCSplitter:
    @staticmethod
    def split(self, fileHandle):
        contentStream = io.StringIO(fileHandle.read())
        infoString = None
        abcString = None
        currentLine = contentStream.readline()

        while(currentLine and not abcString):
            if currentLine[1] == ':' :
                infoString = infoString + currentLine
                currentLine = contentStream.readline()
            else:
                abcString = currentLine

        abcString = contentStream.read()
        return infoString, abcString