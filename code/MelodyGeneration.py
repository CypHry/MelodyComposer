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


filepath = "weights/3Layers-40epochs-15batch-15notes-withDropout-withRDropout.hdf5"

GenNN = NeuralNetwork.NeuralNetwork()
GenNN.load_model(filepath)

environment.set('musicxmlPath', '/bin/musescore3' )
tunes = TuneLoader.TuneLoader("ABC/abcChina06")

starter, output = tunes.tunes[0].getTrainData(NeuralNetwork.SEQUENCE_LEN)

newMelody = GenNN.generate(starter[6])
MusicConverter.convert(newMelody, MUSIC_STREAM).show('musicxml')

compareNewMelody(newMelody)

