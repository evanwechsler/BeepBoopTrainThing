import matplotlib.pyplot as plt
import pandas as pd
import PassengerArrival


def plotDist(dist: pd.DataFrame):

    dist.plot(x="Arrival Time", y="# Passengers")


def getDist():
    arrivalDist = pd.read_csv("./ArrivalDistributions.csv")
    splitDist = [arrivalDist.loc[arrivalDist["Station"] == i] for i in ["A", "B", "C"]]
    return splitDist

def csvToPassengerArrivals():
    arrivalDist = pd.read_csv("./ArrivalDistributions.csv")
    arrivals = PassengerArrival.PassengerArrivals(arrivalFrame=arrivalDist)
    return arrivals

def main():
    dists = getDist()
    plt.figure()
    for dist in dists:
        plt.plot(
            dist["Arrival Time"], dist["# Passengers"], label=dist["Station"].iloc[0]
        )

    plt.xlabel("Time")
    plt.ylabel("# Passengers")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
