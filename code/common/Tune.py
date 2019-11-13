## @file Tune.py

from ABCParser import *
from FileHandleFactory import FileHandleFactory
from MusicConverter import *
from common import Note
import keras, np_utils, numpy

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

    def getNotesAsInts(self):
        return [note.getIntValue() for note in self.notesVector]

    def getTrainData(self, sequenceLen):
        notes = [note.getOneHot() for note in self.notesVector]
        if len(notes) <= sequenceLen:
            raise Exception("Piece too short.")
        inputVector = []
        outputVector = []
        for i in range(len(notes) - sequenceLen):
            sequence = notes[i:i + sequenceLen]
            inputVector.append(sequence)
            outputVector.append(notes[i+sequenceLen])
        return  inputVector, outputVector

