#indentation:An indentation is a 4 space gap given after a conditional statement.
#conditional statement: A conditional statement is a statement used for doing an action when a certain condition given by the user is fulfilled.
#i = 5
#if i > 2:
#    print("the condition works")
#if statement: 'if' statement runs only when the condition is true.
#if i > 2:
 #   print("the condition works")
#else:
   # print("the condition doesn't work")    
#else statement:this statement only gets executed when the above conditional statements (elif and if) are proved wrong.
# Weather Outfit Picker
# Outline:
# A Weather Outfit Picker that asks about temperature, rain, wind, and puddles, then uses if and if-else statements to decide what outfit, umbrella, windbreaker, and shoes to wear, all while keeping every block properly indented.
# Step 1: Ask for today's temperature and use if-else to decide between a jacket and a t-shirt.

# Step 2: Ask whether it is raining, and use an if statement to print an umbrella reminder.

# Step 3: Ask for the wind speed and use if-else to decide if a windbreaker is needed.

# Step 4: Ask whether there are puddles and use if-else to decide between boots and sneakers.

# Step 5: Print a message that sits outside every if and else block.

# Step 6: Print the final outfit summary with every decision made
#code:
a = int(input("today' temperature: "))
b = input("is it raining: ")
c = int(input("wind speed: "))
d = input("are there puddles: ")
if a > 30:
    print("You should wear T-shirt")
else:
    print("you should wear a jacket")
if b == "yes" :
    print("You should use an umbrella")
else:
    print("no need for an umbrella")
if c < 50 :
    print("no need for a wind breaker")
else:
    print("you should use a wind breaker")
if d == "yes" :
    print("You should wear gum boots")
else:
    print("no need for gum boots")
print("the temperature is :",a,"degrees celsius")
print("raining or not :",b)
print("speed of the wind :",c,"km per hour")
print("puddles or not :",d)
