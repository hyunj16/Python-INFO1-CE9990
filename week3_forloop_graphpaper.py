"""
week3_forloop_graphpaper.py

Graph Paper assignment using for loop.
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


for k in range(r):
    
    #Plus and Dash
    for h in range(c):
        print(plus, end="")
        for j in range(cb):
            print(dash, end="")
    print(plus)

    #Bar and Spaces
    for n in range(rb):
        for l in range(c):
            print(bar, end="")
            for m in range(cb):
                print(space, end="")    
        print(bar)

#Last Line
for o in range(c):
    print(plus, end="")
    for p in range(cb):
        print(dash, end="")
print(plus)
        
sys.exit(0)
