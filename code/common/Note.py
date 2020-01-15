## @file Note.py
PITCH_VEC_SIZE = 45
DURATION_VEC_SIZE = 80

## @class Note
class Note:
    def __init__(self):
        self.pitchVector = None
        self.durationVector = None

    def __init__(self, pitchVec, durationVec):
        self.pitchVector = pitchVec
        self.durationVector = durationVec

    def getOneHot(self):
        oneHot = [0]*450
        if self.pitchVector.count(1) == 1:
            oneHot[10*self.pitchVector.index(1)+self.durationVector.index(1)] = 1
        else:
            oneHot[self.durationVector.index(1)] = 1;

        return oneHot

    def setOneHot(self, vector):
        index = vector.index(1)
        self.pitchVector = index/10
        self.durationVector = index%10

