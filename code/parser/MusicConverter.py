## @file MusicConverter.py

from music21 import *
from common import Note

NOTES_VECTOR = "notes vector"
MUSIC_STREAM = "music stream"
QUARTER_LENGTHS = [0.125, 0.25, 0.375, 0.5, 0.75, 1, 1.5, 2, 3, 4]
# TODO: add more notations

class MusicConverter:
    @staticmethod
    def convert(music, toNotation):
        if toNotation == NOTES_VECTOR:
            return MusicConverter._convertMusicStreamToNotesVector(music)
        elif toNotation == MUSIC_STREAM:
            return MusicConverter._convertNotesVectorToMusicStream(music)
        return music

    @staticmethod
    def _convertMusicStreamToNotesVector(music):
        notesVector = []
        for element in music.elements:
            if element.isClassOrSubclass((note.Note, note.Rest)):
                notesVector.append(MusicConverter._changeM21NoteToNote(element))
        return notesVector

    @staticmethod
    def _convertNotesVectorToMusicStream(music):
        musicStream = stream.Stream()
        for note in music:
            musicStream.append(MusicConverter._changeNoteToM21Note(note))

        return musicStream

    @staticmethod
    def _changeM21NoteToNote(M21Note):
        pitchVector = [0]*45
        durationVector = [0]*10
        if int(M21Note.duration.quarterLength) > 4:
            raise Exception("Duration too long")

        minIndex = 0
        minVal = 8
        for i in range(10):
            currentVal = abs(M21Note.duration.quarterLength - QUARTER_LENGTHS[i])
            if currentVal < minVal:
                minVal = currentVal
                minIndex = i

        durationVector[minIndex] = 1

        if M21Note.isClassOrSubclass((note.Note,)):
            interval_ = int(interval.Interval(note.Note('c3'), M21Note).cents / 100)
            if interval_ < 0.0 or interval_ > 44.0:
                raise Exception("Pitch out of scale")
            pitchVector[int(interval_)] = 1

        return Note.Note(pitchVector, durationVector)

    @staticmethod
    def _changeNoteToM21Note(MyNote):
        if MyNote.pitchVector.count(1) == 1:
            pitchIndex = MyNote.pitchVector.index(1)
            durationIndex = MyNote.durationVector.index(1)
            M21Note = note.Note('c3')
            M21Note = M21Note.transpose(pitchIndex)
            M21Note.duration.quarterLength = QUARTER_LENGTHS[durationIndex]
            return M21Note
        else:
            durationIndex = MyNote.durationVector.index(1)
            rest = note.Rest()
            rest.duration.quarterLength = QUARTER_LENGTHS[durationIndex]
            return rest



