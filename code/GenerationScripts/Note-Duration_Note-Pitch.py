from network import NeuralNetwork
from music21 import environment
from common import Tune, Note
from utils import compareNewMelody, updateNoteInput, updatePoDInput
from MusicConverter import MusicConverter, MUSIC_STREAM

############################################################################

ND_modelFilepath = "../weights/30_note-duration_sequence20_epoch20_LLDD_WD"
ND_sequenceLength = 20

NP_modelFilepath = "../weights/60_note-pitch_sequence20_epoch20_LLDD_WD"
NP_sequenceLength = 20

newMelodyLength = 50
starter = Tune.Tune("../ABC/ABCChina06")

inputIndex = 0
inputIndex2 = 0
############################################################################

environment.set('musicxmlPath', '/bin/musescore3' )

ND_model = NeuralNetwork.NeuralNetwork()
ND_model.load_model(ND_modelFilepath)
starterInput, temp = starter.getTrainData(ND_sequenceLength)
ND_input = starterInput[inputIndex]
ND_inputShape = (1, ND_sequenceLength, 450)

NP_model = NeuralNetwork.NeuralNetwork()
NP_model.load_model(NP_modelFilepath)
starterInput, temp = starter.getTrainData(NP_sequenceLength)
NP_input = starterInput[inputIndex2]
NP_inputShape = (1, NP_sequenceLength, 450)

melody = []
for noteIndex in range(newMelodyLength):
    duration = ND_model.pod_generation(ND_input, ND_inputShape)
    pitch = NP_model.pod_generation(NP_input, NP_inputShape)
    melody.append(Note.Note(list(pitch), list(duration)))
    ND_input = updateNoteInput(ND_input, melody[-1])
    NP_input = updateNoteInput(NP_input, melody[-1])

MusicConverter.convert(melody, MUSIC_STREAM).show('musicxml')
compareNewMelody(melody)

