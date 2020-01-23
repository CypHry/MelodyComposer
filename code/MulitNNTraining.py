from common import TuneLoader, Tune, Note
from keras.models import Sequential, load_model
from keras.layers import Dense, LSTM, Dropout, Activation, Bidirectional
import keras, np_utils, numpy
from common import Note
from MusicConverter import *
import numpy as np
import time

tunes = TuneLoader.TuneLoader("ABC/*")


###########################################   1.0   #############################################
print("1.0 / 9.1 START")
sequence = 5

input, output = tunes.getTrainData_duration(sequence)
input = np.asarray(input, dtype=np.float32)
output = np.asarray(output, dtype=np.float32)

model = Sequential()
model.add(LSTM(10, input_shape=(input.shape[1], input.shape[2]), dropout=0.4, recurrent_dropout=0.3, return_sequences=True))
model.add(LSTM(10, dropout=0.1, recurrent_dropout=0.1))
model.add(Dense(10))
model.add(Activation("softmax"))
model.compile(loss='categorical_crossentropy', optimizer='rmsprop')

print("1.0 / 9.1 --- 1 EPOCH")
model.fit(input, output, epochs=1, batch_size=15, verbose=2)
model.save("weights/10_duration-duration_sequence5_epoch1_LLD_WD")

print("1.0 / 9.1 --- 5 EPOCH")
model.fit(input, output, epochs=4, batch_size=15, verbose=2)
model.save("weights/10_duration-duration_sequence5_epoch5_LLD_WD")

print("1.0 / 9.1 --- 10 EPOCH")
model.fit(input, output, epochs=5, batch_size=15, verbose=2)
model.save("weights/10_duration-duration_sequence5_epoch10_LLD_WD")

print("1.0 / 9.1 --- 20 EPOCH")
model.fit(input, output, epochs=10, batch_size=15, verbose=2)
model.save("weights/10_duration-duration_sequence5_epoch20_LLD_WD")

print("1.0 / 9.1 --- 30 EPOCH")
model.fit(input, output, epochs=10, batch_size=15, verbose=2)
model.save("weights/10_duration-duration_sequence5_epoch30_LLD_WD")

print("1.0 / 9.1 --- 40 EPOCH")
model.fit(input, output, epochs=10, batch_size=15, verbose=2)
model.save("weights/10_duration-duration_sequence5_epoch40_LLD_WD")

print("1.0 / 9.1 --- 50 EPOCH")
model.fit(input, output, epochs=10, batch_size=15, verbose=2)
model.save("weights/10_duration-duration_sequence5_epoch50_LLD_WD")

###########################################   1.1   #############################################
print("1.1 / 9.1 START")

sequence = 15

input, output = tunes.getTrainData_duration(sequence)
input = np.asarray(input, dtype=np.float32)
output = np.asarray(output, dtype=np.float32)

model = Sequential()
model.add(LSTM(10, input_shape=(input.shape[1], input.shape[2]), dropout=0.4, recurrent_dropout=0.3, return_sequences=True))
model.add(LSTM(10, dropout=0.1, recurrent_dropout=0.1))
model.add(Dense(10))
model.add(Activation("softmax"))
model.compile(loss='categorical_crossentropy', optimizer='rmsprop')

print("1.1 / 9.1 --- 1 EPOCH")
model.fit(input, output, epochs=1, batch_size=15, verbose=2)
model.save("weights/11_duration-duration_sequence15_epoch1_LLD_WD")

print("1.1 / 9.1 --- 5 EPOCH")
model.fit(input, output, epochs=4, batch_size=15, verbose=2)
model.save("weights/11_duration-duration_sequence15_epoch5_LLD_WD")

print("1.1 / 9.1 --- 10 EPOCH")
model.fit(input, output, epochs=5, batch_size=15, verbose=2)
model.save("weights/11_duration-duration_sequence15_epoch10_LLD_WD")

print("1.1 / 9.1 --- 20 EPOCH")
model.fit(input, output, epochs=10, batch_size=15, verbose=2)
model.save("weights/11_duration-duration_sequence15_epoch20_LLD_WD")

print("1.1 / 9.1 --- 30 EPOCH")
model.fit(input, output, epochs=10, batch_size=15, verbose=2)
model.save("weights/11_duration-duration_sequence15_epoch30_LLD_WD")

print("1.1 / 9.1 --- 40 EPOCH")
model.fit(input, output, epochs=10, batch_size=15, verbose=2)
model.save("weights/11_duration-duration_sequence15_epoch40_LLD_WD")

print("1.1 / 9.1 --- 50 EPOCH")
model.fit(input, output, epochs=10, batch_size=15, verbose=2)
model.save("weights/11_duration-duration_sequence15_epoch50_LLD_WD")

###########################################   1.2   #############################################
print("1.2 / 9.1 START")

sequence = 20

input, output = tunes.getTrainData_duration(sequence)
input = np.asarray(input, dtype=np.float32)
output = np.asarray(output, dtype=np.float32)

model = Sequential()
model.add(LSTM(10, input_shape=(input.shape[1], input.shape[2]), dropout=0.4, recurrent_dropout=0.3, return_sequences=True))
model.add(LSTM(10, dropout=0.1, recurrent_dropout=0.1))
model.add(Dense(10))
model.add(Activation("softmax"))
model.compile(loss='categorical_crossentropy', optimizer='rmsprop')

print("1.2 / 9.1 --- 1 EPOCH")
model.fit(input, output, epochs=1, batch_size=15, verbose=2)
model.save("weights/12_duration-duration_sequence20_epoch1_LLD_WD")

