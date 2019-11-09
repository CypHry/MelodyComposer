## @file MusicConverter.py

from music21 import *
from common import Note

NOTES_VECTOR = "notes vector"
MUSIC_STREAM = "music stream"
# TODO: add more notations

class MusicConverter:
    @staticmethod
    def convert(music, fromNotation, toNotation):
        if toNotation == NOTES_VECTOR and fromNotation == MUSIC_STREAM:
            return _convertMusicStreamToNotesVector(music)
        elif toNotation == MUSIC_STREAM and fromNotation == NOTES_VECTOR:
            return _convertNotesVectorToMusicStream(music)
        return music

    @staticmethod
    def _convertMusicStreamToNotesVector(music):
        notesVector = []
        for element in music.elements:
            if element.isClassOrSubclass((note.Note, note.Rest)):
                notesVector.append(_changeM21NoteToNote(element))
        return notesVector

    @staticmethod
    def _convertNotesVectorToMusicStream(music):
        return music

    @staticmethod
    def _changeM21NoteToNote(M21Note):
        pitchVector = [0]*48
        durationVector = [0]*32
        #if M21Note.isClassOrSubclass((note.Note,)):
            # pitchVector[] # add interval here

        return Note(pitchVector, durationVector)

