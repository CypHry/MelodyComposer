from common import Tune
import glob

class TuneLoader:
    def __init__(self, files):
        self.tunes = []
        for filename in glob.glob(files):
            try:
                self.tunes.append(Tune.Tune(filename))
            except:
                print("could not load:", filename)


    def getTrainData(self, sequenceLen):
        inputVector = []
        outputVector = []
        tempInput = []
        tempOutput = []
        for tune in self.tunes:
            try:
                tempInput, tempOutput = tune.getTrainData(sequenceLen)
                inputVector.extend(tempInput)
                outputVector.extend(tempOutput)
            except:
                print("Tune too short.")

        return inputVector, outputVector

    def getTrainData_duration(self, sequenceLen):
        inputVector = []
        outputVector = []
        tempInput = []
        tempOutput = []
        for tune in self.tunes:
            try:
                tempInput, tempOutput = tune.getTrainData_noteDuration(sequenceLen)
                inputVector.extend(tempInput)
                outputVector.extend(tempOutput)
            except:
                print("Tune too short.")

        return inputVector, outputVector

    def getTrainData_pitch(self, sequenceLen):
        inputVector = []
        outputVector = []
        tempInput = []
        tempOutput = []
        for tune in self.tunes:
            try:
                tempInput, tempOutput = tune.getTrainData_notePitch(sequenceLen)
                inputVector.extend(tempInput)
                outputVector.extend(tempOutput)
            except:
                print("Tune too short.")

        return inputVector, outputVector

