from network import NeuralNetwork
from music21 import environment
from common import Tune, Note
from utils import compareNewMelody, updateNoteInput, updatePoDInput
from MusicConverter import MusicConverter, MUSIC_STREAM

############################################################################

ND_modelFilepath = "../weights/30_note-duration_sequence20_epoch20_LLDD_WD"
ND_sequenceLength = 20

NN_modelFilepath = "../weights/old_weights/3L_2LSTM1D_WD_SL15_model_epoch65_batch15"
NN_sequenceLength = 15

newMelodyLength = 50
starter = Tune.Tune("../ABC/ABCChina06")

inputIndex = 5
inputIndex2 = 15
############################################################################

environment.set('musicxmlPath', '/bin/musescore3' )

ND_model = NeuralNetwork.NeuralNetwork()
ND_model.load_model(ND_modelFilepath)
starterInput, temp = starter.getTrainData(ND_sequenceLength)
ND_input = starterInput[inputIndex]
ND_inputShape = (1, ND_sequenceLength, 450)

NN_model = NeuralNetwork.NeuralNetwork()
NN_model.load_model(NN_modelFilepath)
starterInput, temp = starter.getTrainData(NN_sequenceLength)
NN_input = starterInput[inputIndex]
NN_inputShape = (1, NN_sequenceLength, 450)

melody = []
for noteIndex in range(newMelodyLength):
    duration = ND_model.pod_generation(ND_input, ND_inputShape)
    note = NN_model.note_generation(NN_input, NN_inputShape)
    melody.append(Note.Note(note.pitchVector, duration))
    ND_input = updateNoteInput(ND_input, melody[-1])
    NN_input = updateNoteInput(NN_input, melody[-1])

MusicConverter.convert(melody, MUSIC_STREAM).show('musicxml')
compareNewMelody(melody)
