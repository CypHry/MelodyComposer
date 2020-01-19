from network import NeuralNetwork
from common import TuneLoader, Tune, Note
from music21 import environment
from MusicConverter import MusicConverter, MUSIC_STREAM
import numpy as np

filepath = "weights/weights-first-test-training-5notes.hdf5"

GenNN = NeuralNetwork.NeuralNetwork()
GenNN.load_model(filepath)

environment.set('musicxmlPath', '/bin/musescore3' )
tunes = TuneLoader.TuneLoader("ABC/abcChina06")

starter, output = tunes.tunes[0].getTrainData(5)

newMelody = GenNN.generate(starter[0])
MusicConverter.convert(newMelody, MUSIC_STREAM).show('musicxml')

tunes = TuneLoader.TuneLoader("ABC/*")
found = 0;
for tune in tunes.tunes:
    for j in range(len(tune.notesStream)):
        if any(tune.notesVector[j:5+j] == newMelody[i:5+i] for i in range(len(newMelody) - 6)):
            found = found+1

print(found)
