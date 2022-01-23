class Passenger:
    def __init__(self, arrivalTime) -> None:
        self.waitTime = 0
        self.arrivalTime = arrivalTime

    def incrTime(self, timeToAdd):
        self.waitTime += timeToAdd