print("1.2 / 9.1 --- 5 EPOCH")
model.fit(input, output, epochs=4, batch_size=15, verbose=2)
model.save("weights/12_duration-duration_sequence20_epoch5_LLD_WD")

print("1.2 / 9.1 --- 10 EPOCH")
model.fit(input, output, epochs=5, batch_size=15, verbose=2)
model.save("weights/12_duration-duration_sequence20_epoch10_LLD_WD")

print("1.2 / 9.1 --- 20 EPOCH")
model.fit(input, output, epochs=10, batch_size=15, verbose=2)
model.save("weights/12_duration-duration_sequence20_epoch20_LLD_WD")

print("1.2 / 9.1 --- 30 EPOCH")
model.fit(input, output, epochs=10, batch_size=15, verbose=2)
model.save("weights/12_duration-duration_sequence20_epoch30_LLD_WD")

print("1.2 / 9.1 --- 40 EPOCH")
model.fit(input, output, epochs=10, batch_size=15, verbose=2)
model.save("weights/12_duration-duration_sequence20_epoch40_LLD_WD")

print("1.2 / 9.1 --- 50 EPOCH")
model.fit(input, output, epochs=10, batch_size=15, verbose=2)
model.save("weights/12_duration-duration_sequence20_epoch50_LLD_WD")


time.sleep(20*60)
###########################################   2.0   #############################################
print("2.0 / 9.1 START")

sequence = 15

input, output = tunes.getTrainData_duration(sequence)
input = np.asarray(input, dtype=np.float32)
output = np.asarray(output, dtype=np.float32)

model = Sequential()
model.add(LSTM(10, input_shape=(input.shape[1], input.shape[2]), dropout=0.4, recurrent_dropout=0.3, return_sequences=True))
model.add(Bidirectional(LSTM(10, dropout=0.1, recurrent_dropout=0.1)))
model.add(Dense(10))
model.add(Activation("softmax"))
model.compile(loss='categorical_crossentropy', optimizer='rmsprop')

print("2.0 / 9.1 --- 1 EPOCH")
model.fit(input, output, epochs=1, batch_size=15, verbose=2)
model.save("weights/20_duration-duration_sequence15_epoch1_LBLD_WD")

print("2.0 / 9.1 --- 5 EPOCH")
model.fit(input, output, epochs=4, batch_size=15, verbose=2)
model.save("weights/20_duration-duration_sequence15_epoch5_LBLD_WD")

print("2.0 / 9.1 --- 10 EPOCH")
model.fit(input, output, epochs=5, batch_size=15, verbose=2)
model.save("weights/20_duration-duration_sequence15_epoch10_LBLD_WD")

print("2.0 / 9.1 --- 20 EPOCH")
model.fit(input, output, epochs=10, batch_size=15, verbose=2)
model.save("weights/20_duration-duration_sequence15_epoch20_LBLD_WD")

print("2.0 / 9.1 --- 30 EPOCH")
model.fit(input, output, epochs=10, batch_size=15, verbose=2)
model.save("weights/20_duration-duration_sequence15_epoch30_LBLD_WD")

print("2.0 / 9.1 --- 40 EPOCH")
model.fit(input, output, epochs=10, batch_size=15, verbose=2)
model.save("weights/20_duration-duration_sequence15_epoch40_LBLD_WD")

print("2.0 / 9.1 --- 50 EPOCH")
model.fit(input, output, epochs=10, batch_size=15, verbose=2)
model.save("weights/20_duration-duration_sequence15_epoch50_LBLD_WD")

###########################################   2.1   #############################################
print("2.1 / 9.1 START")

sequence = 20

input, output = tunes.getTrainData_duration(sequence)
input = np.asarray(input, dtype=np.float32)
output = np.asarray(output, dtype=np.float32)

model = Sequential()
model.add(LSTM(10, input_shape=(input.shape[1], input.shape[2]), dropout=0.4, recurrent_dropout=0.3, return_sequences=True))
model.add(Bidirectional(LSTM(10, dropout=0.1, recurrent_dropout=0.1)))
model.add(Dense(10))
model.add(Activation("softmax"))
model.compile(loss='categorical_crossentropy', optimizer='rmsprop')

print("2.1 / 9.1 --- 1 EPOCH")
model.fit(input, output, epochs=1, batch_size=15, verbose=2)
model.save("weights/21_duration-duration_sequence20_epoch1_LBLD_WD")

print("2.1 / 9.1 --- 5 EPOCH")
model.fit(input, output, epochs=4, batch_size=15, verbose=2)
model.save("weights/21_duration-duration_sequence20_epoch5_LBLD_WD")

print("2.1 / 9.1 --- 10 EPOCH")
model.fit(input, output, epochs=5, batch_size=15, verbose=2)
model.save("weights/21_duration-duration_sequence20_epoch10_LBLD_WD")

print("2.1 / 9.1 --- 20 EPOCH")
model.fit(input, output, epochs=10, batch_size=15, verbose=2)
model.save("weights/21_duration-duration_sequence20_epoch20_LBLD_WD")

print("2.1 / 9.1 --- 30 EPOCH")
model.fit(input, output, epochs=10, batch_size=15, verbose=2)
model.save("weights/21_duration-duration_sequence20_epoch30_LBLD_WD")

print("2.1 / 9.1 --- 40 EPOCH")
model.fit(input, output, epochs=10, batch_size=15, verbose=2)
model.save("weights/21_duration-duration_sequence20_epoch40_LBLD_WD")

