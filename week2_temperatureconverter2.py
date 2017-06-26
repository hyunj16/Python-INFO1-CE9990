"""
week2_temperatureconverter2.py

Calculating simple math to convert units while using functions and write-on effect to show results
"""

import sys
import math

def opening():
    print()
    print("Conversion of Temperature")
    print("Choose from one of the two options:")
    print()
    print("1. Fahrenheit to Celsius.")
    print("2. Celsius to Fahrenheit.")
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
            print("Sorry, ", inputvalue, " is not an integer.", sep="")
            continue
        return i

def getFloat(ask):
    assert isinstance(ask, str)
    while True:
        try:
            inputvalue = input(ask)
        except EOFError:
            sys.exit(0)
        try:
            i = float(inputvalue)
        except ValueError:
            print("Sorry, ", inputvalue, " is not an integer.", sep="")
            continue
        return i

def getconversionchoice():
    while True:
        conversionchoice = getInt("Choose either 1 or 2:\t")

        if conversionchoice == 1 or conversionchoice == 2:
            break
        print("Sorry, ", conversionchoice, " is not a valid choice.", sep="")

    print()
    print("You chose ", conversionchoice, " as your choice.", sep="")
    return conversionchoice

def choice1():
    print(conversionchoice, ". We will now convert Fahrenheit to Celsius.", sep="")
    print()
    while True:
        inputfahrenheit = getFloat("What is the temperature in Fahrenheit?\t")
        outputcelsius = (inputfahrenheit - 30) / 2
        #inputfahrenheit = int(inputfahrenheit)
        #outputcelsius = int(outputcelsius)
        celsiusoutput = str("{} degrees in Fahrenheit is {:3} degrees in Celsius.".format(inputfahrenheit, outputcelsius))
        celsiusoutputlength = len(celsiusoutput)
        printoutcome(celsiusoutput, celsiusoutputlength)
        break

def choice2():
    print(conversionchoice, ". We will now convert Celsius to Fahrenheit.", sep="")
    print()
    while True:
        inputcelsius = getFloat("What is the temperature in Celsius?\t")
        outputfahrenheit = inputcelsius * 2 + 30
        #inputcelsius = int(inputcelsius)
        #outputfahrenheit = int(outputfahrenheit)
        fahrenheitoutput = str("{} degrees in Celsius is {:3} degrees in Fahrenheit.".format(inputcelsius, outputfahrenheit))
        fahrenheitoutputlength = len(fahrenheitoutput)
        printoutcome(fahrenheitoutput, fahrenheitoutputlength)
        break

def printoutcome(a, b):
    counter = 0
    while counter < b:
        print(a[counter], end="")
        counter += 1
    print()
    print()
    
def closing():
    closingvalue = input("Enter \"Y\" to continue:\t")
    return closingvalue
    
processchoice = "y"
while processchoice == "y":
    opening()

    conversionchoice = getconversionchoice()
    if conversionchoice == 1:
        choice1()
    else:
        choice2()
    
    processchoice = str.lower(closing())

print("You didn't enter \"Y\". Thank you for using. Good-bye.")
