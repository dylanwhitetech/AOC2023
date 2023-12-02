# what is the sum of the game IDs 

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


# get game number
# if valid game then add to sumtotal

# split line on ;
# parse splits into value and color ? 
# loop through number dict to make number of cubes
# loop through color dict to find color
# if value < color count then valid game / go to next color to parse

for line in cleaneddatta: 
    game, colors = map(str.strip,line.split(':', 1)) # splits the line on :. limiting the split to only one occurance, list with 2 elements

    gamenumber = getnumber(game, numbersfromwords)

    isvalidgame = iscolorcountvalid(colors, cubecounts, numbersfromwords)

    if isvalidgame == True:
        sumtotal += gamenumber

print(sumtotal) # 2162

