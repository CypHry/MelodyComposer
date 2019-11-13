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

    def getIntValue(self):
        if(self.pitchVector.count(1)):
            return 100*self.pitchVector.index(1)+self.durationVector.index(1)
        return self.durationVector.index(1)

    def setIntValue(self, value):
        self.pitchVector = [0]*45
        self.durationVector = [0]*80
        self.pitchVector[int(value/100)] = 1
        self.durationVector[int(value % 100)] = 1

    def getOneHot(self):
        oneHot = [0]*4580
        oneHot[self.getIntValue()] = 1
        return oneHot

    def setOneHot(self, vector):
        self.setIntValue(vector.index(1))