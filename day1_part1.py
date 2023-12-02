# This is for the Advent of Code
# day 1 part 1

# read file
# break string
# check for numbers
# add to temp list? 
# take first and last value from list. 
# make number
# add to running total? 

# list of chars from input string
def stringtolist(inputstring):
    listfromstring = []
    listfromstring.extend(inputstring)
    return listfromstring


def makeanumber(inputarray):
    first = inputarray[0]
    last = inputarray[len(inputarray) - 1]
    number = int(first + last)
    return number



# start

numbers = ["1","2","3","4","5","6","7","8","9","0"]

day1inputfile = open("/Users/dyl13740/Documents/AdventofCode2023/day1input.txt")

day1inputdata = day1inputfile.readlines()

print(day1inputdata[0]) # first line
print(day1inputdata[len(day1inputdata) - 1]) # last line

result = 0


for lines in day1inputdata:
    chararray = stringtolist(lines)

    tempnumbers = []

    for c in chararray:
        if c in numbers:
            tempnumbers.append(c)
            #print(tempnumbers)

    #result = result + makeanumber(tempnumbers)
    
    
    numbertoadd = makeanumber(tempnumbers)
    result = result + numbertoadd

    #print(tempnumbers)
    #print(numbertoadd)
    #print(result)


# end
print(result)
