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
            print("Sorry,", inputvalue, "is not an integer.")
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
            print("Sorry,", inputvalue, "is not a float.")
            continue
        return i

def getconversionchoice():
    while True:
        conversionchoice = getInt("Choose either 1 or 2:\t")

        if conversionchoice == 1 or conversionchoice == 2:
            break
        print("Sorry, ", conversionchoice, " is not a valid choice.", sep="")

    print()
    print("You chose", conversionchoice, "as your choice.")
    return conversionchoice

def choice1():
    print(conversionchoice, ". We will now convert Fahrenheit to Celsius.", sep="")
    print()
    if True:
        inputfahrenheit = getFloat("What is the temperature in Fahrenheit?\t")
        outputcelsius = (inputfahrenheit - 32) / 1.8
        #inputfahrenheit = int(inputfahrenheit)
        #outputcelsius = int(outputcelsius)
        celsiusoutput = "{} degrees in Fahrenheit is {:3} degrees in Celsius.".format(inputfahrenheit, outputcelsius)
        printoutcome(celsiusoutput)

def choice2():
    print(conversionchoice, ". We will now convert Celsius to Fahrenheit.", sep="")
    print()
    if True:
        inputcelsius = getFloat("What is the temperature in Celsius?\t")
        outputfahrenheit = inputcelsius * 1.8 + 32
        #inputcelsius = int(inputcelsius)
        #outputfahrenheit = int(outputfahrenheit)
        fahrenheitoutput = "{} degrees in Celsius is {:3} degrees in Fahrenheit.".format(inputcelsius, outputfahrenheit)
        printoutcome(fahrenheitoutput)

def printoutcome(a):
    print(a)
    print()
    
def closing():
    return input("Enter \"Y\" to continue:\t")
    
processchoice = "y"
while processchoice == "y":
    opening()

    conversionchoice = getconversionchoice()
    if conversionchoice == 1:
        choice1()
    else:
        choice2()
    
    processchoice = closing().lower()

print()
print("You didn't enter \"Y\". Thank you for using. Good-bye.")
