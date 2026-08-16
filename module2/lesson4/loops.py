#loops:they are statements that are executed several times sequentialy. 
#types of loops:
#for loop:it is used to repeat over a sequence such as string.
#while loop:it executes a statement or a group of statemnets until the give condition is true.
#nested loops:the loops which have one or more loops inside another loop while or for loop.
#for loop example:
# n = "hello"
# for i in n:
#     print(i)

# range(start=0,end,step=1) range(end)

# for i in range(0,21,21):
#     print(i)

# Activity 1:
# Sum of whole numbers
# Outline:
# Write a program to calculate the sum of whole numbers.
#solution1:
num = int(input("give the range: "))
num1 = 0
for i in range(num):
    num1 = i * (n + 1)/2
print(num1)
    
# Activity 2:
# Reverse a String
# Outline:
# Write a program to reverse the string entered by the user.

# Solution 2:
String=input("Enter any string: ")
reversed_string=""

for i in String: #for i=0 i<5 i=i+1
    reversed_string=i+reversed_string 

print("Original String:",String)
print("Reversed String:",reversed_string)
# Activity 3:
# reverse order
# Outline:
# Write a program to print the numbers in reverse order beginning from the number entered by the user. range(n,0,1)
#solution3:
a = int(input("range"))
for i in range(a,-1,-1):
    print(i)