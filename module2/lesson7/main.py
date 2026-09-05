#pattern:its a repeated or systematic arrangement of characters like numbers or stars in a specific shape such as triangle ,diamond etc.
#nested for loop:
# a = int(input("enter number: "))
# for i in range(a):
#     for j in range(i+1):
#         print(j,end=" ")
#     print()
#activities:
# 1.Right angle triangle
# Outline:
# Write a program to demonstrate a right angle triangle pattern?
# 2.Floyd’s triangle
# Outline:
# Write a program to demonstrate a Floyd triangle pattern?
# 3.Diamond Pattern
# Outline:
# Write a program to demonstrate the numbers in a diamond pattern?
#solution1:
# a = 6
# for i in range(a):
#     for j in range(i + 1):
#         print(j,end="  ")
#     print()
#solution2:
# a = 6
# num = 1
# for i in range(1,a+1):
#     for j in range(1,i + 1):
#         print(num,end="  ")
#         num += 1
#     print()
#solution3:
a = 2
b = 1
for i in range(0,a):
    print(" ")
    a = a - 1
    for j in range(0,b):
        b = b + 1
        print("*")
    print(end="")

    