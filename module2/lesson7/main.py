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
# i = 1
# c = 5
# for a in range(0,5):
#     for b in range(0,i):
#         print(" ")
#         i = i + 1
#     for e in range(0,c):
#         print("*",end=" ")
#         c = c - 1
# i = 1
# c = 5
for a in range(0, 5):
    # 1. Print all spaces for this row
    for b in range(0, a):  # Uses 'a' directly to increase spaces each row
        print(" ", end="")

    # 2. Print all stars for this row
    for e in range(0, c):
        print("*", end=" ")

    # 3. Move to the next line and decrease star count
    print()
    c = c - 1
