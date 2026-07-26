# Python operator II:
# example:
# a = 300
# if a > 100:
#     print("a is greater than 100")
# elif a < 100:
#     print("a is smaller than 100")
# else:
#      print("the position of a in the integer scale is unknown")
# if-elif-else:- these statemets are called conditional statements.these statements are used to make decisions based on the criteria given by the user.

# Logical Operators (returns boolean values): 
# 1. AND : It joins two conditions together, both the conditions must be True for the whole expression to be True.
# example:
a=2
b=3
c=5

# if a>1 and b<3 and c==5:
#     print("All the conditions are True")
# else:
#     print("One condition is False.")

# 2. OR : It joins two conditions together, at least one condition must be True, for the whole expression to be True.
# example:

# if a>1 or (b<3 and c!=5):
#     print("One of the conditions is True")
# else:
#     print("One condition is False.")

# 3. NOT : It reverses the boolean value.
# example:

# if not (b<3 and c==5) or a>1 :
#     print("One of the conditions is True")
# else:
#     print("One condition is False.")

# Activity 1:
# A Python program that asks the user three questions. It classifies the day using if-elif-else. It uses AND to check sunny weather and homework done together. It uses OR to check rainy or cloudy weather. It uses NOT to catch homework not done. It combines all three operators to print the best plan for the day.

# Step 1: Print the welcome message: " === Smart School Day Planner === ".
# Step 2: Use input() to ask for the day, weather, and homework status. Store each in a variable.
# Step 3: Print the plan header using the day variable in an f-string.
# Step 4: Write if-elif-else to classify the day type (weekend / Monday / Friday / other school day).
# Step 5: Write an if statement using AND to check sunny weather and homework done together.
# Step 6: Write an if statement using OR to check rainy or cloudy weather.
# Step 7: Write an if statement using NOT to catch when homework is not done.
# Step 8: Write if-elif-else using AND, OR, and NOT combined to print the best plan message.
# Step 9: Print the closing message: "Plan complete! Have a wonderful day!"
# Step 10: Run the program with three different combinations of inputs to test all branches.
print("=== Smart School Day Planner ===")
day = input("what day of the week is it today?: ")
weather = input("how is today's weather like?: ")
homework_status = input("what is the homework status?: ")
if day == "sunday":
    print("weekend")
elif day == "monday":
    print("monday")
elif day == "monday":
    print("")
elif day == "monday":
    print("")g