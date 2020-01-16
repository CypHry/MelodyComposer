from network import NeuralNetwork

filepath = "weights/weights-first-test-training.hdf5"

GenNN = NeuralNetwork.NeuralNetwork()
GenNN.load_model(filepath)

