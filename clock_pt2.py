import math

def dist(centerx, centery, x, y):
    return math.sqrt((float(x) - centerx) ** 2 + (float(y) - centery) ** 2)

def maxIndex(arr):
    index = 0
    for i in range(1, len(arr)):
        if(arr[i] > arr[index]):
            index = i
    return index
    
def compute_time(center_x, center_y, x1, y1, x2, y2, x3, y3):
    
    # Calculate angles in radians
    hour_angle = math.atan2(center_y - y2, center_x - x2)
    minute_angle = math.atan2(center_y - y3, center_x - x3)
    second_angle = math.atan2(center_y - y1, center_x - x1)

    # Convert angles to degrees
    hour_angle = math.degrees(hour_angle) - 90
    minute_angle = math.degrees(minute_angle) - 90
    second_angle = math.degrees(second_angle) - 90

    # Calculate hours, minutes, and seconds
    hours = ((hour_angle / 30) + 12) % 12
    minutes = (minute_angle / 6) % 60
    seconds = (second_angle / 6)  % 60

    return f"{int(hours):02d}:{int(minutes):02d}:{int(seconds):02d}"

def main():
    #   #   #  Make variables needed
    inp = list(map(str, input().split(' ')))
    trimedInp = list()
    coordinates = list()
    #   #   #

    #   #   # Trim input and add to trimedInp
    for i in range(len(inp) - 1):
        if inp[i] != '':
            inp[i] = inp[i][:-1]
            trimedInp.append(inp[i])
    trimedInp.append(inp[-1])
    #   #   #

    #   #   # Add trimedInp to coordinates as arrays. Easier to access and manipulate in loops
    for i in range(0, len(trimedInp) - 1,2):
        coordinates.append([float(trimedInp[i]), float(trimedInp[i+1])])
    #   #   #


    center = coordinates[0] # Create center variable and delete it from coordinates array
    del coordinates[0]


    distArr = [dist(center[0], center[1], coordinates[i][0], coordinates[i][1]) for i in range(3)]

    #   #   #   Separating the coordinates into their own variables relative to their distance from the center(Tells which hand is which)
    x3, y3 = coordinates[maxIndex(distArr)][0], coordinates[maxIndex(distArr)][1]
    del coordinates[maxIndex(distArr)]
    del distArr[maxIndex(distArr)]
    x1, y1 = coordinates[maxIndex(distArr)][0], coordinates[maxIndex(distArr)][1]
    del coordinates[maxIndex(distArr)]
    del distArr[maxIndex(distArr)]
    x2, y2 = coordinates[0][0], coordinates[0][1]
    del coordinates[0]
    del distArr[maxIndex(distArr)]
    #   #   #

    print(compute_time(center[0], center[1], x1, y1, x2, y2, x3, y3))

main()
