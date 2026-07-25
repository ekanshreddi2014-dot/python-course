#data types:Data Types are the type of values a variable can hold/store , it's the classification of whether the variable stores a float,integer,string or a boolean and which operation can be performed on it.
#type of data types: 
# 1.integer
# 2.float
# 3.boolean
# 4.string
# example:
a = "Hello!"
print(type(a))
#typecasting: It's a method of convert one variable datatype into a specific datatype.
# example:
x = False
y = 67
print(int(x)+y)
#user input: Taking input from the user
#string operations:
# length: Number of charecters in a string.
# indexing: position of specific charecter in a string.
# slicing: To obtain a specific part of a string.gh[start:end:steps]
# cancatenation: Adding to strings.
# example:
gh = "string"
print(len(gh))
print("the charecter at index 3:  ",gh[3])
print(gh[0:1])
print(gh[3:])
print(gh[-1])
print("hello"+" world")