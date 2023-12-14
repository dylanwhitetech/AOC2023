
# There's really only one race - ignore the spaces between the numbers on each line.



# So, the example from before:
# 
# Time:      7  15   30
# Distance:  9  40  200
# ...now instead means this:
# 
# Time:      71530
# Distance:  940200


# get data
inputdata = []

inputfile = "/Users/dyl13740/Documents/AdventofCode2023/day6_input.txt"
with open(inputfile, 'r') as file: 
    lines = file.readlines()

    for line in lines: 
        inputdata.append(line.strip('\n'))

colon = ':'

# get race time / number 
racedata = {} # everything stored as int

splittime = inputdata[0].split(colon)
splitdistance = inputdata[1].split(colon)

times = splittime[1].strip().split()
distances = splitdistance[1].strip().split()

combinedtimes = ''
combindeddistances = ''

for t in times: 
    combinedtimes += t

for d in distances: 
    combindeddistances += d

print(combinedtimes)
print(combindeddistances)



numberofwins = 0

recorddistance = int(combindeddistances)
totalracetime = int(combinedtimes)

for buttonpresstime in range(totalracetime - 1, 0, -1):
    timetomove = totalracetime - buttonpresstime
    distancedtraveled = buttonpresstime * timetomove

    if distancedtraveled > recorddistance:
        numberofwins += 1


print(numberofwins) # 20537782