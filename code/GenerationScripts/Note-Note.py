from network import NeuralNetwork
from music21 import environment
from common import Tune
from utils import compareNewMelody, updateNoteInput, updatePoDInput
from MusicConverter import MusicConverter, MUSIC_STREAM

############################################################################

modelFilepath = "../weights/82_note-note_sequence40_epoch100_LLBLLDD_WD"
sequenceLength = 40

newMelodyLength = 50
starter = Tune.Tune("../ABC/ABCChina06")

inputIndex = 0
############################################################################

environment.set('musicxmlPath', '/bin/musescore3' )

model = NeuralNetwork.NeuralNetwork()
model.load_model(modelFilepath)
starterInput, temp = starter.getTrainData(sequenceLength)
input = starterInput[inputIndex]
inputShape = (1, sequenceLength, len(input[0]))

melody = []
for noteIndex in range(newMelodyLength):
    melody.append(model.note_generation(input, inputShape))
    input = updateNoteInput(input, melody[-1])

MusicConverter.convert(melody, MUSIC_STREAM).show('musicxml')
compareNewMelody(melody)

