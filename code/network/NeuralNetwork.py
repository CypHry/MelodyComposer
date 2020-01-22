from keras.models import Sequential, load_model
from keras.layers import Dense, LSTM, Dropout, Activation, Bidirectional
import keras, np_utils, numpy
from common import Note

SEQUENCE_LEN = 15

class NeuralNetwork:
    def __init__(self):
        self.model = Sequential()

    def load_model(self, filepath):
        self.model = load_model(filepath)

    def create_model(self, input_shape):
        self.model = Sequential()
        self.model.add(Bidirectional(LSTM(450, dropout=0.4, recurrent_dropout=0.3, return_sequences=True)))
        self.model.add(LSTM(450, input_shape=(input_shape[1], input_shape[2]), recurrent_dropout=0.3))
        self.model.add(Dense(450))
        self.model.add(Activation("softmax"))
        self.model.compile(loss='categorical_crossentropy', optimizer='rmsprop')

    def train(self, input, output, filepath):
        self.model.fit(input, output, epochs=35, batch_size=15, verbose=2)
        self.model.save(filepath)

    def generate(self, starter):
        melody = []
        for noteIndex in range(50):
            input = numpy.reshape(starter, (1, SEQUENCE_LEN, 450))
            prediction = self.model.predict(input, verbose = 0)
            index = numpy.argmax(prediction)
            newNote = Note.Note(prediction, prediction)
            newNote.setFromIndex(index)
            melody.append(newNote)
            starter = starter[1:]
            starter.append(newNote.getOneHot())
        return melody
