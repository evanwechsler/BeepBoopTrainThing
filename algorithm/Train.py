from typing import List
from station import Station

class Train:
    stations = ["A", "B", "C", "U"]
    maxCapacity = 0

    def __init__(self, station=None, moving=False, dwelling=False, capacity=0) -> None:
        if station not in self.stations and station != None:
            raise Exception(f"Station must be one of {self.stations}")
        self.station = station
        self.moving = moving
        self.dwelling = dwelling
        self.passengers = []
        self.numPassengers = 0
        self.maxCapacity = capacity
        self.arrivalTimes = []

    # Tries to add as many passengers to the car as possible
    # Returns the number of remaining passengers
    def pickUpPassengers(self, station: Station):
        if self.isFull():
            return
        numNewPassengers = station.numPassengers
        if self.numPassengers + numNewPassengers > self.maxCapacity:
            availableSeats = self.maxCapacity - self.numPassengers
            self.numPassengers = self.maxCapacity
            self.passengers += station.boardPassengers(availableSeats)
        else:
            self.numPassengers += numNewPassengers
            self.passengers += station.boardPassengers(numNewPassengers)

    def isFull(self):
        return self.numPassengers == self.maxCapacity





class L4(Train):
    def __init__(self, station=None, moving=False, dwelling=False) -> None:
        super().__init__(station, moving, dwelling, 400)


class L8(Train):
    def __init__(self, station=None, moving=False, dwelling=False) -> None:
        super().__init__(station, moving, dwelling, 800)


def main():
    l4 = L4()
    l8 = L8()
    station = Station()
    station.addPassengers(850)
    l8.pickUpPassengers(station)

    print(l8.numPassengers)
    print(station.numPassengers)


if __name__ == "__main__":
    main()
