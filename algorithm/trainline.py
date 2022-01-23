from Train import *
from utility import csvToPassengerArrivals, convertMinsToTime

class TrainLine:
    def __init__(self) -> None:
        # Time 420 is 7am
        self.curTime = 0
        self.stations = [Station(i) for i in ["A", "B", "C"]]
        self.trains = [L4() for i in range(4)] + [L8() for i in range(8)]
        self.arrivalTimes = csvToPassengerArrivals()
        self.goldenRatio = self.arrivalTimes.totalPassengers / sum([train.maxCapacity for train in self.trains])

    def GetNumPassengersWaiting(self, station):
        assert self.curTime >= 0 and self.curTime <= 180
        numPassengers = 0
        for i in range(0, self.curTime + 1, 10):
            time = convertMinsToTime(i)
            numPassengers += int(self.arrivalTimes.getArrivals(time, station))
        return numPassengers
    
    def calcPotentialPassengerCount(self):
        potential_passengers = 0
        simulated_time = self.curTime
        simulated_time += 3
        #potential_passengers += 
        
    



def simulate():
    line = TrainLine()
    line.curTime = 10
    print(line.GetNumPassengersWaiting("A"))



if __name__ == "__main__":
    simulate()