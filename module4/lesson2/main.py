#tuple:tuple is an ordered collection of items grouped together in one container . once created the items inside tuples can never be changed.
#example:
# tuple1 = (1111,"a",6767,"hello")
# print(tuple1)
#keyword :- tuple() : we can convert anything into tupe by using the tuple function
# list1 = ["a",676767,"six seven",1]
# tuple2 = tuple(list1)
# print(tuple2)
#example:
# str1 = ("apple")
# tuple3 = "apple","banana"
# print(type(str1))
# print(type(tuple3))
#example:
# a = int(input("what is the number?"))
# tuple1 = (1,2,3,4,5,6,7,8,9)
# tuple2 = tuple1 + (a,)
# print(len(tuple1))
# print(tuple1[2:7])
# print(tuple1)
# print(tuple2)
# #activity:
# Tuple Operations
# Outline:
# Write a program to perform the following operations: 1. Create a tuple with different datatypes 2. Create another tuple of integers 3. Create a new tuple by adding 9 to the previous tuple 4. Count the occurrences of an element in the tuple 5. Perform slicing on the tuple
# Project:
# https://codingal.s3.ap-south-1.amazonaws.com/media/blackops/lesson-plan-assets/Tuples_bpc-5c43.zip
# Flip Flop
# Outline:
# Write a program to check whether the given tuple - (1,2,3,3,2,1) is a palindrome or not. If it's a palindrome, then it is the same after being reversed.
# Project:
# https://codingal.s3.ap-south-1.amazonaws.com/media/blackops/lesson-plan-assets/Tuples_bpc-5c43.zip
# Weather Prediction
# Outline:
# Create a tuple named weather with these elements - (1, 0, 0, 0, 1, 1, 0). If the element is 1 then the value of rainy increases by 1 otherwise the value of sunny increases by 1. On the basis of the value of rainy and sunny, predict the weather.
# Project:
# https://codingal.s3.ap-south-1.amazonaws.com/media/blackops/lesson-plan-assets/Tuples_bpc-5c43.zip
#solution1:
tuple1 = (1,"a",1.1,True)
print(tuple1)
tuple2 = (1,2,3,4,5,6,7,8)
print(tuple2)
tuple3 = tuple1 + (9,)
print(tuple3)
print("nine occurs ",tuple3.count(9))
print(tuple3[2:4])
#solution2:
a = (1,2,3,4,3,2,1)
b = len(a)
c = b // 2
d = a[0:c]
print(d)
e = len(d)
f = (e - (e * 2)) - 1
g = a[-1:f:-1]
print(g)
if d == g:
    print("the tuple is a palindrome")
else:
    print("the tuple is not a palindrome")
#solution3:
weather = (1,0,0,0,1,1,0)
rainy = 0
sunny = 0
for element in weather:
    if element == 1:
        rainy += 1
    else:
        sunny += 1
if rainy > sunny:
    print("it rained more days")
else:
    print("it was sunny more days")