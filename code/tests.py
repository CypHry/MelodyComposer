from common import TuneLoader, Tune, Note
from network import NeuralNetwork
from MusicConverter import *
import numpy as np

tunes = TuneLoader.TuneLoader("ABC/*")

filepath = "weights/weights-ABC-files-tests.hdf5"

input, output = tunes.getTrainData(15)
input = np.asarray(input, dtype=np.float32)
output = np.asarray(output, dtype=np.float32)

network = NeuralNetwork.NeuralNetwork(input.shape)
network.train(input, output, filepath)



