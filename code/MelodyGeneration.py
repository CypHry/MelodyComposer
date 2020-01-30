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
tune = Tune.Tune("ABC/ABCChina06")

tune.show("text")

