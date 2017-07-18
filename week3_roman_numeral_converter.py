"""
week3_year_in_roman_numeral.py

Tried to come up with different method to convert a number in Roman numerals using "while" loop and manipulating strings.
"""

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

def calculation(number, roman):
    while number > 0:
        print()
        while number >= 1000:
            number -= 1000
            roman = roman + "M"
            #printoutcome(year, roman)
        while number >= 900:
            number -= 900
            roman = roman + "CM"
            #printoutcome(year, roman)
        while number >= 500:
            number -= 500
            roman = roman + "D"
            #printoutcome(year, roman)
        while number >= 400:
            number -= 400
            roman = roman + "CD"
            #printoutcome(year, roman)
        while number >= 100:
            number -= 100
            roman = roman + "C"
            #printoutcome(year, roman)
        while number >= 90:
            number -= 90
            roman = roman + "XC"
            #printoutcome(year, roman)
        while number >= 50:
            number -= 50
            roman = roman + "L"
            #printoutcome(year, roman)
        while number >= 40:
            number -= 40
            roman = roman + "XL"
            #printoutcome(year, roman)
        while number >= 10:
            number -= 10
            roman = roman + "X"
            #printoutcome(year, roman)
        while number >= 5:
            number -= 5
            roman = roman + "V"
            #printoutcome(year, roman)
        while number >= 4:
            number -= 4
            roman = roman + "IV"
            #printoutcome(year, roman)
        while number >= 1:
            number -= 1
            roman = roman + "I"
            #printoutcome(year, roman)
    return(roman)
    
def results(c, d):
    print("You entered ", c, ", and its roman numeral is \"", d, "\".", sep="")
    print()

#Welcome Message
opening()

#Values
inputnumber = int(input("Please enter a number:\t"))
if inputnumber > 4000 or inputnumber <= 0:
    print()
    print("Numbers are out of range for Roman Numerals.")
    print("Please enter a number between 1 and 3999.")
    inputnumber = int(input("Please enter a number:\t"))
else:
    initialroman = ""
    initialnumber = inputnumber
    initialroman

    #Processing Roman Numeral
    romanoutput = calculation(inputnumber, initialroman)

#Print Outcome
results(initialnumber, romanoutput)
