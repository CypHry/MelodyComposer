from network import NeuralNetwork
from common import TuneLoader, Tune, Note
from music21 import environment
from MusicConverter import MusicConverter, MUSIC_STREAM
import numpy as np
from utils import compareNewMelody

filepath = "weights/70_note-note_sequence10_epoch250_LLLLD_WD"

GenNN = NeuralNetwork.NeuralNetwork()
GenNN.load_model(filepath)

environment.set('musicxmlPath', '/bin/musescore3' )
tunes = TuneLoader.TuneLoader("ABC/ABCChina06")

starter, output = tunes.tunes[0].getTrainData(NeuralNetwork.SEQUENCE_LEN)

newMelody = GenNN.generate(starter[15])
MusicConverter.convert(newMelody, MUSIC_STREAM).show('musicxml')

compareNewMelody(newMelody)

