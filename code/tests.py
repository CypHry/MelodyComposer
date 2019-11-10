from common import Tune, Note
from MusicConverter import *

tune = Tune.Tune("/home/cyprian/Documents/ABC/China/Bu_guo")
tune.notesStream.show('text')
print('')
MusicConverter.convert(tune.notesVector, MUSIC_STREAM).show('text')

