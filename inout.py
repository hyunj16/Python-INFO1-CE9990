import sys

choice = "y"
while choice == "y":
    print()
    print("Welcome to Freelance Salary Calculator.")
    print()

    try:
        input1 = input("What is your hourly rate?\t$ ")
    except EOFError:
        sys.exit(0)
    try:
        hourlyrate = float(input1)
    except ValueError:
        print("You must be an unpaid-intern. $0 / hour")
        hourlyrate = 0
    #print(hourlyrate)

    try:
        input2 = input("How many hours a day do you work?\t")
    except EOFError:
        sys.exit(0)
    try:
        hoursaday = int(input2)
    except ValueError:
        print("I will assume 0 hours / day.")
        hoursaday = 0
    #print(hoursaday)
    
    try:
        input3 = input("How many days do you work in a week?\t")
    except EOFError:
        sys.exit(0)
    try:
        daysaweek = int(input3)
    except ValueError:
        print("I guess you don't work.")
        daysaweek = 1
    #print(daysaweek)
    
    weeksinayear = 52

    salary = hourlyrate * daysaweek * hoursaday * weeksinayear
    #print(salary)
    salaryinK = salary/1000
    #print(salaryinK)
    salaryinthousands = int(round(salaryinK))
    
    print()
    print("Your salary is about ", "$ ", salaryinthousands, "K." , sep="")
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
