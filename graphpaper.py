import sys

r = int(input("How many rows of boxes?\t"))
c = int(input("How many columns of boxes?\t"))
rb = int(input("How many rows of blanks in each boxes?\t"))
cb = int(input("How many columns of blanks in each boxes?\t"))

plus = ("+")
dash = ("-")
bar = ("|")
space = (" ")

h = 1
while h <= c:
    
    j = 1
    while j <= r:
        print(plus, end="")
        print(cb*dash, end="")

        j += 1
    print(plus)

    l = 1
    while l <= rb:
        i = 1
        while i <= r:
            print(bar, end="")
            print(cb*space, end="")
            i += 1
        print(bar)
        l += 1
    
    h += 1

m = 1
while m <= r:
    print(plus, end="")

    n = 1
    while n <= cb:
        print(dash, end="")
        n += 1
    m += 1
print(plus)
    
sys.exit(0)
