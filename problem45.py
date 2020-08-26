def tri(n):
    return int((n*(n+1))/2)

def pent(n):
    return int((n * (3*n -1))/2)

def hex(n):
    return n * (2 * n -1)

def geraT(ind):
    l = []
    for i in range(286,ind):
        l.append(tri(i))
    return l

def geraP(ind):
    l = []
    for i in range(185,ind):
        l.append(pent(i))
    return l

def geraH(ind):
    l = []
    for i in range(143,ind):
        l.append(hex(i))
    return l

def gera(max):
    lt = geraT(max)
    lp = geraP(max)
    lh = geraH(max)
    for i in lt:
        if i in lp and lh:
            #print(i)
            return i
    return "\nNot found\nTry another number max\n"

print(gera(10000))

# I'm supoused to give the next number after 40 thousand something that is Triangular,
# Pentagonal and Hexagonal... I found 7906276 that is lower than the correct answer wich
# is 1 and a half milion and something... Sooo I don't know...