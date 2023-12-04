

# get data
inputdata = []

inputfile = "/Users/dyl13740/Documents/AdventofCode2023/day4_input.txt"
with open(inputfile, 'r') as file: 
    lines = file.readlines()

    for line in lines: 
        inputdata.append(line.strip('\n'))

sumtotal = 0

numbersfromwords = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

period = '.'
dash = '-'
colon = ':'
pipe = '|'

def createintarray(listofnumbers): 
    numberarray = []
    array = listofnumbers.strip().split()

    for n in array: 
        number = int(n)
        numberarray.append(number)
    
    return numberarray


# readline
# split out card #: 

# split into two arrays on | 
# read array 1
# read array 2

# for # in array 1 if in array 2
# points *= 2 (points are doubled) first point is 1
# so if points is zero then 1, else 2 

for line in inputdata: 
    points = 0

    splitline = line.split(colon)
    
    gamenumber = splitline[0]
    
    mynumbers = splitline[1].split(pipe)[0] 
    winningnumbers = splitline[1].split(pipe)[1]

    mynumberarray = createintarray(mynumbers)
    winningnumbersarray = createintarray(winningnumbers)

    for n in mynumberarray: 
        if n in winningnumbersarray: 
            if points > 0: 
                points *= 2
            else: 
                points += 1

    sumtotal += points
    print(points)

print(sumtotal) # part 1: 25010