import sys

s = "today"

def findmultipleconsonant(wordinput2):
    for i, c in enumerate(wordinput2):
        print(c)
        if c in "aeiou":
            print("FOUND IT.")
            return i
    print("The word contains no vowels.")
    return -1

testing = findmultipleconsonant(s)
print(testing)

sys.exit(0)
