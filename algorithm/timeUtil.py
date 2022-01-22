from math import floor


def secondsToTime(sec):
    hours = sec // 3600
    minutes = (sec % 3600) // 60
    seconds = (sec % 3600) % 60
    strTime = lambda T: str(T) if len(str(T)) == 2 else f"0{str(T)}"
    return f"{hours}:{strTime(minutes)}:{strTime(seconds)}"


def timeToSeconds(time: str):
    timeList = time.split(":")
    return int(timeList[0]) * 3600 + int(timeList[1]) * 60 + int(timeList[2])


def test():
    seconds = 10 * 60 * 60 + 1000
    timeAsString = secondsToTime(seconds)
    timeAsSeconds = timeToSeconds(timeAsString)
    print(seconds)
    print(timeAsSeconds)
    print(timeAsString)
    print(seconds == timeAsSeconds)


if __name__ == "__main__":
    test()
