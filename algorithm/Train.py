from typing import List
from utlility import getDist
from random import randint


class Car:
    maxCapacity = 50

    def __init__(self, numPassengers=0) -> None:
        if numPassengers > self.maxCapacity:
            raise Exception(f"Number of passengers has exceeded {self.maxCapacity}")
        else:
            self.numPassengers = numPassengers

    # Tries to add as many passengers to the car as possible
    # Returns the number of remaining passengers
    def addPassengers(self, newPassengers=1):
        if self.isFull():
            return newPassengers
        if self.numPassengers + newPassengers > self.maxCapacity:
            remaining = newPassengers - (self.maxCapacity - self.numPassengers)
            self.numPassengers = self.maxCapacity
            return remaining
        else:
            self.numPassengers += newPassengers
            return 0

    def isFull(self):
        return self.numPassengers == self.maxCapacity


class Train:
    stations = ["A", "B", "C", "U"]

    def __init__(self, station=None, moving=False, dwelling=False, numCars=0) -> None:
        if station not in self.stations:
            raise Exception(f"Station must be one of {self.stations}")
        self.station = station
        self.moving = moving
        self.dwelling = dwelling
        self.numCars = numCars
        self.cars: List[Car] = []
        self.numPassengers = 0
        self.maxCapacity = numCars * Car.maxCapacity

    def isFull(self):
        return self.numPassengers == self.maxCapacity

    # Tries to add passengers to train.
    # Fills up cars in order
    # Returns the number of overflow passengers
    def addPassengers(self, newPassengers):
        if self.isFull():
            return newPassengers
        else:
            for car in self.cars:
                remaining = car.addPassengers(newPassengers)
                if remaining == 0:
                    self.numPassengers += newPassengers
                    return 0
                else:
                    self.numPassengers += newPassengers - remaining
                    newPassengers = remaining

            return newPassengers


class L4(Train):
    def __init__(self, station=None, moving=False, dwelling=False) -> None:
        super().__init__(station, moving, dwelling, 4)
        self.cars = [Car() for i in range(4)]


class L8(Train):
    def __init__(self, station=None, moving=False, dwelling=False) -> None:
        super().__init__(station, moving, dwelling, 8)
        self.cars = [Car() for i in range(8)]


def main():
    l4 = L4()
    l8 = L8()

    remaining = l4.addPassengers(143)
    for car in l4.cars:
        print(car.numPassengers)


if __name__ == "__main__":
    main()
