# when looking at color counts. store largest number of cubes found in new dictionary. 
# the largest count is the minimum value for the color. 

# all games are valid.

# take max counts for each color and multiply them
# Game 1: 4 x 2 x 6 = 48
# 48 is the power of the cubes. 

# sum the power of the cubes
sumtotal = 0 

cubecounts = {
    'red': 12,
    'green': 13,
    'blue': 14
}

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



inputfile = open("/Users/dyl13740/Documents/AdventofCode2023/day2input.txt")
inputdata = inputfile.readlines()

cleaneddatta = []
for line in inputdata:
    cleaneddatta.append(line.strip('\n'))


# functions
def getnumber(inputstring, numbersdict): 
    tempnumbers = []
    
    listfromstring = []
    listfromstring.extend(inputstring)
    
    for c in listfromstring:
        if c in numbersdict.values():
            tempnumbers.append(c)
    
    number = int(f"{''.join(tempnumbers)}")

    return number

def getcolor(inputstring, colordict):
    index = 0

    for k in colordict.keys():
        index = inputstring.find(k)
        if index != -1:
            return k # return the color.



def iscolorcountvalid(inputstring, colordict, numbers):
    gameisvalid = True
    
    handfuls = inputstring.split(';') # 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green

    for h in handfuls:
        colorandcount = h.split(',') # 3 blue, 4 red

        for c in colorandcount: 
            number = getnumber(c,numbers)
            color = getcolor(c, colordict) # identify the color
            
            # if count is valid return true
            if number > colordict[color]:
                
                gameisvalid = False
                return gameisvalid
    
    # if no false values found. then its valid game.
    return gameisvalid


def minimumcountpercolor(inputstring, colordict, numbers): 
    mincolorcount = {} # storage dict

    handfuls = inputstring.split(';') # 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green

    for h in handfuls:
        colorandcount = h.split(',') # 3 blue, 4 red

        for c in colorandcount: 
            number = getnumber(c,numbers)
            color = getcolor(c, colordict) # identify the color

            # check dict. 
            if color in mincolorcount.keys(): 
                if number > mincolorcount[color]: 
                    mincolorcount[color] = number
            else:
                mincolorcount[color] = number

    return mincolorcount


for line in cleaneddatta: 
    game, colors = map(str.strip,line.split(':', 1)) # splits the line on :. limiting the split to only one occurance, list with 2 elements

    # game is not used we can ignore

    minimumcolorcounts = minimumcountpercolor(colors, cubecounts, numbersfromwords) # dictionary

    powerofcubes = 0

    for k in minimumcolorcounts.keys(): 
        number = int(minimumcolorcounts[k])

        if powerofcubes > 0: 
            powerofcubes *= number
        else: 
            powerofcubes += number
    
    sumtotal += powerofcubes

# sumtotal
print(sumtotal) #72513