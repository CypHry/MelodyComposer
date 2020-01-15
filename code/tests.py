from common import TuneLoader, Tune, Note
from network import NeuralNetwork
from MusicConverter import *
import numpy as np
from music21 import environment

environment.set('musicxmlPath', '/bin/musescore3' )
tunes = TuneLoader.TuneLoader("ABC/abcChina04")

MusicConverter.convert(tunes.tunes[0].notesVector, MUSIC_STREAM).show('musicxml')


