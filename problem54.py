#read a file to a list of lines
with open('poker.txt') as f:
    lis = f.readlines()

# delete all '\n' from the strings
l = []
for i in lis:
    l.append(i.replace('\n',''))

# clean spaces and organize hands with tuples with lists
nl = []
for i in l:
    x = i[:14]
    y = i[14:]
    x = x.split()
    y = y.split()
    a = (x,y)
    nl.append(a)
    
d = {}
for i in range(len(nl)):
    d[i] = nl[i]
# Now we have a dictionary with an id and a tuple with the list of cards of player1 and player2

def removeSuit(l):
    nl = []
    for i in l:
        nl.append(i[:-1])
    return nl
    
# To use this function you shoul remove suits before
def sortPoker(l):
    nl = []
    if 'A' in l and '2' in l and '3' in l and '4' in l and '5' in l:
        return ['A','2','3','4','5'] 
    for i in l:
        if i > '1' and i <= '9':
            nl.append(int(i))
        elif i == 'T':
            nl.append(10)
        elif i == 'J':
            nl.append(11)
        elif i == 'Q':
            nl.append(12)
        elif i == 'K':
            nl.append(13)
        else: 
            nl.append(14) #A
    nl.sort()
    nnl = []
    for i in nl:
        if i > 1 and i <= 9:
            nnl.append(str(i))
        elif i == 10:
            nnl.append('T')
        elif i == 11:
            nnl.append('J')
        elif i == 12:
            nnl.append('Q')
        elif i == 13:
            nnl.append('K')
        else: 
            nnl.append('A') 
    return nnl     
      
def maxPoker(l): #returns the bigger card in the deck l
    # The deck l is already without suits
    if 'A' in l:
        return 'A'
    elif 'K' in l:
        return 'K'
    elif 'Q' in l:
        return 'Q'
    elif 'J' in l:
        return 'J'
    elif 'T' in l:
        return 'T'
    else:
        nl = []
        for i in l:
            nl.append(int(i))
        return str(max(nl))

def isFlush(l): #5 same color
    c = l[0][-1]
    for i in l:
        if i[-1] != c:
            return False
    return True

def isRoyal(l):
    nl = removeSuit(l)
    if 'A' in nl and 'K' in nl and 'Q' in nl and 'J' in nl and 'T' in nl and isFlush(l):
        return True
    return False

def isStraight(l): # It's sequence of 5
    srtd = [['A','2','3','4','5'],
            ['2','3','4','5','6'],
            ['3','4','5','6','7'],
            ['4','5','6','7','8'],
            ['5','6','7','8','9'],
            ['6','7','8','9','T'],
            ['7','8','9','T','J'],
            ['8','9','T','J','Q'],
            ['9','T','J','Q','K'],
            ['T','J','Q','K','A']]
    nl = removeSuit(l)
    nl =  sortPoker(nl)
    if nl in srtd:
        return True
    return False
  
def isStraightFlush(l):
    return isFlush(l) and isStraight(l)
        
def isFour(l): #4 of a kind
    nl = removeSuit(l)
    for i in nl:
        c = 0
        for j in nl:
            if j == i:
                c+=1
        if c == 4:
            return True
    return False

def isThree(l): #3 of a kind
    nl = removeSuit(l)
    for i in nl:
        c = 0
        for j in nl:
            if j == i:
                c+=1
        if c == 3:
            return True
    return False

def isPair(l): #1 pair only
    nl = removeSuit(l)
    for i in nl:
        c = 0
        for j in nl:
            if j == i:
                c+=1
        if c == 2:
            return True
    return False

def isFullHouse(l):
    return isThree(l) and isPair(l)

def isTwoPairs(l): 
    # This function counts if the hand has three diferent cards.
    # This means that there are a Three or TwoPairs. 
    # Later i will atribute prioritys to make this work properly.
    nl = removeSuit(l)
    e = []
    for i in nl:
        if i not in e:
            e.append(i)
    return len(e) == 3

def higherCard(l): #Returns the higher card of a deck
    nl = removeSuit(l)
    if 'A' in nl:
        return 'A'
    elif 'K' in nl:
        return 'K'
    elif 'Q' in nl:
        return 'Q'
    elif 'J' in nl:
        return 'J'
    elif 'T' in nl:
        return 'T'
    else:
        nnl = []
        for i in nl:
            nnl.append(int(i))
        return str(max(nnl))



def disDraw(l1,l2): # This is used when both have the HighestCard combination and the same highest card
    ll1 = removeSuit(l1)
    ll2 = removeSuit(l2)
    ll1 = sortPoker(ll1)
    ll2 = sortPoker(ll2)
    a = ll1.pop()
    b = ll2.pop()
    while a == b:
        a = ll1.pop()
        b = ll2.pop()
    if a > b:
        return "pl1"
    elif a < b:
        return "pl2"
    else:
        return "Draw"

def higherPair(l): #returns the value of the biggest pair. If there is only one pair, return the value of that pair.
    if isTwoPairs(l):
        nl = removeSuit(l)
        e = []
        while len(nl) > 0:
            a = nl.pop()
            if a in nl and a not in e:
                e.append(a)
        return maxPoker(e)
    if isPair(l):
        nl = removeSuit(l)
        for i in nl:
            c = 0
            for j in nl:
                if j == i:
                    c+=1
            if c == 2:
                return i

def higherThree(l): #returns the value of the Three combination
    nl = removeSuit(l)
    for i in nl:
        c = 0
        for j in nl:
            if j == i:
                c+=1
        if c == 3:
            return j

def higherFour(l): #returns the value of the Four combination
    nl = removeSuit(l)
    for i in nl:
        c = 0
        for j in nl:
            if j == i:
                c+=1
        if c == 4:
            return j

def deck(l): #Function that tells what's the combination of the player and his higher card. 
    # If it's a pair or two pairs, return the higher pair.
    # If it's a Three or a Four returns also the higher card. 
    if isRoyal(l):
        return ("9-Royal",higherCard(l))
    elif isStraightFlush(l):
        return ("8-Sflush",higherCard(l))
    elif isFour(l):
        return ("7-Four", higherFour(l))
    elif isFullHouse(l):
        return ("6-Fhouse", higherThree(l))
    elif isFlush(l):
        return ("5-Flush", higherCard(l))
    elif isStraight(l):
        return ("4-Straight", higherCard(l))
    elif isThree(l):
        return ("3-Three", higherThree(l))
    elif isTwoPairs(l):
        return ("2-2pairs", higherPair(l))
    elif isPair(l):
        return ("1-Pair", higherPair(l))
    else:
        return ("0-Hcard", higherCard(l))

def oneVSone(l1,l2):
    s1, v1 = deck(l1)
    s2, v2 = deck(l2)
    if s1 > s2:
        return "pl1"
    elif s2 > s1:
        return "pl2"
    else:
        if v1 > v2:
            return "pl1"
        elif v2 > v1:
            return "pl2"
        else:
            x = higherCard(l1)
            y = higherCard(l2)
            if x > y:
                return "pl1"
            elif x < y:
                return "pl2"
            else:
                return disDraw(l1,l2)
    
def whoWins(d):
    c1 = 0
    c2 = 0
    for i in d:
        if oneVSone(d[i][0],d[i][1]) == "pl1":
            c1 += 1
        else:
            c2 += 1
    print(c1)
    if c1 > c2:
        return "Player 1 wins!"
    elif c1 < c2:
        return "Player 2 wins!"
    else:
        print("One draw detected\n")
