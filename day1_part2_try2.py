
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

def findallindixesforstring(tofind, line):
    wherefound = []
    index = 0
    while index < len(line):
        index = line.find(tofind, index) # we move the starting point - index

        if index == -1:
            break

        wherefound.append((index, index + len(tofind) - 1 )) # add starting and ending indicies of string. 
        index += 1

    return wherefound



day1inputfile = open("/Users/dyl13740/Documents/AdventofCode2023/day1input.txt")

day1inputdata = day1inputfile.readlines()
cleaneddatta = []

#newlinechars removed
for line in day1inputdata:
    cleaneddatta.append(line.strip('\n'))

    

# start
for line in cleaneddatta:
    indexes = []
    values = []

    for k in numbersfromwords: # look throuhg keys
        
        if len(findallindixesforstring(k, line)) > 0: # if key is present
            indexes += findallindixesforstring(k, line) # could be -1
            values += [numbersfromwords[k]] * len(findallindixesforstring(k, line)) # create array with count number of entries. 

        if len(findallindixesforstring(numbersfromwords[k], line)) > 0:
            indexes += findallindixesforstring(numbersfromwords[k], line) # could be -1
            values += [numbersfromwords[k]] * len(findallindixesforstring(numbersfromwords[k], line))

        # indexes and values are arrays of the same length with values having their cooresponding indexes. 
    
    # so now need to sort both and take the first and last values. 
    firstindexes = [i[0] for i in indexes] # get first index for each tuple
    tempdict = dict(zip(firstindexes, values))
    
    # sort on keys
    sorteddict = dict(sorted(tempdict.items()))

    if len(sorteddict) == 1: 
        number = int(2 * next(iter(sorteddict.values()))) # double value if only one number
        sumtotal += number

    if len(sorteddict) > 1: 
        number = int(list(sorteddict.values())[0] + list(sorteddict.values())[-1]) # first and last values
        print(number)
        sumtotal += number

# end
print(sumtotal)

