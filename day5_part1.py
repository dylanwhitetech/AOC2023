# to find

# seed number
# destination range start
# source range start
# range length

# seed-to-soil mao
# 50 98 2
# 52 50 48

# first line # 50 98 2
# destination range start = 50 [50 51]
# source range start = 98  [98 99]
# range length = 2 

# seed number 98 = soil number 50 / 99 = soil number 51

# line 2 # 52 50 48
# destination range start = 52 [52 99]
# source range start = 50 [50 97]
# range length = 48

# seed number 53 = soil number 55

# numbers NOT in source / destination are the same destination and number 
# seed  soil
# 0     0
# 1     1
# ...   ...
# 48    48
# 49    49
# 50    52
# 51    53
# ...   ...
# 96    98
# 97    99
# 98    50
# 99    51

# Seed number 79 corresponds to soil number 81.
# Seed number 14 corresponds to soil number 14.
# Seed number 55 corresponds to soil number 57.
# Seed number 13 corresponds to soil number 13.

# FIND the CLOSEST LOCATION 
#Seed 79, soil 81, fertilizer 81, water 81, light 74, temperature 78, humidity 78, location 82.
#Seed 14, soil 14, fertilizer 53, water 49, light 42, temperature 42, humidity 43, location 43.
#Seed 55, soil 57, fertilizer 57, water 53, light 46, temperature 82, humidity 82, location 86.
#Seed 13, soil 13, fertilizer 52, water 41, light 34, temperature 34, humidity 35, location 35.

# seed 13 is closest 
# answer is 35

colon = ':'

# get data
inputdata = []

inputfile = "/Users/dyl13740/Documents/AdventofCode2023/day5_inputexample.txt"
with open(inputfile, 'r') as file: 
    lines = file.readlines()

    for line in lines: 
        inputdata.append(line.strip('\n'))


numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

#seeds:

#seed-to-soil map
#soil-to-fertilizer map
#fertilizer-to-water map
#water-to-light map
#light-to-temperature map
#temperature-to-humidity map
#humidity-to-location map

# store strings for seed info.
seedinformation = []

soil = 'seed-to-soil map:'
fertilizer = 'soil-to-fertilizer map:'
water = 'fertilizer-to-water map:'
light = 'water-to-light map:'
temperature = 'light-to-temperature map:'
humidity = 'temperature-to-humidity map:'
location = 'humidity-to-location map:'

# add to list

seedinformation.append(soil)
seedinformation.append(fertilizer)
seedinformation.append(water)
seedinformation.append(light)
seedinformation.append(temperature)
seedinformation.append(humidity)
seedinformation.append(location)


# functions 
def getseednumbers(inputdataarray):
    #seednumberarray = []

    seedsline = inputdataarray[0]

    splitline = line.split(colon)
    listofseeds = splitline[0].split()[1]

    seednumberarray = listofseeds.split()

    return seednumberarray



def formatcategorydata(currentcategoryarray, listofcategories): 

    # currentcategoryarray = 'seed-to-soil map:', '50 98 2', '52 50 48'
    # seed number 50 = 98
    # seed number 51 = 99

    # I want to store the first and last number in the range. 
    # so take first number and ADD the range value given - 1

    categoryranges = []
    categorykey = ''

    for item in currentcategoryarray: 
        if item in listofcategories:
            categorykey = item
        else:
            temparray = item.split()
            
            numberarray = [] # everything in line as number

            for i in temparray:
                numberarray.append(int(i))

            # make the ranges 
            currentlinedata = []
            destinationrange = []
            sourcerange = []

            destinationrange.append(numberarray[0]) # destination start
            destinationrange.append(numberarray[0] + (numberarray[2] - 1)) #destination end

            sourcerange.append(numberarray[1])
            sourcerange.append(numberarray[1] + (numberarray[2] - 1))

            # add ranges to their own list 
            # add range list to categoryranges
            currentlinedata.append(destinationrange)
            currentlinedata.append(sourcerange)

            categoryranges.append(currentlinedata)
            #print(currentlinedata)

    return categorykey, categoryranges

# make map
def makecategorymap(): 
    # use categorydata dictionary BUT already filtered for our specific map
    # import the category 
    # create the number map 
    # check if "seed" or other value is within range
    # output the number it mapped too

    # if the current category is location, note that so we can stop looping. 

    

# loop through the input data line by line 
# if we find a category. 
# make category dictionary KVP with category and lines of data
# 
# clear previous category list. 


# start

# store current category info store each line. 
currentcategoryinfo = []

# store numbers in category data dictionary
# 'category name': [line 1 numbers][line 2 numbers]...[line n numbers]
categorydata = {}

for i in range(2, len(inputdata)): # start of first line of relevent data
    currentline = inputdata[i]

    if currentline in seedinformation and len(currentcategoryinfo) > 1: 
        categorykey, categoryranges = formatcategorydata(currentcategoryinfo, seedinformation)
            
        categorydata[categorykey] = categoryranges
            
        #print(categorydata)
        currentcategoryinfo.clear()
        
        # start new category
        currentcategoryinfo.append(currentline)


    else: 
        # check for blank lines
        if len(currentline) > 1:
            currentcategoryinfo.append(currentline)


# find location for seeds. 

#for seed in categorydata: 
#    print(f'{item} {categorydata[item]}')

# get seed numbers
seednumbers = getseednumbers(inputdata)

for seed in seednumbers:

    # all data in dictionary: categorydata {}

    # seed to soil
    seedtosoilmap = categorydata[soil]

    # source (seed)
    sourcerange = seedtosoilmap[1]
    destinationrange = seedtosoilmap[0]

    # for number of source / destination ranges in the map
    # create number mapping? 

    # if seed does not fall in ranges then it equals itself? 
    # what if number between ranges? 





    # soil to fertilizer

    # fertilizer to water

    # water to light

    # light to temperature

    # temperature to humidity

    # humidity to location
    # save location


