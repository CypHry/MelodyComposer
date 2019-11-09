## @file ABCKeyTransposer

from music21 import *

class ABCKeyTransposer:
    @staticmethod
    def transposeToC(musicStream, fromKey):
        if fromKey.getScale().isClassOrSubclass((scale.MajorScale,)):
            interval_ = interval.Interval(fromKey.getScale().pitchFromDegree(1), scale.MajorScale('c').pitchFromDegree(1))
        else:
            interval_ = interval.Interval(fromKey.getScale().pitchFromDegree(1), scale.MinorScale('a').pitchFromDegree(1))

        return musicStream.transpose(interval_)
