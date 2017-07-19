"""
week3_year_in_roman_numeral.py

Tried to come up with different method to convert a number in Roman numerals using "while" loop and manipulating strings.
"""

import sys

def opening():
    print()
    print("Welcome to Roman Numeral Converter")
    print()
        
def printoutcome(a, b):
    print(a)
    print(b)
    print()

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
            continue
        return i

numerals = [
    [1000, "M"],
    [ 900, "CM"],
    [ 500, "D"],
    [ 400, "CD"],
    [ 100, "C"],
    [  90, "XC"],
    [  50, "L"],
    [  40, "XL"],
    [  10, "X"],
    [   9, "IX"],
    [   5, "V"],
    [   4, "IV"],
    [   1, "I"]
]

def calculation(number):
    roman = ""
    for numeral in numerals:
        while number >= numeral[0]:
            number -= numeral[0]
            roman += numeral[1]
    return roman
    
def results(c, d):
    print("You entered ", c, ", and its roman numeral is \"", d, "\".", sep="")
    print()

#Welcome Message
opening()
askchoice = "y"

while askchoice == "y":
    #Values
    inputnumber = int(input("Please enter a number:\t"))
    while inputnumber > 4000 or inputnumber <= 0:
        print()
        print("Your number is out of range for Roman Numerals.")
        print("Please enter a number between 1 and 3999.")
        inputnumber = int(input("Please enter a number:\t"))
        continue
    initialroman = ""
    initialnumber = inputnumber

    #Processing Roman Numeral
    romanoutput = calculation(inputnumber)

    #Print Outcome
    results(initialnumber, romanoutput)
    print("Would you like to convert another number?")
    askchoice = str.lower(input("Please enter \"Y\" to continue:\t"))
print("You didn't \"Y\".")
print("Thanks for using. Good bye.")

sys.exit(0)
