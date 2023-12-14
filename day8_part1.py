
# get data
inputdata = []

inputfile = "Day8/day8_input.txt"
with open(inputfile, 'r') as file: 
    lines = file.readlines()

    for line in lines:      
        inputdata.append(line.strip('\n'))

# func
def tryfindnode(node, tofind, stepcount, leftright, network):
    left = 'L'
    right = 'R'

    found = False
    count = stepcount

    if leftright == left: 
        nextnode = network[node][0]

        count += 1

        if nextnode == tofind:
            found = True
            return found, count, nextnode
        else:
            return found, count, nextnode
        
        
    if leftright == right: 
        nextnode = network[node][1]

        count += 1

        if nextnode == tofind: 
            found = True
            return found, count, nextnode
        else:
            return found, count, nextnode



# start

rightleftpattern = inputdata[0].strip()

nodenetwork = {}
nodelist = []

for i in range(2, len(inputdata)):

    # make dictionary
    nodemap = inputdata[i].split('=')
    formatnodelinks = nodemap[1].replace('(','').replace(')','').replace(' ','').strip()


    node = nodemap[0].strip()
    nodelinks = formatnodelinks.split(',')

    nodelist.append(node)
    nodenetwork[node] = nodelinks


# follow the RL pattern
nodetofind = 'ZZZ'
totalsteps = 0

currentnode = nodelist[0]

foundzzz = False

loopcount = 0

# while not found keep looping through 
while not foundzzz:
    for direction in rightleftpattern: 

        found, totalsteps, currentnode = tryfindnode(currentnode, nodetofind, totalsteps, direction, nodenetwork)

    loopcount += 1

    print(f'loop {loopcount}')
    print(f'{currentnode, totalsteps}')

    if found == True:
        print(f' {currentnode} - {found} in {totalsteps} steps')

        foundzzz = True

    


