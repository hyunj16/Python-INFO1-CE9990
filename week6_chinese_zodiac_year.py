"""
week6_chinese_zodiac_year.py

Tuple and dictionary
"""

import sys
import math

def opening():
    print()
    print("Welcome to Chinese Zodiac Year.")
    print("Enter your birth year to find out your Zodiac animal.")
    print()

def closing():
    print()    
    print("You didn't \"Y\".")
    print("Thanks for using. Good bye.")

def printresults(resultyear, resultanimal, resultdescription, resultnumber1, resultnumber2):
    print()
    print("You were born ", resultyear, ".", sep="")
    print("It was the year of ", resultanimal, ".", sep="")
    print()
    print(resultdescription)
    print()
    print("Your lucky numbers are ", resultnumber1, ".", sep="")
    print("But you should avoid following numbers: ", resultnumber2, ".", sep="")
    
def getYear(ask1):
    assert isinstance(ask1, str)
    while True:
        try:
            inputvalue = input(ask1)
        except EOFError:
            sys.exit(0)
        try:
            i = int(inputvalue)
        except ValueError:
            print("Sorry,", inputvalue, "is not a year.")
            continue
        return i

def getKey(ask2):
    assert isinstance(ask2, str)
    while True:
        try:
            inputvalue = input(ask2)
        except EOFError:
            sys.exit(0)
        try:
            h = int(inputvalue)
        except ValueError:
            print("Sorry,", inputvalue, "is not a string.")
            continue
        return h
    
def writtenformat(rawtuple):
    numberslength = checklength(rawtuple)
    #print(numberslength)
    writtentuple = str(rawtuple[:numberslength-1]) + " and " + str(rawtuple[-1])
    return writtentuple
    
def checklength(alist):
    lengthvalue = len(alist)
    return lengthvalue

def calculation(year):
    yearnumber = year % 12
    return yearnumber

