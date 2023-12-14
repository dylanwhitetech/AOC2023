# find numbers that are diagonal 

# 467..114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598..

# axample total - 4361

# readline
# store numbers and their starting and ending index? 
# dictionary, number is value, indexes are list of start to end
# if symbol? 
# symbal is NOT "." or number

# every number is only counted once

# get data
inputdata = []

inputfile = "/Users/dyl13740/Documents/AdventofCode2023/day3inputexample.txt"
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

def indexfornumber(inputarray):
    first = inputarray[0]
    last = inputarray[len(inputarray) - 1]
    array = []
    array.append(first)
    array.append(last)
    return array


# get numbers and symbols their indexes
def readlineintodictionary(inputstring, numbers, dot):
    numberdict = {}
    symboldict = {}

    tracknumber = []
    trackindex = []

    countsymbol = 0

    for i, c in enumerate(inputstring): 
        if c in numbers.values():
            tracknumber.append(c)
            trackindex.append(i)

        if c not in numbers.values() and c != dot: # symbol
            tracknumber.clear()
            trackindex.clear()
            
            if c in symboldict.keys():
                countsymbol += 1
                c += '-' + str(countsymbol)

                symboldict[c] = i
            else: 
                symboldict[c] = i

        if c == dot and len(tracknumber) > 0:
            # add current number to dictionary
            newnumber = ''.join(tracknumber)
            newrange = indexfornumber(trackindex)

            if newnumber not in numberdict.keys():
                numberdict[newnumber] = newrange
                
            tracknumber.clear()
            trackindex.clear()

    # return numbers with indexes and symbols with index
    return numberdict, symboldict


# current line test
def linetest(numberdictionary, symboldictionary): 
    
    total = 0

    numberstested = [] # part numbers to add to total.

    if len(symboldictionary) > 0: 
        for n in numberdictionary.keys():
            # get range from number dict. 
                
            #firstindex
            firstnumberinrange = numberdictionary[n][0]
            
            if firstnumberinrange > 0: 
                firstnumberinrange -= 1
            
            # last index
            lastnumberinrange = numberdictionary[n][len(numberdictionary[n]) - 1]
            lastnumberinrange += 1
        
            for k in symboldictionary.keys():
                if firstnumberinrange <= symboldictionary[k] <= lastnumberinrange:
                    
                    # IF numbers are duplicates
                    if dash in n:
                        formattednumber = n.split(dash, 1)[0] # take everything before the -

                        if formattednumber not in numberstested:
                            numberstested.append(int(formattednumber))

                    else: 
                        if n not in numberstested:
                            numberstested.append(int(n))
    
    return numberstested



# store all part numbers
partnumbers = []

# test first line against itself
firstlinenumberdict, firstlinesymboldict = readlineintodictionary(inputdata[0], numbersfromwords, period)
firstlinenumbertoadd = linetest(firstlinenumberdict, firstlinesymboldict)

# test first line against second line. 
secondlinenumberdict, secondlinesymboldict = readlineintodictionary(inputdata[1], numbersfromwords, period)
secondlinenumbertoadd = linetest(firstlinenumberdict, secondlinesymboldict)

for p in firstlinenumbertoadd: 
        if p not in partnumbers: 
            partnumbers.append(p)

for p in secondlinenumbertoadd: 
    if p not in partnumbers: 
            partnumbers.append(p)


# start reading all lines.
for i in range(1, len(inputdata)): 
    # previous line 
    previouslinenumberdict, previouslinesymboldict = readlineintodictionary(inputdata[i - 1], numbersfromwords, period)

    # current line in numbers and symbol index dictionary
    currentnumberdict, currentsymboldict = readlineintodictionary(inputdata[i], numbersfromwords, period)
    

    # current line numbers vs current line symbols
    currentline = linetest(currentnumberdict, currentsymboldict)
        
    # current line numbers vs previous line symbols 
    currentlinevsprevioussymbol = linetest(currentnumberdict, previouslinesymboldict)

    # current line symbols vs previous line. 
    previouslinecurrentsymbol = linetest(previouslinenumberdict, currentsymboldict)

    # check against existing part numbers
    for p in currentline: 
        partnumbers.append(p)
    for p in currentlinevsprevioussymbol:
        partnumbers.append(p)
    for p in previouslinecurrentsymbol:
        partnumbers.append(p)

    print(inputdata[i-1])
    print(inputdata[i])
    print(currentline)
    print(currentlinevsprevioussymbol)
    print(previouslinecurrentsymbol)
    print()
    print(partnumbers)

    
for part in partnumbers: 
        sumtotal += part

print(sumtotal) #538046