print("2.1 / 9.1 --- 50 EPOCH")
model.fit(input, output, epochs=10, batch_size=15, verbose=2)
model.save("weights/21_duration-duration_sequence20_epoch50_LBLD_WD")

###########################################   3.0   #############################################
print("3.0 / 9.1 START")

sequence = 20

input, temp = tunes.getTrainData(sequence)
temp, output = tunes.getTrainData_duration(sequence)
input = np.asarray(input, dtype=np.float32)
output = np.asarray(output, dtype=np.float32)

model = Sequential()
model.add(LSTM(450, input_shape=(input.shape[1], input.shape[2]), dropout=0.4, recurrent_dropout=0.3, return_sequences=True))
model.add(LSTM(100, dropout=0.1, recurrent_dropout=0.1))
model.add(Dense(50))
model.add(Dense(10))
model.add(Activation("softmax"))
model.compile(loss='categorical_crossentropy', optimizer='rmsprop')

print("3.0 / 9.1 --- 1 EPOCH")
model.fit(input, output, epochs=1, batch_size=15, verbose=2)
model.save("weights/30_note-duration_sequence20_epoch1_LLDD_WD")

print("3.0 / 9.1 --- 20 EPOCH")
model.fit(input, output, epochs=19, batch_size=15, verbose=2)
model.save("weights/30_note-duration_sequence20_epoch20_LLDD_WD")

print("3.0 / 9.1 --- 40 EPOCH")
model.fit(input, output, epochs=20, batch_size=15, verbose=2)
model.save("weights/30_note-duration_sequence20_epoch40_LLDD_WD")

print("3.0 / 9.1 --- 60 EPOCH")
model.fit(input, output, epochs=20, batch_size=15, verbose=2)
model.save("weights/30_note-duration_sequence20_epoch60_LLDD_WD")

print("3.0 / 9.1 --- 100 EPOCH")
model.fit(input, output, epochs=40, batch_size=15, verbose=2)
model.save("weights/30_note-duration_sequence20_epoch100_LLDD_WD")

print("3.0 / 9.1 --- 150 EPOCH")
model.fit(input, output, epochs=50, batch_size=15, verbose=2)
model.save("weights/30_note-duration_sequence20_epoch150_LLDD_WD")

time.sleep(60*60)
###########################################   3.1   #############################################
print("3.1 / 9.1 START")

sequence = 10

input, temp = tunes.getTrainData(sequence)
temp, output = tunes.getTrainData_duration(sequence)
input = np.asarray(input, dtype=np.float32)
output = np.asarray(output, dtype=np.float32)

model = Sequential()
model.add(LSTM(450, input_shape=(input.shape[1], input.shape[2]), dropout=0.4, recurrent_dropout=0.3, return_sequences=True))
model.add(LSTM(100, dropout=0.1, recurrent_dropout=0.1))
model.add(Dense(50))
model.add(Dense(10))
model.add(Activation("softmax"))
model.compile(loss='categorical_crossentropy', optimizer='rmsprop')

print("3.1 / 9.1 --- 1 EPOCH")
model.fit(input, output, epochs=1, batch_size=15, verbose=2)
model.save("weights/31_note-duration_sequence10_epoch1_LLDD_WD")

print("3.1 / 9.1 --- 20 EPOCH")
model.fit(input, output, epochs=19, batch_size=15, verbose=2)
model.save("weights/31_note-duration_sequence10_epoch20_LLDD_WD")

print("3.1 / 9.1 --- 40 EPOCH")
model.fit(input, output, epochs=20, batch_size=15, verbose=2)
model.save("weights/31_note-duration_sequence10_epoch40_LLDD_WD")

print("3.1 / 9.1 --- 60 EPOCH")
model.fit(input, output, epochs=20, batch_size=15, verbose=2)
model.save("weights/31_note-duration_sequence10_epoch60_LLDD_WD")

print("3.1 / 9.1 --- 100 EPOCH")
model.fit(input, output, epochs=40, batch_size=15, verbose=2)
model.save("weights/31_note-duration_sequence10_epoch100_LLDD_WD")

print("3.1 / 9.1 --- 150 EPOCH")
model.fit(input, output, epochs=50, batch_size=15, verbose=2)
model.save("weights/31_note-duration_sequence10_epoch150_LLDD_WD")

time.sleep(20*60)
###########################################   4.0   #############################################
print("4.0 / 9.1 START")

sequence = 5

input, output = tunes.getTrainData_pitch(sequence)
input = np.asarray(input, dtype=np.float32)
output = np.asarray(output, dtype=np.float32)

model = Sequential()
model.add(LSTM(45, input_shape=(input.shape[1], input.shape[2]), dropout=0.4, recurrent_dropout=0.3, return_sequences=True))
model.add(LSTM(45, dropout=0.1, recurrent_dropout=0.1))
model.add(Dense(45))
model.add(Activation("softmax"))
model.compile(loss='categorical_crossentropy', optimizer='rmsprop')

print("4.0 / 9.1 --- 1 EPOCH")
model.fit(input, output, epochs=1, batch_size=15, verbose=2)
model.save("weights/40_pitch-pitch_sequence5_epoch1_LLD_WD")

print("4.0 / 9.1 --- 5 EPOCH")
model.fit(input, output, epochs=4, batch_size=15, verbose=2)
model.save("weights/40_pitch-pitch_sequence5_epoch5_LLD_WD")

print("4.0 / 9.1 --- 20 EPOCH")
model.fit(input, output, epochs=15, batch_size=15, verbose=2)
model.save("weights/40_pitch-pitch_sequence5_epoch20_LLD_WD")

