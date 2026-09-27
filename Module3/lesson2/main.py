#positional arguments : positional arguments are like values passed into function that gets matched to a parameter based upon the order it is listed.
#example:
# def subtract(a,b):
#     return a - b
# print(subtract(5,10))
#docstring: docstring is like a sticky note that we attach to a function that tells what a function does.
#example:
# def add(c,d):
#     """"this function adds two numbers and returns the result"""
#     return c + d
# print(add.__doc__)
#recursion : a function that keeps on calling itself to solve a smaller version of the saame problem.
#example:
# def count_down(n):
#     if n == 0:
#         print("blast off")
#     else:
#         print(n)
#         count_down(n-1)
# count_down(6)
# Tip, the waiter
# Outline:
# Let's create a function total_calc() that helps us calculate and print out the total amount paid at a restaurant. Given a bill amount and the percentage of the bill amount you decide to pay us a tip (tip_perc ), this function calculates the total amount you should pay.
# Cube of the cube
# Outline:
# Define a function to find a cube and define another function which let execute the cube function if the number is divisible by 3
# Factorial
# Outline:
# Write a program to find the factorial using recursive function
#solution1:
# def total_calc():
#     b = int(input("what is the bill? : "))
#     c = int(input("what is the bill you want to pay? : "))
#     d = c / 100 *b
#     x = d + b
#     return x
# print("the total bill is ",total_calc())
#solution2:
# def cube():
#     e = int(input("what is the number? : "))
#     return e * e * e
# def check(f):
#     g = f % 3
#     if g == 0:
#         print("the number is divisable by three")
#     else:
#         print("the number is not divisable by three")
# f = cube()
# print(f," is the cubed number")
# print(check(f))

