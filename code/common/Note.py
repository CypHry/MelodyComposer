## @file Note.py

## @class Note
class Note:
    def __init__(self):
        self.pitchVector = None
        self.durationVector = None

    def __init__(self, pitchVec, durationVec):
        self.pitchVector = pitchVec
        self.durationVector = durationVec