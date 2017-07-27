"""

week5_pig_latin.py

Pig Latin using "list" "enumerate" and "for" loop.  Finds multiple consonants and process it.
"""

import sys

def opening():
    print()
    print("Welcome to Pig Latin Converter")

def getStr(ask):
    assert isinstance(ask, str)
    while True:
        try:
            inputvalue = input(ask)
        except EOFError:
            sys.exit(0)
        try:
            i = str(inputvalue)
        except ValueError:
            print("Sorry,", inputvalue, "is not a word.")
            continue
        return i

#Search first letter for a vowel
def findvowels(wordinput1):
    return 1 if wordinput1[0] in "aeiou" else 0

#Search for the first vowel in a word
def findmultipleconsonant(wordinput2):
    for i, c in enumerate(wordinput2):
        if c in "aeiou":
            #print("FOUND IT.")
            return i
    print("The word contains no vowels.")
    return -1

def processing(choice, initialword):
    consonantplacement = findmultipleconsonant(initialword)
    if consonantplacement == 0:
        initialword = initialword + "way"
    else:
        initialword = initialword[consonantplacement:] + initialword[:consonantplacement] + "ay"
    return initialword

def printout(a, b):
    print()
    print("You entered \"", a, ".\" ", sep="")
    print("Pig Latin for \"", a, "\" is \"", b, ".\"", sep="")

#Welcome Message
opening()
askchoice = "y"

while askchoice == "y":
    print()
    word = getStr("Please enter a word:\t")
    initial = word

    #print(word)
    #print(type(word))

    found = findvowels(word)

    #print(found)

    processedword = processing(found, word)

    #print(processedword)

    printout(initial, processedword)
    print()
    print("Would you like to convert another word?")
    askchoice = str.lower(input("Please enter \"Y\" to continue:\t"))

print()    
print("You didn't \"Y\".")
print("Thanks for using. Good bye.")
