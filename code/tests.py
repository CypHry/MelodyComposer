from common import Tune

notesStream = stream.Stream()
for element in tune.musicStream.parts[0].elements:
    for noteOrRest in element.elements:
        notesStream.append(noteOrRest)