#nested loops : nested loops are loops which are in one-another.
#nested while loops: a while loop which is in another while or for loop.
#example:
# i = 1
# while i <= 5:
#     j = 1
#     while j <= 10:
#         print(j,end=" ")
#         j = j + 1
#     print()
#     i = i + 1
#nested for loops: a for loop which is in another for or while loop.
#example:
for i in range(1,5):
    for j in range(1,11):
        print(j,end=" ")
    print()
#activity:
# ATM Cash Dispenser
# Outline:
# This one activity keeps you working with both nested loop types end to end - a daily ATM session that serves several customers, then a denomination report printed once the day is done.
# WHAT YOU WILL BUILD

# You build a program that serves customers one at a time at an ATM, breaking each withdrawal

# into notes, then prints a daily denomination report once the session ends.

# HOW IT WORKS

# Step 1: Set up six counter variables (one per note value) plus counters for customers served and

# total dispensed, all starting at 0.

# Step 2: Start an outer while loop that keeps serving customers until the flag variable serving

# becomes False.

# Step 3: Ask for the customer's name and withdrawal amount; if the amount is invalid, print a

# message and continue back to the top of the loop.

# Step 4: Inside that same repeat, run an inner while loop that checks each of the six note values

# one at a time and works out how many of each note to dispense.

# Step 5: Update the matching counter variable for whichever note value was just dispensed, then

# ask if there is a next customer, setting serving to False if not.

# Step 6: Once the outer while loop ends, start an outer for loop stepping through each of the six

# note values to print the daily denomination report.

# Step 7: Inside that same repeat, run an inner for loop that prints one symbol for every note of that

# # value dispensed across the whole day.
#solution:
a = 1
b = 10
c = 50
d = 100
e = 500
f = 1000
customers_served = 0
total_dispensed = 0
flag = True
customer_name = input("what's your name ? : ")
while flag == True:
    withdrawel_amount = int(input("how much do you want to withdraw ",customer_name,"?: "))
    if withdrawel_amount <= 0:
       print("invalid amount please try again")

