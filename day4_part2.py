
# get data
inputdata = []

inputfile = "/Users/dyl13740/Documents/AdventofCode2023/day4_input.txt"
with open(inputfile, 'r') as file: 
    lines = file.readlines()

    for line in lines: 
        inputdata.append(line.strip('\n'))

sumtotal = 0

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


# how many total scratch cards. 

# for number of matches add a second run of that many cards
# make card dictionary, add to number of cards as needed. 

cardcounts = {}

for line in inputdata:
    matches = 0

    splitline = line.split(colon)
    
    gamenumber = splitline[0].split()[1]
    
    mynumbers = splitline[1].split(pipe)[0] 
    winningnumbers = splitline[1].split(pipe)[1]

    mynumberarray = createintarray(mynumbers)
    winningnumbersarray = createintarray(winningnumbers)

    for n in mynumberarray: 
        if n in winningnumbersarray: 
            matches += 1

    cardcounts[int(gamenumber)] = matches


# -----------------------
listofnewcardcounts = {}

for k in cardcounts.keys():
    listofnewcardcounts[k] = 1

for k in cardcounts.keys(): 
    v = cardcounts[k]


for c in cardcounts.keys(): 
    r = range(1, cardcounts[c] + 1)

    #if cardcounts[c] > 0: 
    #    listofnewcardcounts[c] += 1

    for i in r:
        listofnewcardcounts[c + i] += listofnewcardcounts[c]

    

# for number of matches 
# add 1 to next number for number of matches
# 

print(listofnewcardcounts)

for n in listofnewcardcounts.values(): 
    sumtotal += n

print(sumtotal) # part 2 9924412
