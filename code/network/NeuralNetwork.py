from keras.models import Sequential
from keras.layers import Dense, LSTM, Dropout, Activation
import keras, np_utils, numpy
from keras.callbacks import ModelCheckpoint

class NeuralNetwork:
    def __init__(self, input_shape):
        self.model = Sequential()
        self.model.add(LSTM(256, input_shape=(input_shape[1], input_shape[2]), return_sequences=True))
        self.model.add(Dropout(0.3))
        self.model.add(LSTM(512, return_sequences=True))
        self.model.add(Dropout(0.3))
        self.model.add(LSTM(256))
        self.model.add(Dense(256))
        self.model.add(Dropout(0.3))
        self.model.add(Dense(2421))
        self.model.add(Activation('softmax'))
        self.model.compile(loss='categorical_crossentropy', optimizer='rmsprop')

    def train(self, input, output, filepath):
        self.model.fit(input, output, epochs=100, batch_size=64, verbose=1)
        self.model.save_weights(filepath)

