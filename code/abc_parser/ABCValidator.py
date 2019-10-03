## @file ABCValidator.py
#   Implementation of abc file validator.

from FileHandle import ReadOnlyFileHandle
from ABCSplitter import ABCSplitter

## @class ABCValidator
#   ABC file validator.
class ABCValidator:
    def validate(self, fileHandle):
        infoString, abcString = ABCSplitter.split(fileHandle)

        if not _checkInfo(infoString) or not _checkABC(abcString):
            return False
        return True

    # TODO: Converter needs to be implemented first
    #   Currently I dont know which information is actually needed
    def _checkInfo(self):
        return True

    def _checkABC(self):
        return True