#operater:They are symbols which can be used to do arithemetic,logical or assignment operations on values called operands.
#operands:They are the numbers or values or variables on which operations are done on.
#Types of operators:-
#1.arithmetic operators:-These operators perform mathematical operations.Such as addition(+) , subtraction(-), multiplication(*),division(/),modulus(%),floor division(//) and exponentiation(**).

# Example for Arithmetic operations:
# a=15
# b=3
# print("This is the sum of a and b: ",a+b)
# print("This is difference between a and b: ",a-b)
# print("This is the product of a and b: ",a*b)
# print("This will give the result of division between a and b: ",a/b) # 4/5=0.8, It will give us result for the whole division. 
# print("This is will give us the quotient from a and b: ",a//b) # Will not give us any results in decimals, but if the dividend is already in decimal then it will return us the result in decimal. 20//5=4
# print("This will raise the power of a to b: ",a**b)
# print("This will give us the remainder when we divide a from b: ",a%b)

#2.comparison operators:-These operators are used ot compare 2 operands and return either true or false.Such as:-equal to(==),not equal to(!=),greater than(>),less than(<),greater than equal to(>=),less than equal to(<=).

# Example for comparison operations: 
a=15
b=3
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)
print(a==b)

#3.assignment operators:-These operators assign values to variables or pdate the current value of variables with new values,often combining arithmetic or bit wise operation.Such as simple assignment(=),add and assign(+=),subtract and assign(-=),multiply and assign(*=),divide and assign(/=),floor and assign(//=),exponentiate and assign(**=),modulus and assign(%=)

# Example for assignment operators:
total=560
total+=300
print("Line 33: ",total) #new value after doing add and assing
total-=15
print("Line 35: ",total)
total *=2
print("Line 37: ",total)
total/=2
print("Line 39: ",total)
total//=25
print("Line 41: ",total)

#4.logical operators:-They are used for logical operations such as AND ,OR and NOT.



# Activity 1: Write a Python program that tracks a farmer's harvest across 5 fields. You will calculate the total and average yield, pack the harvest into 25 kg bags, find the leftover grain, compare this year's harvest with last year's, and update the total with a bonus crop and seed reserve.