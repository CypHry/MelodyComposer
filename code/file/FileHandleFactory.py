## @file FileHandleFactory.py
#   This file implements factory for creating FileHandles in a safe way.

from FileHandle import WriteOnlyFileHandle, ReadOnlyFileHandle
import os.path

## @class FileHandleFactory
#   Implements safe way of creating FileHandles.
class FileHandleFactory:
    @staticmethod
    def createReadOnlyFileHandle(fileName):
        if os.path.isfile(fileName):
            return ReadOnlyFileHandle(fileName)
        else:
            return None

    @staticmethod
    def createWriteOnlyFileHandle(fileName):
        return WriteOnlyFileHandle(fileName)

