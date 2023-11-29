import math

class hand:
    length = None
    x1 = 0
    y1 = 0
    x2 = 0
    y2 = 0
    def __init__(self, centerx, centery, x, y, divisions):
        self.x1 = centerx
        self.y1 = centery
        self.x2 = x
        self.y2 = y
        self.length = math.sqrt((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2)
        self.divisions = divisions
    def findTime(self):
        pass
        # self.time = # Need to finish this tomorrow
        # return self.time

class coordinate:
    x = 0
    y = 0
    def __init__(self, x, y):
        self.x = x
        self.y = y


def dist(centerx, centery, x, y):
    return math.sqrt((x - centerx) ** 2 + (y - centery) ** 2)


inp = list(map(str, input().split(' ')))
trimedinp = []
coordinates = {}
distArray = []


#   #    # Trimming
for i in inp:
    if i != '':
        trimedinp.append(i)

for i in range(len(trimedinp)-1):
    trimedinp[i] = trimedinp[i][:-1]
#   #   #


trimedinp = list(map(float, trimedinp))
print(trimedinp)

#   #   # Finds and sets the correct coordinates to the correct hands
center = [trimedinp[0], trimedinp[1]]
for i in range(2, len(trimedinp), 2):
    coordinates[dist(center[0], center[1], trimedinp[i], trimedinp[i + 1])] = coordinate(trimedinp[i], trimedinp[i+1])
    distArray.append(dist(center[0], center[1], trimedinp[i], trimedinp[i + 1]))
distArray.sort()
print(distArray)

minHand = hand(center[0], center[1], coordinates[distArray[2]].x, coordinates[distArray[2]].y, 60)
secHand = hand(center[0], center[1], coordinates[distArray[1]].x, coordinates[distArray[1]].y, 60)
hourHand = hand(center[0], center[1], coordinates[distArray[0]].x, coordinates[distArray[0]].y, 12)
#   #   #
# hour = hourHand.findTime()
# Min = minHand.findTime()
# sec = secHand.findTime()

hour = distArray[0]
sec = distArray[1]
Min = distArray[2]

print(hour,sec,  Min)