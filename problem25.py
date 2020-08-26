'''
What's the index of the first term in the Fibonacci sequence
to contain 1000 digits?
'''

def fib1000():
    i=2
    d= {}
    d[1] = 1
    d[2] = 1
    f = 0

    while len(str(f)) < 1000:
        i += 1
        f = d[i-1] + d[i-2]
        d[i] = f
    print(len(str(d[i])))
    return i

r = fib1000()

print("\nResult: " + str(r) + "\n")