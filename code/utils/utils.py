from network import NeuralNetwork
from common import TuneLoader, Tune, Note
from music21 import environment
from MusicConverter import MusicConverter, MUSIC_STREAM
import numpy as np

def compareNewMelody(newMelody):
    tunes = TuneLoader.TuneLoader("ABC/*")
    found = 0;
    for tune in tunes.tunes:
        inTune = 0
        for j in range(len(tune.notesStream)):
            if any(tune.notesVector[j:5 + j] == newMelody[i:5 + i] for i in range(len(newMelody) - 6)):
                found = found + 1
                inTune = inTune + 1
        if inTune > 0:
            print(inTune)
            print(tune.musicStream.metadata.title)
            if inTune > 15:
                tune.notesStream.show('musicxml')

    print(found)
    return

def createBaggingEnsembles(input, output):
    pass

