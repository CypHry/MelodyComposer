## @file FileHandleFactory.py
#   This file implements factory for creating FileHandles in a safe way.

# TODO: Add ReadWriteFileHandle

from enum import Enum
from FileHandle import WriteOnlyFileHandle, ReadOnlyFileHandle
import os.path

## @class FileHandleFactory
#   Implements safe way of creating FileHandles.
class FileHandleFactory:
    class FileMode(Enum):
        ReadOnly = "r"
        WriteOnly = "w+"

    ## @brief createFileHandle
    #   This is the only method that should be called.
    def createFileHandle(fileMode, fileName):
        cases = {
            FileHandleFactory.FileMode.ReadOnly: FileHandleFactory._createReadOnlyFileHandle,
            FileHandleFactory.FileMode.WriteOnly: FileHandleFactory._createWriteOnlyFileHandle
        }

        return cases.get(fileMode, None)(fileName)

    def _createReadOnlyFileHandle(fileName):
        if os.path.isfile(fileName):
            return ReadOnlyFileHandle(fileName)
        else:
            return None

    def _createWriteOnlyFileHandle(fileName):
        return WriteOnlyFileHandle(fileName)
