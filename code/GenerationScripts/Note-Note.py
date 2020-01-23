from network import NeuralNetwork
from music21 import environment
from common import Tune
from utils import compareNewMelody, updateNoteInput, updatePoDInput
from MusicConverter import MusicConverter, MUSIC_STREAM

############################################################################

modelFilepath = "weights/note-note"
sequenceLength = 0

newMelodyLength = 0
starter = Tune.Tune("ABC/ABCChina06")

############################################################################

environment.set('musicxmlPath', '/bin/musescore3' )

model = NeuralNetwork.NeuralNetwork()
model.load_model(modelFilepath)
input, temp = starter.getTrainData(sequenceLength)
inputShape = (1, sequenceLength, len(input[0]))

melody = []
for noteIndex in range(newMelodyLength):
    melody.append(model.note_generation(input, inputShape))
    updateNoteInput(input, melody[-1])

MusicConverter.convert(melody, MUSIC_STREAM).show('musicxml')
compareNewMelody(newMelody)

