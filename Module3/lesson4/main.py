#exception handling : an exception is a way of python saying omething went wrong wjile the progra was running . when anything  like this happends python tsops and shows an error message unless you handle / resolve it .
#catching errors with try and except : 
#example :
# try:
#     number = int(input("enter a number "))
#     print("you entered ",number)
# except:
#    print("that wasn't a valid number")
#example :
# try:
#     a = int(input("enter a number "))
#     b = int(input("enter another number "))
#     print(a / b)
# except ValueError:
#     print("please enter numbers only")
# except ZeroDivisionError:
#     print("you cannot divide ny zero")
#example :
# try:
#     a = int(input("enter a number "))
# except ValueError:
#     print("invalid number")
# else:
#     print("you entered",a)
# finally:
#     print("done")
#retrying with a loop until the input is valid :
#example :
# while True:
#     try:
#         a = int(input("enter a number "))
#         break
#     except ValueError:
#         print("INVALID NUMBER")
# print("your number is ",a)
#activity:
#1Value Error
#Outline:
# Write a program to understand how the value error exception works?
#2Multiple exceptions
#Outline:
# Write a program to check how the exceptions and finally statement works
#3Bye Bye
# Outline:
# Write a program using nested while loop. If the value is divided by two, then it will run an infinite loop of the bye. 
#solution1:
try:
    a = int(input("what is the operand"))
    b = int(input("what is the operand"))
    print(a + b)
except ValueError:
    print("invalid value")
#solution2:
try:
    c = int(input("what is the operand"))
    d = int(input("what is the operand"))
except ValueError:
    print("incorrect value")
else:
    print(c + d)
finally:
    print("operation complete")
#solution3:
while True:
    try:
        e = int(input("what is the number"))
        f = e % 2
        if f == 0:
            print("bye")
            continue
        else:
            break
    except ValueError:
        print("invalid number")