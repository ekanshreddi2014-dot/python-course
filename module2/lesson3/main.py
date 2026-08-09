#nested conditional statements
#nested if statements:a nested if is an if statement written inside another if block.
#nested if-else statement:a nested if-else statemment adds a branch inside the outer if block.this means , every inner decision has two outcomes:-one for true and one for false 
#example:
i = 10
# if i >= 8:
#     if i <= 12:
#         print("i is smaller than 12 ")
#     else:
#         print("i s greater than 12")
# else:
#     if i <= 8:
#         print("i is smaller than 8")
#     else:
#         print("i is greater than 8")
# if i >= 8:
#     if i == 10:
#         print("i is 10")
#     if i >= 9:
#         print("i is greater than 9")
#     if i > 10:
#         print("i is greater than 10")    
#=========ACTIVITT===========
#Custom Ride Builder
# Outline:
# A Python program that prints a welcome banner. It asks you to pick a vehicle — Bike or Car. It uses a nested if-else inside each branch to ask for a specific model. It prints the name, top speed or seats, and best use case for the chosen model. It handles invalid input with an else at the outer level. It closes with a goodbye message.
# SKILLS PRACTISED

# Nesting concept, nested if, nested if-else, indentation levels, multi-level decision making, integer

# input with int(input()), and if-elif-else chaining.

# STEPS

# Step 1: Print the welcome banner: " === Welcome to Ride Builder! === ".

# Step 2: Print the Step 1 menu: "1 - Bike" and "2 - Car". Take input and store in choice.

# Step 3: Write the outer if for choice == 1 (Bike branch).

# Step 4: Inside the Bike branch, print the Step 2 bike menu. Take input and store in bike_type.

# Step 5: Write a nested if-else for bike_type: Scooty details if 1, Mountain Bike details if else.

# Step 6: Write the outer elif for choice == 2 (Car branch).

# Step 7: Inside the Car branch, print the Step 2 car menu. Take input and store in car_type.

# Step 8: Write a nested if-else for car_type: Sedan details if 1, SUV details if else.

# Step 9: Write the outer else to print an invalid choice message.

# Step 10: Print the closing banner: " === Your custom ride is ready! === ".
#activity:
print("===Welcome To Vehicle Selection Menu===")
print("which vehicle do you want ? : 1 for bike and 2 for car")
a = input("which do you want ? : ")
if a == "1":
    bike_type = input("which kind of bike do you want ? : 1 for mountain bike and 2 for scooty")
    if bike_type == "2":
        print("here are the details for scooty:" \
              " top speed : 100 kmp" \
              " colour : red" \
              " weight : 100 kg")
    else:
        print("here are the details for mountain bike:" \
              " top speed : 200 kmp" \
              " colour : green" \
              " weight : 60 kg") 
elif a == "2":
    car_type = input("which kind of car do you want ? : 1 for suv and 2 for sedan")
    if car_type == "2":
            print("here are the details for sedan:" \
                  " top speed : 200 kmp" \
                  " colour : brown" \
                  " weight : 600 kg")
    else:
        print("here are the details for SUV:" \
              " top speed : 150 kmp" \
              " colour : white" \
              " weight : 1000 kg") 