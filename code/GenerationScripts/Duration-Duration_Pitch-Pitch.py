from network import NeuralNetwork
from music21 import environment
from common import Tune, Note
from utils import compareNewMelody, updateNoteInput, updatePoDInput
from MusicConverter import MusicConverter, MUSIC_STREAM

############################################################################

DD_modelFilepath = "weights/duration-duration"
DD_sequenceLength = 0

PP_modelFilepath = "weights/pitch-pitch"
PP_sequenceLength = 0

newMelodyLength = 0
starter = Tune.Tune("ABC/ABCChina06")

############################################################################

environment.set('musicxmlPath', '/bin/musescore3' )

DD_model = NeuralNetwork.NeuralNetwork()
DD_model.load_model(DD_modelFilepath)
DD_input, temp = starter.getTrainData_noteDuration(DD_sequenceLength)
DD_inputShape = (1, DD_sequenceLength, len(DD_input[0]))

PP_model = NeuralNetwork.NeuralNetwork()
PP_model.load_model(PP_modelFilepath)
PP_input, temp = starter.getTrainData_notePitch(PP_sequenceLength)
PP_inputShape = (1, PP_sequenceLength, len(PP_input[0]))

melody = []
for noteIndex in range(newMelodyLength):
    duration = DD_model.pod_generation(DD_input, DD_inputShape)
    pitch = PP_model.pod_generation(PP_input, PP_inputShape)
    melody.append(Note.Note(pitch, duration))
    updatePoDInput(DD_input, duration)
    updatePoDInput(PP_input, pitch)

MusicConverter.convert(melody, MUSIC_STREAM).show('musicxml')
compareNewMelody(melody)

