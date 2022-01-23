from typing import List
from PassengerArrival import PassengerArrivals
from Train import L4, L8, Station, Train
from permute import perm_unique
from timeUtil import secondsToTime
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

travelTimes = [0, dwellTime + AtoB, dwellTime + BtoC, dwellTime + CtoU]

stationA = Station()
stationB = Station()
stationC = Station()
stationU = Station()

stations = [stationA, stationB, stationC, stationU]

trains = [4 for i in range(numL4s)] + [8 for i in range(numL8s)]

trainPermutations = list(perm_unique(trains))

trains = [L4() for i in range(numL4s)] + [L8() for i in range(numL8s)]


def createSimpleSchedule(trains: List[Train]):
    # 7:00
    curTime = 7 * 3600

    def cumulative(lists):
        cu_list = []
        length = len(lists)
        cu_list = [sum(lists[0:x:1]) for x in range(0, length + 1)]
        return cu_list[1:]

    for train in trains:
        arrivalTimes = [secondsToTime(curTime + i) for i in cumulative(travelTimes)]
        train.arrivalTimes = arrivalTimes
        curTime += 10 * 60
        print(train.arrivalTimes)


# print(len(trainPermutations))
createSimpleSchedule(trains)
