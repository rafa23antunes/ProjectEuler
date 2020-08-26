'''
Biggest pandigital number
'''

import itertools
import math

def isPandigital(num):
    l = []
    s = str(num)
    for i in range(1,len(s)+1):
        l.append(i)
    for i in range(len(s)):
        if int(s[i]) in l:
            l.remove(int(s[i]))
    return len(l) == 0

#print(isPandigital(123498765))

def isPrime(num):
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

#print(isPrime(3300))22

def biggest(lis):
    l = list(itertools.permutations(lis))
    l = [[str(x) for x in tup] for tup in l]
    l2 = []
    for i in l:
        word = ''.join(i)
        l2.append(word)
    l3 = []
    for i in l2:
        if isPrime(int(i)):
            l3.append(int(i))
    return max(l3)


# My computer doesn't have enough 'power' to give me an answer.
# Maybe I have to do this in another way. Check this later...

# I comeback later and figure it out. I have to use itertools to see all the 
# combinations... I try with 9 digits, 8 digits and nothing... So with 7 digits
# and after some time i recived an answer... 7652413


l = [1,2,3,4,5,6,7]

print(biggest(l))