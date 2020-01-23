from network import NeuralNetwork
from music21 import environment
from common import Tune, Note
from utils import compareNewMelody, updateNoteInput, updatePoDInput
from MusicConverter import MusicConverter, MUSIC_STREAM

############################################################################

ND_modelFilepath = "weights/note-duration"
ND_sequenceLength = 0

NP_modelFilepath = "weights/note-pitch"
NP_sequenceLength = 0

newMelodyLength = 0
starter = Tune.Tune("ABC/ABCChina06")

############################################################################

environment.set('musicxmlPath', '/bin/musescore3' )

ND_model = NeuralNetwork.NeuralNetwork()
ND_model.load_model(ND_modelFilepath)
ND_input, temp = starter.getTrainData(ND_sequenceLength)
ND_inputShape = (1, ND_sequenceLength, len(ND_input[0]))

NP_model = NeuralNetwork.NeuralNetwork()
NP_model.load_model(NP_modelFilepath)
NP_input, temp = starter.getTrainData(NP_sequenceLength)
NP_inputShape = (1, NP_sequenceLength, len(NP_input[0]))

melody = []
for noteIndex in range(newMelodyLength):
    duration = ND_model.pod_generation(ND_input, ND_inputShape)
    pitch = NP_model.pod_generation(NP_input, NP_inputShape)
    melody.append(Note.Note(pitch, duration))
    updateNoteInput(ND_input, melody[-1])
    updateNoteInput(NP_input, melody[-1])

MusicConverter.convert(melody, MUSIC_STREAM).show('musicxml')
compareNewMelody(melody)

