"""

week7_grades.py

Take in user input of test scores to a list and outputs a letter grade.
Tried to use "append" list, and "return" results with "function"
"""

import sys

def opening():
    print()
    print("Welcome to Letter Grade Calculator.")
    print("Type in your test scores, and when you're finished, type \"done\" to see results.")
    print()
    
def askinput(ask):
    assert isinstance(ask, str)
    while True:
        try:
            inputvalue = input(ask)
        except EOFError:
            sys.exit(0)
        return inputvalue
    
def printresults(results1, results2, results3, results4, results5):
    print()
    print("These are your input numbers:\t", results1, ".", sep="")
    print("You have entered ", results2, " test scores in total.", sep="")
    print("The total test score is ", results3, ".", sep="")
    print("The average test score is ", results4, ".", sep="")
    print("Your grade is ", results5, ".", sep="")

def calculation(finalscore):
    letter = ""
    for lettergrade in lettergradelist:
        if finalscore >= lettergrade[0]:
            letter = lettergrade[1]
            #print(score)
            #print(letter)
            return letter

lettergradelist = [
    [100, "A+"],
    [94, "A"],
    [90, "A-"],
    [87, "B+"],
    [84, "B"],
    [80, "B-"],
    [77, "C+"],
    [74, "C"],
    [70, "C-"],
    [67, "D+"],
    [64, "D"],
    [60, "D-"],
    [0, "F"]
]

check = "y"

while check == "y":
    listofgrades = []
    counter = 0
    
    opening()

    inputscores = 0
    totalscore = 0
    while True:
        inputscores = askinput("Please enter your grade and hit enter:\t")
        if inputscores == "done":
            break
        else:
            counter += 1
            scores = int(inputscores)
            listofgrades.append(scores)
            totalscore += scores
            averagescore = totalscore / counter
    finalletter = calculation(averagescore)
          
    printresults(listofgrades, counter, totalscore, averagescore, finalletter)

    print()
    check = str.lower(input("Would you like to start over? Please enter \"Y\":\t"))
    
print("You didn't enter \"Y\".")
print("Good-bye.")

sys.exit(0)
