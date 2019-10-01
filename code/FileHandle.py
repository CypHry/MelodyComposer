## @file FileHandle.py
#   File contains implementation of FileHandle class.
#   This should be used to operate with files.

from abc import ABC, abstractmethod

## @class FileHandle
#   This is just the base class for all file handles.
#   It should not be used as a standalone as it does nothing useful.
class FileHandle(ABC):
    def __init__(self, filename, mode):
        self.file = open(filename, mode)

    def __del__(self):
        self.file.close();

    @abstractmethod
    def read(self):
        return None

    @abstractmethod
    def write(self, content):
        pass


## @class ReadOnlyFileHandle:
#   Handle for read only files
class ReadOnlyFileHandle(FileHandle):
    def __init__(self, filename):
        super().__init__(filename, "r")
        self.content = self.file.read()

    def __del__(self):
        FileHandle.__del__(self)

    def read(self):
        return self.content

    def write(self, content):
        pass


## @class ReadOnlyFileHandle:
#   Handle for write only files.
#   Creates new file if specified not exist.
class WriteOnlyFileHandle(FileHandle):
    def __init__(self, filename):
        super().__init__(filename, "w+")

    def __del__(self):
        FileHandle.__del__(self)

    def read(self):
        return None

    def write(self, content):
        self.file.write(content)