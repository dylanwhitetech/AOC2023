# get data
inputdata = []

inputfile = "/Users/dyl13740/Documents/AdventofCode2023/day6_input.txt"
with open(inputfile, 'r') as file: 
    lines = file.readlines()

    for line in lines: 
        inputdata.append(line.strip('\n'))

colon = ':'


# Time:      7  15   30
# Distance:  9  40  200

# start speed 
# zero millimeters per milliseconds 

# per millisecond
# button press increases speed by 1 millimeter per millisecond


# total race time is split into 2 parts 
    # button hold time
    # travel time

# race 1, 4 ways to win
# race 2, 8 ways to win
# race 3, 9 ways t0 win

# answer = 4 * 8 * 9

# get race time / number 
racedata = {} # everything stored as int

splittime = inputdata[0].split(colon)
splitdistance = inputdata[1].split(colon)

times = splittime[1].strip().split()
distances = splitdistance[1].strip().split()

for n in range(0, len(times)): 
    racedata[times[int(n)]] = distances[int(n)]

print(times)
print(distances)


def calculatenumberofwins(datadictionary): 
    # can hold button for all numbers from 0 to time - 1
    # distance is record. 
    # check for how many times boat travels past record
    # track number of button hold times 

    # distanced traveled = buttonpresstime * timeleftinrace

    # total number of wins
    totalwaystowin = 1

    for time in datadictionary:
        numberofwins = 0

        recorddistance = int(datadictionary[time])
        totalracetime = int(time)

        for buttonpresstime in range(totalracetime - 1, 0, -1):
            timetomove = totalracetime - buttonpresstime
            distancedtraveled = buttonpresstime * timetomove

            if distancedtraveled > recorddistance:
                numberofwins += 1

        totalwaystowin *= numberofwins

    return totalwaystowin


waystowin = calculatenumberofwins(racedata)
print(waystowin) #170000