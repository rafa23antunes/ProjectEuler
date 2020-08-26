'''
It can be seen that the number 125874, and its double, 251748, contain exactly the
the same digits. but in a diferent order.

Find the smallest positive integer, x, sutch that 2x, 3x, 4x, 5x and 6x contain the same digits.
'''

# Function that tests if two numbers have the same digits
def testa(n1, n2):
    s1 = str(n1)
    s2 = str(n2)
    for i in s1:
        if i not in s2:
            return False
    for i in s2:
        if i not in s1:
            return False
    return True


def test_list(n, lis):
    for i in lis:
        if testa(n,i) == False:
            return False
    return True


def makeithappen():
    r=0
    b = False
    while(b==False):
        r+=1
        l = [2*r, 3*r, 4*r, 5*r, 6*r]
        if test_list(r,l):
            b= True
        else:
            l = []
    return r