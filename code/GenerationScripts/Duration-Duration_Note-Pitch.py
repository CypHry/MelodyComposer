from network import NeuralNetwork
from music21 import environment
from common import Tune, Note
from utils import compareNewMelody, updateNoteInput, updatePoDInput
from MusicConverter import MusicConverter, MUSIC_STREAM

############################################################################

DD_modelFilepath = "weights/duration-duration"
DD_sequenceLength = 0

NP_modelFilepath = "weights/note-pitch"
NP_sequenceLength = 0

newMelodyLength = 0
starter = Tune.Tune("ABC/ABCChina06")

############################################################################

environment.set('musicxmlPath', '/bin/musescore3' )

DD_model = NeuralNetwork.NeuralNetwork()
DD_model.load_model(DD_modelFilepath)
DD_input, temp = starter.getTrainData_noteDuration(DD_sequenceLength)
DD_inputShape = (1, DD_sequenceLength, len(DD_input[0]))

NP_model = NeuralNetwork.NeuralNetwork()
NP_model.load_model(NP_modelFilepath)
NP_input, temp = starter.getTrainData(NP_sequenceLength)
NP_inputShape = (1, NP_sequenceLength, len(NP_input[0]))

melody = []
for noteIndex in range(newMelodyLength):
    duration = DD_model.pod_generation(DD_input, DD_inputShape)
    pitch = NP_model.pod_generation(NP_input, NP_inputShape)
    melody.append(Note.Note(pitch, duration))
    updatePoDInput(DD_input, duration)
    updateNoteInput(NP_input, melody[-1])

MusicConverter.convert(melody, MUSIC_STREAM).show('musicxml')
compareNewMelody(melody)

