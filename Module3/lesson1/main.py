#function: function is a block of code that foes one specific task and we can use it again and again without rewriting the whole code.
#syntax:
#def hello():
#Example:
# def hello():
#     print("hello!,world")
# def greet():
#     hello()
# greet()
#types of function:1.built in function:Ex :- print function
#                  2.user-defined function: Ex :- greet
#parameters:parameters are the input that we define at a time of function creation.they are given in the round brackets which are after the function name.
#arguments:they are pieces of information we place inside the parentheses when we call a function.so that we can use different values every single time.
#example:
# def greet(name):
#     return ("hello "+name)
# print(greet("ekansh"))


def add(a,b):
     return a + b
def subtract(a,b):
     return a - b
def calculate(a,b):
    operation = input("what operation do you want to perform add or subtract: ").lower()
    if operation == "add":
        print(add(a,b))
    elif operation == "subtract":
        print(subtract(a,b))
    else:
        print("plese provide a valid operation")
calculate(67,1)
#classroom activity:
# My Lemonade Stand Calculator
# Outline:
# A Lemonade Stand Calculator that greets every customer, calculates the total cost and change due using functions with arguments and return statements, and prints a personalized thank you message alongside the final receipt.
#solution:
