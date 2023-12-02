# It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".


# read file
# break string
# check for numbers
# check for word numbers

# add to temp list? 
# take first and last value from list. 
# make number
# add to running total? 

# making number from line: 
# read string
# read character
# check character against number list
# if not in then keep reading and add to temp string
# when you get to number STOP. check temp string against number strings
# add number string to list
# add number to list
# delete temp string
# keep reading string




# list of chars from input string
def stringtolist(inputstring):
    listfromstring = []
    listfromstring.extend(inputstring)
    return listfromstring

# number from first and last value in array
def makeanumber(inputarray):
    first = inputarray[0]
    last = inputarray[len(inputarray) - 1]
    number = int(first + last)
    return number

def listtostring(inoputarray):
    emptystring = ''.join(inoputarray)
    return emptystring


def findanumbertest(inputchararray):
    tempstring = listtostring(inputchararray)

    for n in numbersfromwords.keys(): # for each key, is it in the temp string.
        if n in tempstring:
            found = True
            foundnumber = numbersfromwords[n]
            break
        else:
            found = False
            foundnumber = ''
    
    return found, foundnumber

    
    

numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
'''
numbersfromwords = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    'zero': 0
}
'''

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

day1inputfile = open("/Users/dyl13740/Documents/AdventofCode2023/day1input.txt")

day1inputdata = day1inputfile.readlines()
cleaneddatta = []
#newlinechars removed
for line in day1inputdata:
    cleaneddatta.append(line.strip('\n'))

result = 0
count = 0

# start
for lines in cleaneddatta:
    chararray = stringtolist(lines)

    # array for numbers found
    tempnumbers = []

    tempword = []

    for c in chararray:
        if c in numbers:
            tempnumbers.append(c)

        else:
            tempword.append(c)

            if len(tempword) > 1:
                numbertestresults = findanumbertest(tempword)
                
                # unpack tuple of test results
                found, numberfound = numbertestresults

                if found == True:
                    tempword.clear()
                    tempnumbers.append(numberfound)
    
    # now we process the line and make our number
    number = makeanumber(tempnumbers)

    count += 1
    print(f"line {count} - lines {lines} - number {number}")
    result += number


print(result) #






