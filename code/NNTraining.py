from common import TuneLoader, Tune, Note
from network import NeuralNetwork
from MusicConverter import *
import numpy as np

tunes = TuneLoader.TuneLoader("ABC/*")

filepath = "weights/weights-first-test-training-5notes.hdf5"

input, output = tunes.getTrainData(5)
input = np.asarray(input, dtype=np.float32)
output = np.asarray(output, dtype=np.float32)
network = NeuralNetwork.NeuralNetwork()
network.create_model(input.shape)
network.train(input, output, filepath)

