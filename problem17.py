"""
Euler Project 
In Python

Problem 17:
If numbers 1 to 5 are written out in words:one, two, three, four, five, then 
there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 inclusive were written in words, how many
letters would be used?

ans: 21124
"""

# I made a dictionary with some keywords (numbers) that I found out helpfull
d = {
    0: "",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
    100: "onehundred",
    200: "twohundred",
    300: "threehundred",
    400: "fourhundred",
    500: "fivehundred",
    600: "sixhundred",
    700: "sevenhundred",
    800: "eighthundred",
    900: "ninehundred",
    1000: "onethousand"
}

# Function that add a number to a dictionary in the format ' number: "string" ' 
def make(num, d):
    if num in d:
        return d[num]
    if len(str(num)) == 2:
        a = str(num)[0]
        b = str(num)[1]
        a += "0"
        r = make(int(a),d) + make(int(b),d)
        d[num] = r
    if len(str(num)) == 3 and str(num)[1:3] == "00":
        d[num] = make(int(str(num)[0]),d) + "hundred"
    if len(str(num)) == 3:
        a = str(num)[0]
        b = str(num)[1:3]
        a += "00"
        r = make(int(a),d) + "and" + make(int(b),d)
        d[num] = r
    return 0


for i in range(1,1000):
    make(i,d)
# this variable will store de result
c = 0
for i in range(0,len(d)):
    #print(d[i])
    c += len(d[i])

print("\nThe result is: " + str(c) +"\n")


