#random module:the random module is a feature of python which we can use to get a numbers which at first seem like random but are dependent on th specific enviroment in the computer.
#example:
# import random 
# print(random.random())
#math module:it is a built in python tool kit for calculation that go beyond basic arithematics.
#example:
# import math
# print(math.ceil(23.56))
# print(math.floor(23.56))
# print(math.copysign(10,-2))
# print(math.sqrt(67))
# print(math.fabs(-96))
# print(math.gcd(24,56))
# #activity:
# Number game
# Outline:
# Write a program to generate a random integer and match it with the input given by the user?
# Project:
# https://codingal.s3.ap-south-1.amazonaws.com/media/blackops/lesson-plan-assets/Random_and_math_module_bpc-65dc.zip
# Rock paper scissors
# Outline:
# Create a program to play rock, paper, and scissors. Use a random module to select from the given options Check whether the random guess matches the user’s answer
# Project:
# https://codingal.s3.ap-south-1.amazonaws.com/media/blackops/lesson-plan-assets/Random_and_math_module_bpc-65dc.zip
# Mathematical operations
# Outline:
# Write a program to understand the different functions of the math module.
# Project:
# https://codingal.s3.ap-south-1.amazonaws.com/media/blackops/lesson-plan-assets/Random_and_math_module_bpc-65dc.zip
#solution1:
import random
a = random.randint(0,100)
while True:
    b = int(input("please submit your guess"))
    if b < a:
        print("your guess is lower than the random number")
    elif b > a:
        print("your guess is greater than the random number")
    else:
        print("congratulation you succeeded")
        break