print("4.0 / 9.1 --- 30 EPOCH")
model.fit(input, output, epochs=10, batch_size=15, verbose=2)
model.save("weights/40_pitch-pitch_sequence5_epoch30_LLD_WD")

print("4.0 / 9.1 --- 40 EPOCH")
model.fit(input, output, epochs=10, batch_size=15, verbose=2)
model.save("weights/40_pitch-pitch_sequence5_epoch40_LLD_WD")

print("4.0 / 9.1 --- 60 EPOCH")
model.fit(input, output, epochs=20, batch_size=15, verbose=2)
model.save("weights/40_pitch-pitch_sequence5_epoch60_LLD_WD")

###########################################   4.1   #############################################
print("4.1 / 9.1 START")

sequence = 15

input, output = tunes.getTrainData_pitch(sequence)
input = np.asarray(input, dtype=np.float32)
output = np.asarray(output, dtype=np.float32)

model = Sequential()
model.add(LSTM(45, input_shape=(input.shape[1], input.shape[2]), dropout=0.4, recurrent_dropout=0.3, return_sequences=True))
model.add(LSTM(45, dropout=0.1, recurrent_dropout=0.1))
model.add(Dense(45))
model.add(Activation("softmax"))
model.compile(loss='categorical_crossentropy', optimizer='rmsprop')

print("4.1 / 9.1 --- 1 EPOCH")
model.fit(input, output, epochs=1, batch_size=15, verbose=2)
model.save("weights/41_pitch-pitch_sequence15_epoch1_LLD_WD")

print("4.1 / 9.1 --- 5 EPOCH")
model.fit(input, output, epochs=4, batch_size=15, verbose=2)
model.save("weights/41_pitch-pitch_sequence15_epoch5_LLD_WD")

print("4.1 / 9.1 --- 20 EPOCH")
model.fit(input, output, epochs=15, batch_size=15, verbose=2)
model.save("weights/41_pitch-pitch_sequence15_epoch20_LLD_WD")

print("4.1 / 9.1 --- 30 EPOCH")
model.fit(input, output, epochs=10, batch_size=15, verbose=2)
model.save("weights/41_pitch-pitch_sequence15_epoch30_LLD_WD")

print("4.1 / 9.1 --- 40 EPOCH")
model.fit(input, output, epochs=10, batch_size=15, verbose=2)
model.save("weights/41_pitch-pitch_sequence15_epoch40_LLD_WD")

print("4.1 / 9.1 --- 60 EPOCH")
model.fit(input, output, epochs=20, batch_size=15, verbose=2)
model.save("weights/41_pitch-pitch_sequence15_epoch60_LLD_WD")


time.sleep(20*60)
###########################################   4.2   #############################################
print("4.2 / 9.1 START")

sequence = 20

input, output = tunes.getTrainData_pitch(sequence)
input = np.asarray(input, dtype=np.float32)
output = np.asarray(output, dtype=np.float32)

model = Sequential()
model.add(LSTM(45, input_shape=(input.shape[1], input.shape[2]), dropout=0.4, recurrent_dropout=0.3, return_sequences=True))
model.add(LSTM(45, dropout=0.1, recurrent_dropout=0.1))
model.add(Dense(45))
model.add(Activation("softmax"))
model.compile(loss='categorical_crossentropy', optimizer='rmsprop')

print("4.2 / 9.1 --- 1 EPOCH")
model.fit(input, output, epochs=1, batch_size=15, verbose=2)
model.save("weights/42_pitch-pitch_sequence20_epoch1_LLD_WD")

print("4.2 / 9.1 --- 5 EPOCH")
model.fit(input, output, epochs=4, batch_size=15, verbose=2)
model.save("weights/42_pitch-pitch_sequence20_epoch5_LLD_WD")

print("4.2 / 9.1 --- 20 EPOCH")
model.fit(input, output, epochs=15, batch_size=15, verbose=2)
model.save("weights/42_pitch-pitch_sequence20_epoch20_LLD_WD")

print("4.2 / 9.1 --- 30 EPOCH")
model.fit(input, output, epochs=10, batch_size=15, verbose=2)
model.save("weights/42_pitch-pitch_sequence20_epoch30_LLD_WD")

print("4.2 / 9.1 --- 40 EPOCH")
model.fit(input, output, epochs=10, batch_size=15, verbose=2)
model.save("weights/42_pitch-pitch_sequence20_epoch40_LLD_WD")

print("4.2 / 9.1 --- 60 EPOCH")
model.fit(input, output, epochs=20, batch_size=15, verbose=2)
model.save("weights/42_pitch-pitch_sequence20_epoch60_LLD_WD")

###########################################   5.0   #############################################
print("5.0 / 9.1 START")

sequence = 15

input, output = tunes.getTrainData_pitch(sequence)
input = np.asarray(input, dtype=np.float32)
output = np.asarray(output, dtype=np.float32)

model = Sequential()
model.add(LSTM(45, input_shape=(input.shape[1], input.shape[2]), dropout=0.4, recurrent_dropout=0.3, return_sequences=True))
model.add(Bidirectional(LSTM(10, dropout=0.1, recurrent_dropout=0.1)))
model.add(Dense(45))
model.add(Activation("softmax"))
model.compile(loss='categorical_crossentropy', optimizer='rmsprop')

print("5.0 / 9.1 --- 1 EPOCH")
model.fit(input, output, epochs=1, batch_size=15, verbose=2)
model.save("weights/50_pitch-pitch_sequence15_epoch1_LBLD_WD")

