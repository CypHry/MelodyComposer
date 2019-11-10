## @file MusicConverter.py

from music21 import *
from common import Note

NOTES_VECTOR = "notes vector"
MUSIC_STREAM = "music stream"
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
        return music

    @staticmethod
    def _changeM21NoteToNote(M21Note):
        pitchVector = [0]*45
        durationVector = [0]*80
        durationVector[int(M21Note.duration.quarterLength*20)] = 1
        if M21Note.isClassOrSubclass((note.Note,)):
            pitchVector[int(interval.Interval(note.Note('c3'), M21Note).cents / 100)] = 1

        return Note.Note(pitchVector, durationVector)

