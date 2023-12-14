# get data
inputdata = []

inputfile = "/Users/dyl13740/Documents/AdventofCode2023/day3input.txt"
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



def readlineintodictionary(inputstring, numbers, dot):
    numberdict = {}
    symboldict = {}

    tracknumber = []
    trackindex = []

    countsymbol = 0
    countnumber = 0

    for i, c in enumerate(inputstring): 
        
        # start storing numbers
        if c in numbers.values(): 
            tracknumber.append(c)
            trackindex.append(i)

        # hit end of number
        if c not in numbers.values(): 
            if c == dot: 
                # end number counting and make number
                if len(tracknumber) > 0: 
                    newnumber = ''.join(tracknumber)
                    newrange = indexfornumber(trackindex)

                    if newnumber in numberdict.keys(): # takes care of duplicate numbers (need to strip this later)
                        countnumber += 1
                        newnumber += dash + str(countnumber)

                        numberdict[newnumber] = newrange

                        tracknumber.clear()
                        trackindex.clear()
                    else: 
                        numberdict[newnumber] = newrange

                        tracknumber.clear()
                        trackindex.clear()
                    
            else: # its a symbol then 
                if len(tracknumber) > 0: 
                    newnumber = ''.join(tracknumber)
                    newrange = indexfornumber(trackindex)

                    if newnumber in numberdict.keys(): # takes care of duplicate numbers (need to strip this later)
                        countnumber += 1
                        newnumber += dash + str(countnumber)

                        numberdict[newnumber] = newrange

                        tracknumber.clear()
                        trackindex.clear()
                    else: 
                        numberdict[newnumber] = newrange

                        tracknumber.clear()
                        trackindex.clear()
                
                if c in symboldict.keys(): 
                    countsymbol += 1
                    
                    c += dash + str(countsymbol)

                    symboldict[c] = i

                else: 
                    symboldict[c] = i
    
    return numberdict, symboldict


def linetest(partnumberdict, currentsymboldict):
    validpartnumbers = []

    for p in partnumberdict: 
        #get index of number start / end
        firstnumberinrange = partnumberdict[p][0]
            
        if firstnumberinrange > 0: 
           firstnumberinrange -= 1
            
        # last index
        lastnumberinrange = partnumberdict[p][len(partnumberdict[p]) - 1]
        lastnumberinrange += 1

        for k in currentsymboldict.keys(): 
            if firstnumberinrange <= currentsymboldict[k] <= lastnumberinrange:
                validpartnumbers.append(p)

    # IF found fix formatting if necessary
    # loop through validpartnumbers lsit and fix as necessary. 
    formattedvalidpartnumbers = []

    for partnumber in validpartnumbers: 
        if dash in partnumber: 
            fixedpartnumber = partnumber.split(dash, 1)[0] # take everything before the -
            formattedvalidpartnumbers.append(int(fixedpartnumber))
        else: 
            formattedvalidpartnumbers.append(int(partnumber))

    # return numbers
    return formattedvalidpartnumbers


# full part number list
allpartnumbers = []


# test first line
##firstlinenumbers, firstlinesymbols = readlineintodictionary(inputdata[0], numbersfromwords, period)

#secondlinenumbers, secondlinesymbols = readlineintodictionary(inputdata[1], numbersfromwords, period)

#firstlinevalidnumbers = linetest(firstlinenumbers,firstlinesymbols, secondlinesymbols)

#for n in firstlinevalidnumbers: 
#    allpartnumbers.append(n)


# start reading all lines.
for i in range(1, len(inputdata)): 
    previouslinenumbers, previouslinesymbols = readlineintodictionary(inputdata[i - 1], numbersfromwords, period)

    currentlinenumbers, currentlinesymbols = readlineintodictionary(inputdata[i], numbersfromwords, period)

    #previouslinevalidnumbers = linetest(previouslinenumbers, previouslinesymbols, currentlinesymbols)
    
    #for n in previouslinevalidnumbers: 
    #    allpartnumbers.append(n)



    currentnumberssameline = linetest(currentlinenumbers, currentlinesymbols)
    currentnumberspreviousline = linetest(currentlinenumbers, previouslinesymbols)

    currentsymbolspreviousline = linetest(previouslinenumbers, currentlinesymbols)
    

    # current line vs itself
    # current line vs previous symbols 

    # current symbols vs previous line numbers
    # current 

    # -------
    # current number vs current symbols 
    
    # previous symbols vs current numbers 
    # previous numbers vs current symbols 














    for n in currentnumberssameline: 
        allpartnumbers.append(n)

    for n in currentnumberspreviousline: 
        allpartnumbers.append(n)

    for n in currentsymbolspreviousline: 
        allpartnumbers.append(n)
        
    print(allpartnumbers)

for partnumbers in allpartnumbers: 
    number = int(partnumbers)
    sumtotal += number

print(sumtotal)