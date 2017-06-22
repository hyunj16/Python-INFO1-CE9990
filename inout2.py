import sys

choice = "y"
while choice == "y":
    print()
    print("Welcome to Tip Calculator.")
    print()

    try:
        input1 = input("How much is your bill?\t$ ")
    except EOFError:
        sys.exit(0)
    try:
        bill = float(input1)
    except ValueError:
        print("You are not paying the bill. You entered $0.")
        bill = 0
    #print(bill)

    try:
        input2 = input("What perecentage are you willing to pay as a tip?\t")
    except EOFError:
        sys.exit(0)
    try:
        percentage = float(input2)
    except ValueError:
        print("You entered 0%.")
        percentage = 0
    #print(percentage)
    
    try:
        input3 = input("How many people are paying the tip?\t")
    except EOFError:
        sys.exit(0)
    try:
        people = int(input3)
    except ValueError:
        print("I guess you don't work.")
        people = 1
    #print(people)
    
    tip = bill * percentage / 100 
    #print(tip)
    tipperperson = round(tip / people, 2)
    #print(tipperperson)

    
    print()
    print("Your bill came out to be ", "$", bill, ".", sep="")
    print("You wanted to pay a ", percentage, "% tip.", sep="")
    print("So you are paying $ ", tip, " in total.", sep="")
    print("You are dividing the tip among ", people, ".", sep="")
    print("So you all need to pay $", tipperperson, " per person.", sep="")
    print()
    
    try:
        input4 = input("Would you want to calculate again? Press \"Y\" to continue. ")
    except EOFError:
        sys.exit(0)
    try:
        choice = str(input4)
        choice = str.lower(choice)
    except ValueError:
        print("You must mean \"N\".")
        choice = "n"

print()    
print("You didn't press \"Y\".")
print("Thank you for using. Bye.")
print()
sys.exit(0)