print("5.0 / 9.1 --- 5 EPOCH")
model.fit(input, output, epochs=4, batch_size=15, verbose=2)
model.save("weights/50_pitch-pitch_sequence15_epoch5_LBLD_WD")

print("5.0 / 9.1 --- 20 EPOCH")
model.fit(input, output, epochs=15, batch_size=15, verbose=2)
model.save("weights/50_pitch-pitch_sequence15_epoch20_LBLD_WD")

print("5.0 / 9.1 --- 30 EPOCH")
model.fit(input, output, epochs=10, batch_size=15, verbose=2)
model.save("weights/50_pitch-pitch_sequence15_epoch30_LBLD_WD")

print("5.0 / 9.1 --- 40 EPOCH")
model.fit(input, output, epochs=10, batch_size=15, verbose=2)
model.save("weights/50_pitch-pitch_sequence15_epoch40_LBLD_WD")

print("5.0 / 9.1 --- 60 EPOCH")
model.fit(input, output, epochs=20, batch_size=15, verbose=2)
model.save("weights/50_pitch-pitch_sequence15_epoch60_LBLD_WD")

###########################################   5.1   #############################################
print("5.1 / 9.1 START")

sequence = 20

input, output = tunes.getTrainData_pitch(sequence)
input = np.asarray(input, dtype=np.float32)
output = np.asarray(output, dtype=np.float32)

model = Sequential()
model.add(LSTM(45, input_shape=(input.shape[1], input.shape[2]), dropout=0.4, recurrent_dropout=0.3, return_sequences=True))
model.add(Bidirectional(LSTM(10, dropout=0.1, recurrent_dropout=0.1)))
model.add(Dense(45))
model.add(Activation("softmax"))
model.compile(loss='categorical_crossentropy', optimizer='rmsprop')

print("5.1 / 9.1 --- 1 EPOCH")
model.fit(input, output, epochs=1, batch_size=15, verbose=2)
model.save("weights/51_pitch-pitch_sequence20_epoch1_LBLD_WD")

print("5.1 / 9.1 --- 5 EPOCH")
model.fit(input, output, epochs=4, batch_size=15, verbose=2)
model.save("weights/51_pitch-pitch_sequence20_epoch5_LBLD_WD")

print("5.1 / 9.1 --- 20 EPOCH")
model.fit(input, output, epochs=15, batch_size=15, verbose=2)
model.save("weights/51_pitch-pitch_sequence20_epoch20_LBLD_WD")

print("5.1 / 9.1 --- 30 EPOCH")
model.fit(input, output, epochs=10, batch_size=15, verbose=2)
model.save("weights/51_pitch-pitch_sequence20_epoch30_LBLD_WD")

print("5.1 / 9.1 --- 40 EPOCH")
model.fit(input, output, epochs=10, batch_size=15, verbose=2)
model.save("weights/51_pitch-pitch_sequence20_epoch40_LBLD_WD")

print("5.1 / 9.1 --- 60 EPOCH")
model.fit(input, output, epochs=20, batch_size=15, verbose=2)
model.save("weights/51_pitch-pitch_sequence20_epoch60_LBLD_WD")


time.sleep(60*60)
###########################################   6.0   #############################################
print("6.0 / 9.1 START")

sequence = 20

input, temp = tunes.getTrainData(sequence)
temp, output = tunes.getTrainData_pitch(sequence)
input = np.asarray(input, dtype=np.float32)
output = np.asarray(output, dtype=np.float32)

model = Sequential()
model.add(LSTM(450, input_shape=(input.shape[1], input.shape[2]), dropout=0.4, recurrent_dropout=0.3, return_sequences=True))
model.add(LSTM(100, dropout=0.1, recurrent_dropout=0.1))
model.add(Dense(50))
model.add(Dense(45))
model.add(Activation("softmax"))
model.compile(loss='categorical_crossentropy', optimizer='rmsprop')

print("6.0 / 9.1 --- 1 EPOCH")
model.fit(input, output, epochs=1, batch_size=15, verbose=2)
model.save("weights/60_note-pitch_sequence20_epoch1_LLDD_WD")

print("6.0 / 9.1 --- 20 EPOCH")
model.fit(input, output, epochs=19, batch_size=15, verbose=2)
model.save("weights/60_note-pitch_sequence20_epoch20_LLDD_WD")

print("6.0 / 9.1 --- 50 EPOCH")
model.fit(input, output, epochs=30, batch_size=15, verbose=2)
model.save("weights/60_note-pitch_sequence20_epoch50_LLDD_WD")

print("6.0 / 9.1 --- 100 EPOCH")
model.fit(input, output, epochs=50, batch_size=15, verbose=2)
model.save("weights/60_note-pitch_sequence20_epoch100_LLDD_WD")

print("6.0 / 9.1 --- 150 EPOCH")
model.fit(input, output, epochs=50, batch_size=15, verbose=2)
model.save("weights/60_note-pitch_sequence20_epoch150_LLDD_WD")

time.sleep(60*60)
###########################################   6.1   #############################################
print("6.1 / 9.1 START")

sequence = 10

input, temp = tunes.getTrainData(sequence)
temp, output = tunes.getTrainData_pitch(sequence)
input = np.asarray(input, dtype=np.float32)
output = np.asarray(output, dtype=np.float32)

