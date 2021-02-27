# Exercise 2 - Faulty Calculator
# Design a calculator which will correctly solve all the problems except
# the following ones:
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# The program should take operator and the two numbers as input from the user and then return the result

import time

print("Enter operator(+ or - or * or / )")
str = input()
op = str.strip()
a = int(input("Enter first number"))
b = int(input("Enter second number"))

time.sleep(1.5)

if op == "+":
    if ((a == 56) or (a == 9)) and ((b == 9) or (b == 56)):
        print(77)
    else:
        print(a + b)

elif op == "*":
    if ((a == 45) or (a == 3)) and ((b == 3) or (b == 45)):
        print(555)
    else:
        print(a * b)

elif op == "-":
    print(a - b)

elif op == "/":
    if ((a == 56) or (a == 6)) and ((b == 6) or (b == 56)):
        print(4)
    else:
        print(a / b)

else:
    print("\nCan't do this")

time.sleep(3.0)
