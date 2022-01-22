from Train import L4, L8
from utlility import getDist


passengerDist = getDist()
maxCapacity = 50
dwellTime = 3 * 60
AtoB = 8 * 60
BtoC = 9 * 60
CtoU = 11 * 60

l4s = [L4() for i in range(4)]
l8s = [L8() for i in range(8)]

curTime = 7 * 60 * 60