model = Sequential()
model.add(LSTM(450, input_shape=(input.shape[1], input.shape[2]), dropout=0.4, recurrent_dropout=0.3, return_sequences=True))
model.add(LSTM(100, dropout=0.1, recurrent_dropout=0.1))
model.add(Dense(50))
model.add(Dense(45))
model.add(Activation("softmax"))
model.compile(loss='categorical_crossentropy', optimizer='rmsprop')

print("6.1 / 9.1 --- 1 EPOCH")
model.fit(input, output, epochs=1, batch_size=15, verbose=2)
model.save("weights/61note-pitch_sequence10_epoch1_LLDD_WD")

print("6.1 / 9.1 --- 20 EPOCH")
model.fit(input, output, epochs=19, batch_size=15, verbose=2)
model.save("weights/61_note-pitch_sequence10_epoch20_LLDD_WD")

print("6.1 / 9.1 --- 50 EPOCH")
model.fit(input, output, epochs=30, batch_size=15, verbose=2)
model.save("weights/61_note-pitch_sequence10_epoch50_LLDD_WD")

print("6.1 / 9.1 --- 100 EPOCH")
model.fit(input, output, epochs=50, batch_size=15, verbose=2)
model.save("weights/61_note-pitch_sequence10_epoch100_LLDD_WD")

print("6.1 / 9.1 --- 150 EPOCH")
model.fit(input, output, epochs=50, batch_size=15, verbose=2)
model.save("weights/61_note-pitch_sequence10_epoch150_LLDD_WD")


time.sleep(20*60)
###########################################   7.0   #############################################
print("7.0 / 9.1 START")

sequence = 10

input, output = tunes.getTrainData(sequence)
input = np.asarray(input, dtype=np.float32)
output = np.asarray(output, dtype=np.float32)

model = Sequential()
model.add(LSTM(450, input_shape=(input.shape[1], input.shape[2]), dropout=0.4, recurrent_dropout=0.3, return_sequences=True))
model.add(LSTM(100, dropout=0.1, recurrent_dropout=0.1, return_sequences=True))
model.add(LSTM(100, dropout=0.3, recurrent_dropout=0.1, return_sequences=True))
model.add(LSTM(200, dropout=0.4, recurrent_dropout=0.1))
model.add(Dense(450))
model.add(Activation("softmax"))
model.compile(loss='categorical_crossentropy', optimizer='rmsprop')

print("7.0 / 9.1 --- 1 EPOCH")
model.fit(input, output, epochs=1, batch_size=15, verbose=2)
model.save("weights/70_note-note_sequence10_epoch1_LLLLD_WD")

print("7.0 / 9.1 --- 50 EPOCH")
model.fit(input, output, epochs=49, batch_size=15, verbose=2)
model.save("weights/70_note-note_sequence10_epoch50_LLLLD_WD")

print("7.0 / 9.1 --- 100 EPOCH")
model.fit(input, output, epochs=50, batch_size=15, verbose=2)
model.save("weights/70_note-note_sequence10_epoch100_LLLLD_WD")

print("7.0 / 9.1 --- 150 EPOCH")
model.fit(input, output, epochs=50, batch_size=15, verbose=2)
model.save("weights/70_note-note_sequence10_epoch150_LLLLD_WD")

print("7.0 / 9.1 --- 200 EPOCH")
model.fit(input, output, epochs=50, batch_size=15, verbose=2)
model.save("weights/70_note-note_sequence10_epoch200_LLLLD_WD")

print("7.0 / 9.1 --- 250 EPOCH")
model.fit(input, output, epochs=50, batch_size=15, verbose=2)
model.save("weights/70_note-note_sequence10_epoch250_LLLLD_WD")

time.sleep(20*60)
###########################################   7.1   #############################################
print("7.1 / 9.1 START")

sequence = 20

input, output = tunes.getTrainData(sequence)
input = np.asarray(input, dtype=np.float32)
output = np.asarray(output, dtype=np.float32)

model = Sequential()
model.add(LSTM(450, input_shape=(input.shape[1], input.shape[2]), dropout=0.4, recurrent_dropout=0.3, return_sequences=True))
model.add(LSTM(100, dropout=0.1, recurrent_dropout=0.1, return_sequences=True))
model.add(LSTM(100, dropout=0.3, recurrent_dropout=0.1, return_sequences=True))
model.add(LSTM(200, dropout=0.4, recurrent_dropout=0.1))
model.add(Dense(450))
model.add(Activation("softmax"))
model.compile(loss='categorical_crossentropy', optimizer='rmsprop')

print("7.1 / 9.1 --- 1 EPOCH")
model.fit(input, output, epochs=1, batch_size=15, verbose=2)
model.save("weights/71_note-note_sequence20_epoch1_LLLLD_WD")

print("7.1 / 9.1 --- 50 EPOCH")
model.fit(input, output, epochs=49, batch_size=15, verbose=2)
model.save("weights/71_note-note_sequence20_epoch50_LLLLD_WD")

print("7.1 / 9.1 --- 100 EPOCH")
model.fit(input, output, epochs=50, batch_size=15, verbose=2)
model.save("weights/71_note-note_sequence20_epoch100_LLLLD_WD")

print("7.1 / 9.1 --- 150 EPOCH")
model.fit(input, output, epochs=50, batch_size=15, verbose=2)
model.save("weights/71_note-note_sequence20_epoch150_LLLLD_WD")

print("7.1 / 9.1 --- 200 EPOCH")
model.fit(input, output, epochs=50, batch_size=15, verbose=2)
model.save("weights/71_note-note_sequence20_epoch200_LLLLD_WD")

