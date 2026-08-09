#operators-III
#identity operators:these operators check whether 2 variables point to the same object memeory or not.identity operators:
#   1.is
#   2.is not
#example:
# a = 5
# b = 7
# c = a
# print(a is b)
# print(b is c)
# print(c is a)
# print(a is not c)
# print(b is not a)
#membership operators:these operators check whether a value can be found in a collection of items or not.operators: in and not in
#example:
# sentence = "HELLO WORLD!"
# print("O"in sentence)
# print("xyz"not in sentence)
#bit-wise operators:6 bit wise operators
#1:- &(and)
#2:- |(or)
#3:- ~(not)
#4:- ^(xor)
#example:-
# a = 5
# b = 3
# print(a & b)
# print(a | b)
# print(~ b)
#a = 0101
#b = 0011
#Write a program to illustrate the use of 'is' identity operator
#Write a program to show students’ grades by entering marks for five subjects, calculating the average, and checking the grade range using membership operators in and not in. For example, use in to check whether the average is in the range 91 to 100, 81 to 90, and so on, and use not in to validate marks outside the allowed range.
#example:
a = input("value a :")
b = input("value b :")
c = input("value c :")
print(a is b)
print(a is c)
print(b is c)
print(a is not b)
print(a is not c)
print(b is not c)
