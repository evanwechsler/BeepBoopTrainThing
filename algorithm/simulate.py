from typing import List, TypedDict

from Train import L4, Station, Train, TrainLine


def initScene():
    stations = [Station() for i in range(3)]
    
    trainLine = TrainLine(stations)


def calcMeanWaitTime(trains: List[Train], passengerDistribution):
    pass
