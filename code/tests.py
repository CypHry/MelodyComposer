from common import Tune, Note

tune = Tune.Tune("/home/cyprian/Documents/ABC/China/Bu_guo")
for note in tune.notesVector:
    print(note.durationVec)
    print(note.pitchVec)