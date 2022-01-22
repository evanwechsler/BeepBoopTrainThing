import utility

def main():
    arrivals = utility.csvToPassengerArrivals()
    print(arrivals.getArrivals("7:00", "A"))

if __name__ == "__main__":
    main()