from network import NeuralNetwork
from music21 import environment
from common import Tune, Note
from utils import compareNewMelody, updateNoteInput, updatePoDInput
from MusicConverter import MusicConverter, MUSIC_STREAM

############################################################################

DD_modelFilepath = "../weights/12_duration-duration_sequence20_epoch1_LLD_WD"
DD_sequenceLength = 20

NN_modelFilepath = "../weights/old_weights/3L_2LSTM1D_WD_SL15_model_epoch65_batch15"
NN_sequenceLength = 15

newMelodyLength = 50
starter = Tune.Tune("../ABC/ABCChina06")

inputIndex = 5
inputIndex2 = 0
############################################################################

environment.set('musicxmlPath', '/bin/musescore3' )

DD_model = NeuralNetwork.NeuralNetwork()
DD_model.load_model(DD_modelFilepath)
DD_input, temp = starter.getTrainData_noteDuration(DD_sequenceLength)
DD_input = DD_input[inputIndex]
DD_inputShape = (1, DD_sequenceLength, len(DD_input[0]))

NN_model = NeuralNetwork.NeuralNetwork()
NN_model.load_model(NN_modelFilepath)
NN_input, temp = starter.getTrainData(NN_sequenceLength)
NN_input = NN_input[inputIndex2]
NN_inputShape = (1, NN_sequenceLength, len(NN_input[0]))

melody = []
for noteIndex in range(newMelodyLength):
    duration = DD_model.pod_generation(DD_input, DD_inputShape)
    note = NN_model.note_generation(NN_input, NN_inputShape)
    melody.append(Note.Note(note.pitchVector, duration))
    DD_input = updatePoDInput(DD_input, duration)
    NN_input = updateNoteInput(NN_input, melody[-1])

MusicConverter.convert(melody, MUSIC_STREAM).show('musicxml')
compareNewMelody(melody)

