from network import NeuralNetwork
from music21 import environment
from common import Tune, Note
from utils import compareNewMelody, updateNoteInput, updatePoDInput
from MusicConverter import MusicConverter, MUSIC_STREAM

############################################################################

ND_modelFilepath = "weights/note-duration"
ND_sequenceLength = 0

NN_modelFilepath = "weights/note-note"
NN_sequenceLength = 0

newMelodyLength = 0
starter = Tune.Tune("ABC/ABCChina06")

############################################################################

environment.set('musicxmlPath', '/bin/musescore3' )

ND_model = NeuralNetwork.NeuralNetwork()
ND_model.load_model(ND_modelFilepath)
ND_input, temp = starter.getTrainData(ND_sequenceLength)
ND_inputShape = (1, ND_sequenceLength, len(ND_input[0]))

NN_model = NeuralNetwork.NeuralNetwork()
NN_model.load_model(NN_modelFilepath)
NN_input, temp = starter.getTrainData(NN_sequenceLength)
NN_inputShape = (1, NN_sequenceLength, len(NN_input[0]))

melody = []
for noteIndex in range(newMelodyLength):
    duration = ND_model.pod_generation(ND_input, ND_inputShape)
    note = NN_model.note_generation(NN_input, NN_inputShape)
    melody.append(Note.Note(note.pitchVector, duration))
    updateNoteInput(ND_input, melody[-1])
    updateNoteInput(NN_input, melody[-1])

MusicConverter.convert(melody, MUSIC_STREAM).show('musicxml')
compareNewMelody(melody)
