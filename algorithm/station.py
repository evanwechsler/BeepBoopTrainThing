from Train import *
from Passenger import Passenger
class Station:
    def __init__(self, stationId) -> None:
        self.passengers: List[Passenger] = []
        self.numPassengers = 0
        self.stationID = stationId

    def addPassengers(self, currTime, numPassengers: int):
        self.passengers += [Passenger(currTime) for i in range(numPassengers)]
        self.numPassengers += numPassengers

    def boardPassengers(self, numPassengers: int):
        boardingPassengers = self.passengers[:numPassengers]
        self.passengers = self.passengers[numPassengers:]
        self.numPassengers -= numPassengers
        return boardingPassengers