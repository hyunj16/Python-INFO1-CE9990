
import sys

s = "today"

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
            if currentword == vowel:
                print("FOUND IT.")
                return i   #instead of the break
            n += 1
        i += 1
    print("The word contains no vowels.")
    return -1

testing = findmultipleconsonant(s)
print(testing)
sys.exit(0)
