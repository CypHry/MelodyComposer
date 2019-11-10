## @file Tune.py

from ABCParser import *
from FileHandleFactory import FileHandleFactory
from MusicConverter import *

class Tune:
    def __init__(self, fileName):
        fileHandle = FileHandleFactory.createReadOnlyFileHandle(fileName)
        self.musicStream = ABCParser.parse(fileHandle)
        self.notesStream = stream.Stream()
        for element in self.musicStream.parts[0].elements:
            for noteOrRest in element.elements:
                self.notesStream.append(noteOrRest)
        self.notesVector = MusicConverter.convert(self.notesStream, NOTES_VECTOR)

    def show(self):
        self.musicStream.show("text")

