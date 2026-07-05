import keyword
#1. git add . :this command should be used when we want add a file or update any changes to github
#2. git commit -m "message" :this command will be used after line number 1, it will be used for telling what this update or file is about.
#3. git push origin branch name (master) :this command is used to insert or push a file or an update to git hub.

# Today's topics:
# 1. Identifiers: They are used to name a varibale,function, class or modules,etc. , it can be an alphabet, contain a digit or combination of alphabet, underscore, digit. example: my_name
# 2. Variables: They are user-defined, it is a quantity that  may change or update with the conrtext of program or condition. It has no specific command for generating variables. example: sum=6+5
# 3. Keywords: They are pre-defined that has some specific meaning reserved for the programmming language. Example: print,int,float,etc.

# a = input("number: ")
# key=41451
# # lock
# True="154"
# print(True)


# Activity 1: Write a program for print command.
#Activty 2: Write a program to create different variables to store various values.
# Activity 3: Write a program to print all the keywords
print("hi, my name is ekansh.")
a = 10
b = 5
c = "canned food"
print(a,b,c)
print(keyword.kwlist)