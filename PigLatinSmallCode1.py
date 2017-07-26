"""
PigLatinSmallCode1.py

Testing 
"""

import sys

s = "strictly"

def multipleconsonant(wordinput2):
    i = 0
    while i < 10:
        print(wordinput2[i])
        if wordinput2[i] == "i":
            break
        i += 1
    return i

testing = multipleconsonant(s)
print(testing)

sys.exit(0)
