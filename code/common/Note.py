## @file Note.py

NOTE_A_PITCH_VEC = [1, 0, 0, 0, 0, 0, 0, 0] ## pitch A representation in every octave
NOTE_B_PITCH_VEC = [0, 1, 0, 0, 0, 0, 0, 0] ## pitch B representation in every octave
NOTE_C_PITCH_VEC = [0, 0, 1, 0, 0, 0, 0, 0] ## pitch C representation in every octave
NOTE_D_PITCH_VEC = [0, 0, 0, 1, 0, 0, 0, 0] ## pitch D representation in every octave
NOTE_E_PITCH_VEC = [0, 0, 0, 0, 1, 0, 0, 0] ## pitch E representation in every octave
NOTE_F_PITCH_VEC = [0, 0, 0, 0, 0, 1, 0, 0] ## pitch F representation in every octave
NOTE_G_PITCH_VEC = [0, 0, 0, 0, 0, 0, 1, 0] ## pitch G representation in every octave
NOTE_REST_VEC    = [0, 0, 0, 0, 0, 0, 0, 1] ## rest representation

NOTE_BASE8_DURATION  = [1, 0, 0, 0, 0, 0, 0, 0, 0] ## 4 times base duration
NOTE_BASE6_DURATION  = [0, 1, 0, 0, 0, 0, 0, 0, 0] ## 4 times base duration
NOTE_BASE4_DURATION  = [0, 0, 1, 0, 0, 0, 0, 0, 0] ## 4 times base duration
NOTE_BASE3_DURATION  = [0, 0, 0, 1, 0, 0, 0, 0, 0] ## 3 times base duration
NOTE_BASE2_DURATION  = [0, 0, 0, 0, 1, 0, 0, 0, 0] ## 2 times base duration
NOTE_BASE_DURATION   = [0, 0, 0, 0, 0, 1, 0, 0, 0] ## equal to the base duration
NOTE_BASE_2_DURATION = [0, 0, 0, 0, 0, 0, 1, 0, 0] ## base duration / 2
NOTE_BASE_4_DURATION = [0, 0, 0, 0, 0, 0, 0, 1, 0] ## base duration / 4
NOTE_BASE_8_DURATION = [0, 0, 0, 0, 0, 0, 0, 0, 1] ## base duration / 8

class NoteConverter:
    @staticmethod
    def convert(abcString):
        return None, None

## @class Note
class Note:
    def __init__(self):
        self.abcString = None
        self.pitchVec = None
        self.durationVec = None

    def __init__(self, noteAbcString):
        self.abcString = noteAbcString
        self.pitchVec, self.durationVec = NoteConverter.convert(noteAbcString)