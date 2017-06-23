import sys

r = int(input("How many rows of boxes?\t"))
c = int(input("How many columns of boxes?\t"))
rb = int(input("How many rows of blanks in each boxes?\t"))
cb = int(input("How many columns of blanks in each boxes?\t"))

a = str("+")
b = str("-")
d = str("|")
e = str(" ")

h = 1
while h <= c:
    
    j = 1
    while j <= r:
        print(a, end="")

        k = 1
        while k <= cb:
            print(b, end="")
            k += 1

        j += 1
    print(a)

    l = 1
    while l <= rb:
        i = 1
        while i <= r:
            print(d, end="")
            print(cb*e, end="")
            i += 1
        print(d)
        l += 1
    
    h += 1

m = 1
while m <= r:
    print(a, end="")

    n = 1
    while n <= cb:
        print(b, end="")
        n += 1
    m += 1
print(a)
    
sys.exit(0)
