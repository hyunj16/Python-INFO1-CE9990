"""
week2_temperatureconverter.py

Calculating simple math to convert units while using functions and write-on effect to show results
"""

import sys
import math

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

def printoutcome(a, b):
    print(a)
    print()
    
print("Conversion of Temperature")
print("Choose from one of the two options.")
print("1. Fahrenheit to Celsius.")
print("2. Celsius to Fahrenheit.")

while True:
    conversionchoice = getInt("Choose either 1 or 2:\t")

    if conversionchoice == 1 or conversionchoice == 2:
        break
    print("Sorry, ", conversionchoice, " is not a valid choice.", sep="")

print()
print("You chose", conversionchoice, "as your choice.")

if conversionchoice == 1:
    print(conversionchoice, ". We will now convert Fahrenheit to Celsius.", sep="")
    print()
    while True:
        inputfahrenheit = getFloat("What is the temperature in Fahrenheit?\t")
        outputcelsius = (inputfahrenheit - 30) / 2
        #inputfahrenheit = int(inputfahrenheit)
        #outputcelsius = int(outputcelsius)
        celsiusoutput = "{} degrees in Fahrenheit is {:3} degrees in Celsius.".format(inputfahrenheit, outputcelsius)
        printoutcome(celsiusoutput)
    
else:
    print(conversionchoice, ". We will now convert Celsius to Fahrenheit.", sep="")
    print()
    while True:
        inputcelsius = getFloat("What is the temperature in Celsius?\t")
        outputfahrenheit = inputcelsius * 2 + 30
        #inputcelsius = int(inputcelsius)
        #outputfahrenheit = int(outputfahrenheit)
        fahrenheitoutput = "{} degrees in Celsius is {:3} degrees in Fahrenheit.".format(inputcelsius, outputfahrenheit)
        printoutcome(fahrenheitoutcome)

