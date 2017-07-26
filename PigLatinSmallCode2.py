"""
PigLatinSmallCode2.py

Testing 
"""
import sys

s = "today"

def findmultipleconsonant(wordinput2):
    i = 0
    wordlength = len(wordinput2)
    check = 0
    while i < wordlength and check == 0:
        print(wordinput2[i])
        n = 0
        currentword = wordinput2[i]
        while n < 5:
            vowels = [
                "a",
                "e",
                "i",
                "o",
                "u"
            ]
            vowel = vowels[n]
            print(vowel)
            if currentword == vowel:
                print("FOUND IT.")
                check = 1
                break
            n += 1
        i += 1
    return i-1

testing = findmultipleconsonant(s)
print(testing)

sys.exit(0)
