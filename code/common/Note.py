## @file Note.py

## @class Note
class Note:
    def __init__(self):
        self.pitchVec = None
        self.durationVec = None

    def __init__(self, pitchVec, durationVec):
        self.pitchVec = pitchVec
        self.durationVec = durationVec