animals = [
    ("monkey",
     {"description" : "Those born under the Chinese Zodiac sign of the Monkey thrive on having fun. \
They’re energetic, upbeat, and good at listening but lack self-control. They like being active and \
stimulated and enjoy pleasing self before pleasing others. They’re heart-breakers, not good at long-term \
relationships, morals are weak. Compatible with Rat or Dragon.",
      "luckynumbers" : (1, 7, 8),
      "unluckynumbers" : (2, 5, 9)}),  
    ("rooster",
     {"description" : "Those born under the Chinese Zodiac sign of the Rooster are practical, resourceful, \
observant, analytical, straightforward, trusting, honest, perfectionists, neat and conservative. Compatible \
with Ox or Snake.",
      "luckynumbers" : (5, 7, 8),
      "unluckynumbers" : (1, 3, 9)}),  
    ("dog",
     {"description" : "Those born under the Chinese Zodiac sign of the Dog are loyal, \
faithful, honest, distrustful, often guilty of telling white lies, temperamental, prone \
to mood swings, dogmatic, and sensitive. Dogs excel in business but have trouble finding mates. \
Compatible with Tiger or Horse.",
      "luckynumbers" : (3, 4, 9),
      "unluckynumbers" : (1, 6, 7)}),  
    ("boar",
     {"description" : "Those born under the Chinese Zodiac sign of the Pig are extremely nice, good-mannered \
and tasteful. They’re perfectionists who enjoy finer things but are not perceived as snobs. They enjoy helping \
others and are good companions until someone close crosses them, then look out! They’re intelligent, always \
seeking more knowledge, and exclusive. Compatible with Rabbit or Goat.",
      "luckynumbers" : (2, 5, 8),
      "unluckynumbers" : (1, 3, 9)}),  
    ("mouse",
     {"description" : "Those born under the Chinese Zodiac sign of the Rat are quick-witted, clever, charming, \
sharp and funny. They have excellent taste, are a good friend and are generous and loyal to others considered part \
of its pack. Motivated by money, can be greedy, is ever curious, seeks knowledge and welcomes challenges. Compatible \
with Dragon or Monkey.",
      "luckynumbers" : (2, 3),
      "unluckynumbers" : (5, 9)}),  
    ("ox",
     {"description" : "Another of the powerful Chinese Zodiac signs, the Ox is steadfast, solid, a goal-oriented \
leader, detail-oriented, hard-working, stubborn, serious and introverted but can feel lonely and insecure. Takes \
comfort in friends and family and is a reliable, protective and strong companion. Compatible with Snake or Rooster.",
      "luckynumbers" : (1, 9),
      "unluckynumbers" : (3, 4)}),  
    ("tiger",
     {"description" : "Those born under the Chinese Zodiac sign of the Tiger are authoritative, self-possessed, \
have strong leadership qualities, are charming, ambitious, courageous, warm-hearted, highly seductive, moody, \
intense, and they’re ready to pounce at any time. Compatible with Horse or Dog.",
      "luckynumbers" : (1, 3, 4),
      "unluckynumbers" : (6, 7, 8)}),  
    ("hare",
     {"description" : "Those born under the Chinese Zodiac sign of the Rabbit enjoy being surrounded by family \
and friends. They’re popular, compassionate, sincere, and they like to avoid conflict and are sometimes seen as \
pushovers. Rabbits enjoy home and entertaining at home. Compatible with Goat or Pig.",
      "luckynumbers" : (3, 4, 9),
      "unluckynumbers" : (1, 7, 8)}),  
    ("dragon",
     {"description" : "A powerful sign, those born under the Chinese Zodiac sign of the Dragon are energetic and \
warm-hearted, charismatic, lucky at love and egotistic. They’re natural born leaders, good at giving orders and \
doing what’s necessary to remain on top. Compatible with Monkey and Rat.",
      "luckynumbers" : (1, 6, 7),
      "unluckynumbers" : (3, 8, 9)}),  
    ("snake",
     {"description" : "Those born under the Chinese Zodiac sign of the Snake are seductive, gregarious, \
introverted, generous, charming, good with money, analytical, insecure, jealous, slightly dangerous, \
smart, they rely on gut feelings, are hard-working and intelligent. Compatible with Rooster or Ox.",
      "luckynumbers" : (2, 8, 9),
      "unluckynumbers" : (1, 6, 7)}),  
    ("horse",
     {"description" : "Those born under the Chinese Zodiac sign of the Horse love to roam free. They’re \
energetic, self-reliant, money-wise, and they enjoy traveling, love and intimacy. They’re great at \
seducing, sharp-witted, impatient and sometimes seen as a drifter. Compatible with Dog or Tiger.",
      "luckynumbers" : (2, 3, 7),
      "unluckynumbers" : (1, 5, 6)}),  
    ("sheep",
     {"description" : "Those born under the Chinese Zodiac sign of the Goat enjoy being alone in their \
thoughts. They’re creative, thinkers, wanderers, unorganized, high-strung and insecure, and can be \
anxiety-ridden. They need lots of love, support and reassurance. Appearance is important too. \
Compatible with Pig or Rabbit.",
      "luckynumbers" : (2, 7),
      "unluckynumbers" : (3, 8)}),  
]

check = "y"
while check == "y":
    #Opening
    opening()

    #User Input
    year = getYear("Please enter your year:\t")
    #initialyear = year
    #print("You entered ", year, ".", sep="")

    animalnumber = calculation(year)
    #print(animalnumber)
    theanimal = animals[animalnumber][0]
    #print(theanimal)
    yeardescription = animals[animalnumber][1]["description"]
    luckynumbers = animals[animalnumber][1]["luckynumbers"]
    unluckynumbers = animals[animalnumber][1]["unluckynumbers"]
    
    #print(yeardescription)

    
    luckyresults = writtenformat(luckynumbers)
    unluckyresults = writtenformat(unluckynumbers)
    #print(luckynumberslength, unluckynumberslength)
    
    #Results
    printresults(year, theanimal, yeardescription, luckyresults, unluckyresults)
    
    #Check if the user want to continue
    print()
    print("Would you like to try again?")
    check = str.lower(input("Please enter \"Y\" to continue:\t"))

#Closing
closing()

sys.exit(0)
