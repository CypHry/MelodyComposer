## @file Note.py

import numpy as np

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

    def __eq__(self, other):
        return self.pitchVector == other.pitchVector and self.durationVector == other.durationVector

    def getOneHot(self):
        oneHot = [0]*450
        if self.pitchVector.count(1) == 1:
            oneHot[10*self.pitchVector.index(1)+self.durationVector.index(1)] = 1
        else:
            oneHot[self.durationVector.index(1)] = 1;

        return oneHot

    def setOneHot(self, vector):
        index = vector.index(1)
        self.pitchVector = [0] * 45
        self.durationVector = [0] * 10
        self.pitchVector[int(np.int_(index)/10)] = 1
        self.durationVector[int(np.int_(index)%10)] = 1

    def setFromIndex(self, index):
        self.pitchVector = [0] * 45
        self.durationVector = [0] * 10
        self.pitchVector[int(np.int_(index)/10)] = 1
        self.durationVector[int(np.int_(index)%10)] = 1

