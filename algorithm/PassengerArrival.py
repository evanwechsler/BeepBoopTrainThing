import pandas as pd

class PassengerArrivals:
    def __init__(self, arrivalFrame):
        self.trainDict = {}
        totalPassengers = 0
        for i in ["A", "B", "C"]: self.trainDict[i] = {}
        for index, row in arrivalFrame.iterrows():
                letter_dict = self.trainDict[row[0]]
                letter_dict[row[1]] = row[2]
                totalPassengers += row[2]
        self.totalPassengers = totalPassengers
    
    def getArrivals(self, time, station):
        return self.trainDict[station][time]