"""
PigLatinSmallCode2.py

Testing 
"""
import sys

s = "strictly"

def findmultipleconsonant(wordinput2):
    i = 0
    wordlength = len(wordinput2)
    while i < wordlength:
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
            #print(vowel)
            if wordinput2[i] == vowel:
                print("FOUND IT.")
                break
            n += 1
        i += 1
    return i

testing = findmultipleconsonant(s)
print(testing)

sys.exit(0)
