"""
graphpaper.py

Print "+", "-", "|", " " to draw a graph.

"""

import sys

def getInt(ask):
    assert isinstance(ask, str)
    while True:
        try:
            inputvalue = input(ask)
        except EOFError:
            sys.exit(0)

        try:
            i = int(inputvalue)
        except ValueError:
            print("Sorry,", inputvalue, "is not an integer.")
            continue #Go back up to the word "while"

        return i


r = getInt("How many rows of boxes?\t")
c = getInt("How many columns of boxes?\t")
rb = getInt("How many rows of blanks in each boxes?\t")
cb = getInt("How many columns of blanks in each boxes?\t")

plus = ("+")
dash = ("-")
bar = ("|")
space = (" ")

h = 1
while h <= c:
    
    j = 1
    while j <= r:
        print(plus, end="")
        print(cb*dash, end="")
        j += 1
    print(plus)

    l = 1
    while l <= rb:
        i = 1
        while i <= r:
            print(bar, end="")
            print(cb*space, end="")
            i += 1
        print(bar)
        l += 1
    h += 1

m = 1
while m <= r:
    print(plus, end="")
    print(cb*dash, end="")
    m += 1
print(plus)
    
sys.exit(0)