print("7.1 / 9.1 --- 250 EPOCH")
model.fit(input, output, epochs=50, batch_size=15, verbose=2)
model.save("weights/71_note-note_sequence20_epoch250_LLLLD_WD")

time.sleep(60*60)
###########################################   8.0   #############################################
print("8.0 / 9.1 START")

sequence = 10

input, output = tunes.getTrainData(sequence)
input = np.asarray(input, dtype=np.float32)
output = np.asarray(output, dtype=np.float32)

model = Sequential()
model.add(LSTM(450, input_shape=(input.shape[1], input.shape[2]), dropout=0.4, recurrent_dropout=0.3, return_sequences=True))
model.add(LSTM(100, dropout=0.1, recurrent_dropout=0.1, return_sequences=True))
model.add(Bidirectional(LSTM(100, dropout=0.1, recurrent_dropout=0.1, return_sequences=True)))
model.add(LSTM(200, dropout=0.4, recurrent_dropout=0.2))
model.add(Dense(450))
model.add(Dense(450))
model.add(Activation("softmax"))
model.compile(loss='categorical_crossentropy', optimizer='rmsprop')

print("8.0 / 9.1 --- 1 EPOCH")
model.fit(input, output, epochs=1, batch_size=15, verbose=2)
model.save("weights/80_note-note_sequence10_epoch1_LLBLLDD_WD")

print("8.0 / 9.1 --- 50 EPOCH")
model.fit(input, output, epochs=49, batch_size=15, verbose=2)
model.save("weights/80_note-note_sequence10_epoch50_LLBLLDD_WD")

print("8.0 / 9.1 --- 100 EPOCH")
model.fit(input, output, epochs=50, batch_size=15, verbose=2)
model.save("weights/80_note-note_sequence10_epoch100_LLBLLDD_WD")

print("8.0 / 9.1 --- 150 EPOCH")
model.fit(input, output, epochs=50, batch_size=15, verbose=2)
model.save("weights/80_note-note_sequence10_epoch150_LLBLLDD_WD")

print("8.0 / 9.1 --- 200 EPOCH")
model.fit(input, output, epochs=50, batch_size=15, verbose=2)
model.save("weights/80_note-note_sequence10_epoch200_LLBLLDD_WD")

print("8.0 / 9.1 --- 250 EPOCH")
model.fit(input, output, epochs=50, batch_size=15, verbose=2)
model.save("weights/80_note-note_sequence10_epoch250_LLBLLDD_WD")

time.sleep(60*60)
###########################################   8.1   #############################################
print("8.1 / 9.1 START")

sequence = 20

input, output = tunes.getTrainData(sequence)
input = np.asarray(input, dtype=np.float32)
output = np.asarray(output, dtype=np.float32)

model = Sequential()
model.add(LSTM(450, input_shape=(input.shape[1], input.shape[2]), dropout=0.4, recurrent_dropout=0.3, return_sequences=True))
model.add(LSTM(100, dropout=0.1, recurrent_dropout=0.1, return_sequences=True))
model.add(Bidirectional(LSTM(100, dropout=0.1, recurrent_dropout=0.1, return_sequences=True)))
model.add(LSTM(200, dropout=0.4, recurrent_dropout=0.2))
model.add(Dense(450))
model.add(Dense(450))
model.add(Activation("softmax"))
model.compile(loss='categorical_crossentropy', optimizer='rmsprop')

print("8.1 / 9.1 --- 1 EPOCH")
model.fit(input, output, epochs=1, batch_size=15, verbose=2)
model.save("weights/81_note-note_sequence20_epoch1_LLBLLDD_WD")

print("8.1 / 9.1 --- 50 EPOCH")
model.fit(input, output, epochs=49, batch_size=15, verbose=2)
model.save("weights/81_note-note_sequence20_epoch50_LLBLLDD_WD")

print("8.1 / 9.1 --- 100 EPOCH")
model.fit(input, output, epochs=50, batch_size=15, verbose=2)
model.save("weights/81_note-note_sequence20_epoch100_LLBLLDD_WD")

print("8.1 / 9.1 --- 150 EPOCH")
model.fit(input, output, epochs=50, batch_size=15, verbose=2)
model.save("weights/81_note-note_sequence20_epoch150_LLBLLDD_WD")

print("8.1 / 9.1 --- 200 EPOCH")
model.fit(input, output, epochs=50, batch_size=15, verbose=2)
model.save("weights/81_note-note_sequence20_epoch200_LLBLLDD_WD")

print("8.1 / 9.1 --- 250 EPOCH")
model.fit(input, output, epochs=50, batch_size=15, verbose=2)
model.save("weights/81_note-note_sequence20_epoch250_LLBLLDD_WD")

time.sleep(60*60)
###########################################   8.2   #############################################
print("8.2 / 9.1 START")

sequence = 40

input, output = tunes.getTrainData(sequence)
input = np.asarray(input, dtype=np.float32)
output = np.asarray(output, dtype=np.float32)

model = Sequential()
model.add(LSTM(450, input_shape=(input.shape[1], input.shape[2]), dropout=0.4, recurrent_dropout=0.3, return_sequences=True))
model.add(LSTM(100, dropout=0.1, recurrent_dropout=0.1, return_sequences=True))
model.add(Bidirectional(LSTM(100, dropout=0.1, recurrent_dropout=0.1, return_sequences=True)))
model.add(LSTM(200, dropout=0.4, recurrent_dropout=0.2))
model.add(Dense(450))
model.add(Dense(450))
model.add(Activation("softmax"))
model.compile(loss='categorical_crossentropy', optimizer='rmsprop')

