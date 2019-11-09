## @file Tune.py

from Note import Note
from ABCParser import *
from FileHandleFactory import FileHandleFactory

class Tune:
    def __init__(self, fileName):
        fileHandle = FileHandleFactory.createReadOnlyFileHandle(fileName)
        self.musicStream = ABCParser.parse(fileHandle)
        self.notesVector

    def show(self):
        self.musicStream.show("text")

tune = Tune("/home/cyprian/Documents/ABC/China/ai_erwa")
tune.show()

