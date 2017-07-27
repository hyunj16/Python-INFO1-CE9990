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
    vowels = [
        "a",
        "e",
        "i",
        "o",
        "u"
    ]
    wordinput1[0]
    #print(wordinput[0])
    for i, vowel in enumerate(vowels):
        if wordinput1[0] == vowel:
            #print("The same.")
            returnvalue = 1
            break
        else:
            returnvalue = 0
    return (returnvalue)

#Search for the first vowel in a word
def findmultipleconsonant(wordinput2):
    i = 0
    wordlength = len(wordinput2)
    check = 0
    while i < wordlength and check == 0:
        #print(wordinput2[i])
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
            if currentword == vowel:
                #print("FOUND IT.")
                check = 1
                break
            n += 1
        i += 1
    return i-1

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
