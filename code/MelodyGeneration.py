from network import NeuralNetwork
from common import TuneLoader, Tune, Note
from music21 import environment
from MusicConverter import MusicConverter, MUSIC_STREAM
import numpy as np

filepath = "weights/weights-first-test-training.hdf5"

GenNN = NeuralNetwork.NeuralNetwork()
GenNN.load_model(filepath)

environment.set('musicxmlPath', '/bin/musescore3' )
tunes = TuneLoader.TuneLoader("ABC/abcChina04")

starter, output = tunes.tunes[0].getTrainData(15)

newMelody = GenNN.generate(starter[0])
MusicConverter.convert(newMelody, MUSIC_STREAM).show('musicxml')
