# Camel Cards


# list of hands

# goal is to order based on strength of hands


# on hand, 5 cards
# all possible cards:  A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, 2

# every hand has one type. 
# five of a kind
#   AAAAA

# four of a kind
#   AAAA2

# full house
#   23332

# three of a kind 
#   TTT98

# two pair
# 23432

# one pair
# A23A4

# high card
#   23456

# if hands are the same type
#   compare first, second, third, .... card to find highest
#   hand with the highest individual card when compared is "higher hand"


# each hand has a bid amount
#   strongest hand has rank = total number of hands

#   total winnings == (rank * bid amount) + rank * bid amount) ... for all hands



# readfile
# read lines into list


# identify hand type
#   use a hit list? 
#   hits = [1,0,0,0,0,0,1,0,0,0,2]
#   hits track the number of cards in the hand / index matching the card identifier list


# add hand to type dictionary? 

# sort type dictionary? 


# get data
inputdata = []

inputfile = "Day7/day7_input.txt"
with open(inputfile, 'r') as file: 
    lines = file.readlines()

    for line in lines: 
        inputdata.append(line.strip('\n'))

#split hand info in to hand and bid
def splithandinfo(inputstring): 
    splitinput = inputstring.split()

    cards = splitinput[0]
    bid = splitinput[1]

    return cards, bid


def sortlistofhands(listofhands, allpossbilecards): 
    sortedhandsandbids = []
    handsandbids = {}
    
    sortedhands = []
    handsaslist = []

    for hand in listofhands: 
        cardsinhand, bidofhand = splithandinfo(hand)

        handsandbids[cardsinhand] = bidofhand
        handsaslist.append(cardsinhand)

    sortfunction = lambda s: tuple(allpossbilecards.index(char) for char in s)

    sortedhands = sorted(handsaslist, key=sortfunction)

    for h in sortedhands:
        sortedhandsandbids.append(f'{h} {handsandbids[h]}')

    return sortedhandsandbids







# hand types
fiveofakind = []
fourofakind = []
fullhouse = []
threeofakind = []
twopair = []
onepair = []
highcard = []

cards = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
cardcount = len(cards)



# find hand type and separate into specific list
for hand in inputdata: 
    
    # list with 0s for length of the cards list. 
    cardsfound = [0 for _ in range(cardcount)]

    cardsinhand, bidofhand = splithandinfo(hand)

    # find card in hand / count it
    for c in cards: 
        numberofcards = cardsinhand.count(c)

        # index of card from cards list
        cardindex = cards.index(c)
        cardsfound[cardindex] += numberofcards

    if 5 in cardsfound:
        fiveofakind.append(hand)
    
    elif 4 in cardsfound:
        fourofakind.append(hand)

    elif 3 in cardsfound:
        if 2 in cardsfound:
            fullhouse.append(hand)
        else:
            threeofakind.append(hand)

    elif 2 in cardsfound:
        if cardsfound.count(2) == 2:
            twopair.append(hand)
        else:
            onepair.append(hand)

    else:
        highcard.append(hand)


# sort lists on scoring
# read cards
# compare first card, second etc

sortedfiveofakind = sortlistofhands(fiveofakind, cards)
sortedfourofakind = sortlistofhands(fourofakind, cards)
sortedfullhouse = sortlistofhands(fullhouse, cards)
sortedthreeofakind = sortlistofhands(threeofakind, cards)
sortedtwopair = sortlistofhands(twopair, cards)
sortedonepair = sortlistofhands(onepair, cards)
sortedhighcard = sortlistofhands(highcard, cards)

allsortedhandslist = sortedfiveofakind + sortedfourofakind + sortedfullhouse + sortedthreeofakind + sortedtwopair + sortedonepair + sortedhighcard
allsortedhandslist.reverse()
print(allsortedhandslist)


# do math
totalwinnings = 0

for h in range(0, len(allsortedhandslist)): 

    cardsinhand, bidofhand = splithandinfo(allsortedhandslist[h])

    totalwinnings += int(bidofhand) * (h + 1)

print(totalwinnings)