print("8.2 / 9.1 --- 1 EPOCH")
model.fit(input, output, epochs=1, batch_size=15, verbose=2)
model.save("weights/82_note-note_sequence40_epoch1_LLBLLDD_WD")

print("8.2 / 9.1 --- 50 EPOCH")
model.fit(input, output, epochs=49, batch_size=15, verbose=2)
model.save("weights/82_note-note_sequence40_epoch50_LLBLLDD_WD")

print("8.2 / 9.1 --- 100 EPOCH")
model.fit(input, output, epochs=50, batch_size=15, verbose=2)
model.save("weights/82_note-note_sequence40_epoch100_LLBLLDD_WD")

print("8.2 / 9.1 --- 150 EPOCH")
model.fit(input, output, epochs=50, batch_size=15, verbose=2)
model.save("weights/82_note-note_sequence40_epoch150_LLBLLDD_WD")

print("8.2 / 9.1 --- 200 EPOCH")
model.fit(input, output, epochs=50, batch_size=15, verbose=2)
model.save("weights/82_note-note_sequence40_epoch200_LLBLLDD_WD")

print("8.2 / 9.1 --- 250 EPOCH")
model.fit(input, output, epochs=50, batch_size=15, verbose=2)
model.save("weights/82_note-note_sequence40_epoch250_LLBLLDD_WD")

print("8.2 / 9.1 --- 300 EPOCH")
model.fit(input, output, epochs=50, batch_size=15, verbose=2)
model.save("weights/82_note-note_sequence40_epoch300_LLBLLDD_WD")

###########################################   9.0   #############################################
print("9.0 / 9.1 START")

sequence = 5

input, output = tunes.getTrainData_duration(sequence)
input = np.asarray(input, dtype=np.float32)
output = np.asarray(output, dtype=np.float32)

model = Sequential()
model.add(LSTM(10, input_shape=(input.shape[1], input.shape[2]), dropout=0.4, recurrent_dropout=0.3))
model.add(Dense(10))
model.add(Activation("softmax"))
model.compile(loss='categorical_crossentropy', optimizer='rmsprop')

print("9.0 / 9.1 1 EPOCH")
model.fit(input, output, epochs=1, batch_size=15, verbose=2)
model.save("weights/90_duration-duration_sequence5_epoch1_LD_WD")

print("9.0 / 9.1 5 EPOCH")
model.fit(input, output, epochs=4, batch_size=15, verbose=2)
model.save("weights/90_duration-duration_sequence5_epoch5_LD_WD")

print("9.0 / 9.1 10 EPOCH")
model.fit(input, output, epochs=5, batch_size=15, verbose=2)
model.save("weights/90_duration-duration_sequence5_epoch10_LD_WD")

print("9.0 / 9.1 20 EPOCH")
model.fit(input, output, epochs=10, batch_size=15, verbose=2)
model.save("weights/90_duration-duration_sequence5_epoch20_LD_WD")

print("9.0 / 9.1 30 EPOCH")
model.fit(input, output, epochs=10, batch_size=15, verbose=2)
model.save("weights/90_duration-duration_sequence5_epoch30_LD_WD")

print("9.0 / 9.1 40 EPOCH")
model.fit(input, output, epochs=10, batch_size=15, verbose=2)
model.save("weights/90_duration-duration_sequence5_epoch40_LD_WD")

print("9.0 / 9.1 50 EPOCH")
model.fit(input, output, epochs=10, batch_size=15, verbose=2)
model.save("weights/90_duration-duration_sequence5_epoch50_LD_WD")

###########################################   9.1   #############################################
print("9.1 / 9.1 START")

sequence = 15

input, output = tunes.getTrainData_duration(sequence)
input = np.asarray(input, dtype=np.float32)
output = np.asarray(output, dtype=np.float32)

model = Sequential()
model.add(LSTM(10, input_shape=(input.shape[1], input.shape[2]), dropout=0.4, recurrent_dropout=0.3))
model.add(Dense(10))
model.add(Activation("softmax"))
model.compile(loss='categorical_crossentropy', optimizer='rmsprop')

print("9.1 / 9.1 1 EPOCH")
model.fit(input, output, epochs=1, batch_size=15, verbose=2)
model.save("weights/91_duration-duration_sequence15_epoch1_LD_WD")

print("9.0 / 9.1 5 EPOCH")
model.fit(input, output, epochs=4, batch_size=15, verbose=2)
model.save("weights/91_duration-duration_sequence15_epoch5_LD_WD")

print("9.0 / 9.1 10 EPOCH")
model.fit(input, output, epochs=5, batch_size=15, verbose=2)
model.save("weights/91_duration-duration_sequence15_epoch10_LD_WD")

print("9.0 / 9.1 20 EPOCH")
model.fit(input, output, epochs=10, batch_size=15, verbose=2)
model.save("weights/91_duration-duration_sequence15_epoch20_LD_WD")

print("9.0 / 9.1 30 EPOCH")
model.fit(input, output, epochs=10, batch_size=15, verbose=2)
model.save("weights/91_duration-duration_sequence15_epoch30_LD_WD")

print("9.0 / 9.1 40 EPOCH")
model.fit(input, output, epochs=10, batch_size=15, verbose=2)
model.save("weights/91_duration-duration_sequence15_epoch40_LD_WD")

print("9.0 / 9.1 50 EPOCH")
model.fit(input, output, epochs=10, batch_size=15, verbose=2)
model.save("weights/91_duration-duration_sequence15_epoch50_LD_WD")

