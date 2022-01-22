from typing import List
from PassengerArrival import PassengerArrivals
from Train import L4, L8, Station, Train
from permute import perm_unique
from utility import csvToPassengerArrivals, getDist
from itertools import permutations


passengerDist = getDist()
maxCapacity = 50
dwellTime = 3 * 60
AtoB = 8 * 60
BtoC = 9 * 60
CtoU = 11 * 60
numL4s = 4
numL8s = 12

stationA = Station()
stationB = Station()
stationC = Station()
stationU = Station()

stations = [stationA, stationB, stationC, stationU]

trains = [4 for i in range(numL4s)] + [8 for i in range(numL8s)]

trainPermutations = list(perm_unique(trains))


def createSimpleSchedule(trains: List[Train]):
    pass


print(len(trainPermutations))
