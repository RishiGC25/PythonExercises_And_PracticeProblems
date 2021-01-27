# Exercise 4
# Pattern Printing
# Input = Integer n
# Boolean = True or False
#
# True n=4
# *
# **
# ***
# ****
#
# False n=4
# ****
# ***
# **
# *

print("Enter the number of rows 'n' ")
n = int(input())
print("Enter 1 for true;and 0 for false;")
print("True will print a normal triangle with", n, "rows and false will print an inverted triangle with same rows")
boo = int(input())
TrueOrFalse = bool(boo)

if TrueOrFalse:
    for i in range(1, n+1):
        for j in range(1, i+1):
            print("*", end=" ")
        print()

else:
    for i in range(n, 0, -1):
        for j in range(1, i+1):
            print("*", end=" ")
        print()
