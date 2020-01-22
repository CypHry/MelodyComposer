from common import TuneLoader, Tune, Note
from network import NeuralNetwork
from MusicConverter import *
import numpy as np

tunes = TuneLoader.TuneLoader("ABC/*")

filepath = "weights/2L_1L1BL_WD_model"

input, output = tunes.getTrainData(NeuralNetwork.SEQUENCE_LEN)
input = np.asarray(input, dtype=np.float32)
output = np.asarray(output, dtype=np.float32)
network = NeuralNetwork.NeuralNetwork()
#network.create_model(input.shape)
network.load_model("weights/2L_1L1BL_WD_model")
network.train(input, output, filepath)

