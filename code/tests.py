from common import Tune, Note
from network import NeuralNetwork
from MusicConverter import *

tune = Tune.Tune("/home/cyprian/Documents/ABC/China/Bu_guo")

filepath = "weights/weights-tests.hdf5"

input, output = tune.getTrainData(15)
network = NeuralNetwork.NeuralNetwork(input.shape)
network.train(input, output, filepath)



