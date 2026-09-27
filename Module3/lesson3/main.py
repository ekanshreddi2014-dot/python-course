#keywords:keywords are predefined words in python which can be used to do fuctions like print information , make desitions etc.
#return keyword:return keyword is the keyword used at the end of most functions it gives back the information which we got during the ongoing of a function and it ends the function where the return keyword is placed.
# example :
# def add(a,b):
#     return a + b
# print("hello!")
# print(add(3,4))
#break keyword:the break keyword immediatly stops the entire loop and jumps straight to the first line of code.
#example:
# for i in range(1,10):
#     if i == 5:
#         break
#     print(i)
#continue keyword:continue skips the remaining code in thecurrent loop and jumps to the next iteration .
#example:
# for i in range(1,10):
#     if i == 5:
#         continue
#     print(i)
#activity:
# Snack Vending Machine
# Outline:
# You build a snack vending machine that accepts coins one at a time, rejects invalid ones, stops once enough money is inserted, and calculates any change owed using a function.
#steps:
# Step 1: Define a function calculate_change(paid, price) that subtracts price from paid and returns the result.

# Step 2: Set the snack price and print a greeting showing the price and the accepted coin values.

# Step 3: Start a while True loop that keeps asking for coins, using continue to reject any coin that isn't 1, 5, 10, or

# 25

# Step 4: Add every valid coin to a running total and print how much has been inserted so far.

# Step 5: Use break to stop the loop the moment the total reaches or passes the snack price.

# Step 6: Call calculate_change() with the total inserted and the snack price to work out the change.

# Step 7: Use pass when the change is exactly zero, or print the change amount otherwise, then print a purchase

# summary.
# solution :
def calculate_change(paid,coins):
    answer = paid - coins
    return answer
print("chips = 10 rupees" \
"      cold drink = 20 rupees" \
"      frozen sandwich = 50 rupees")
print("hello customer what would you like to buy .")
print("here are the accepted coins : -" \
"      1,5,10 and 25 rupee")
flag = True
snacks = input("what snack do you want: ").lower()
coins = 0
if snacks == "chips":
    coins = 10
if snacks == "cold drink":
    coins = 20
if snacks == "frozen sandwich":
    coins = 50
coins_2 = coins
while flag == True:
    coins_given = int(input("please insert coin ."))
    if coins_given == 1 or coins_given == 5 or coins_given == 10 or coins_given == 25:
        coins = coins - coins_given
        print(coins_2 - (coins_2 - (coins_2 - coins))," coins has been give")
        if coins <= 0:
            print("payment complete")
            break
        else:
            continue 
    else:
        print("invalid coin")
        print("please insert again")
paid = coins_2 - (coins_2 - (coins_2 - coins))
print(calculate_change(paid,coins_2)," rupees returned")