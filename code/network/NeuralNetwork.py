from keras.models import Sequential, load_model
from keras.layers import Dense, LSTM, Dropout, Activation
import keras, np_utils, numpy

class NeuralNetwork:
    def __init__(self, filepath):
        self.model = load_model(filepath)

    def __init__(self, input_shape):
        self.model = Sequential()
        self.model.add(LSTM(450, input_shape=(input_shape[1], input_shape[2]), return_sequences=True))
        self.model.add(LSTM(450))
        self.model.add(Dense(input_shape[2]))
        self.model.add(Activation('softmax'))
        self.model.compile(loss='categorical_crossentropy', optimizer='rmsprop')

    def train(self, input, output, filepath):
        self.model.fit(input, output, epochs=100, batch_size=15, verbose=2)
        self.model.save(filepath)

    def generate(self, starter):
        pass