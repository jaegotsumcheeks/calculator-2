"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here
calculation = input("What is your calculation? (e.g + 12) >> ")

tokens = calculation.split(" ")

operator = tokens[0]
num1 = int(tokens[1])
num2 = int(tokens[2])

if operator == "+":
   x = add(num1,num2)
elif operator == "-":
   x = subtract(num1,num2)
elif operator == "*":
   x = multiply(num1,num2)
elif operator == "/":
   x = divide(num1,num2)
elif operator == "square":
   x = square(num1,num2)
elif operator == "cube":
   x = cube(num1,num2)
elif operator == "pow":
   x = power(num1,num2)
elif operator == "mod":
   x = mod(num1,num2)
